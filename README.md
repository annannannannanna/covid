## covid

The data is up-to-date as of September 18th, 2020.

The data is stored in the **"covid.json"** file, under the **"[first](https://github.com/annannannannanna/covid/releases/tag/first)"** tag.

At the top level, there is a dictionary that contains a country code as the key and country data as the value. The full name of the country can be found in the "location" field. In addition to the "location", there are several other fields that contain general statistics about the country:

- "population"
- "population_density"
- "median_age"
- "aged_65_older"
- "aged_70_older"
- "diabetes_prevalence"
- "life_expectancy"


  In addition, this object has a data field containing actual infection data. This field points to an array (list) of data, each item of which has the following fields:
  
- "date" (YYYY-MM-DD)
- "total_cases"
- "new_cases"
- "total_deaths"
- "new_deaths"
- "total_tests"
- "new_tests"

For the number of registered cases and deaths, the data is also provided normalized to a million people (e.g., new_cases_per_million). Similarly, for tests, the number is provided per thousand people (e.g., new_tests_per_thousand).

Let's start by finding countries with the highest indicators. To do this, we will use the **max_value()** function, which takes a **value_name** as an input parameter. The function should return the **location** of the country with the highest **value_name** for the specified indicator.

Let's write a function called **max_value** that takes in a **value name** and returns the name of the country with the highest **value_name** for that indicator.
 - sample input: max_value('median_age')
 - sample output: "Japan"

[covid_1.py](https://github.com/annannannannanna/covid/blob/main/covid_1.py)

Now let's take a look at the daily indicators. Let's find the day in August when the total value of the "value_name" indicator was the highest for all countries.

We will write a function called "day_with_max_value" that will return the string indicating this date.

The function "day_with_max_value" will take in a parameter "value_name" and return the date (in the format "2020-08-dd") of the day when the total "value_name" was the maximum for all countries in August.

Sample input: "day_with_max_value('new_cases')"
Sample output: "2020-08-13"

[covid_2.py](https://github.com/annannannannanna/covid/blob/main/covid_2.py)

Now, let's calculate the correlation between the number of tests and the number of positive cases. We can use the following formula to do this:

```python
def corr(data_x, data_y):
    sx, sy, sxy, sx2, sy2, n = 0.0, 0.0, 0.0, 0.0, 0.0, 0
    for x, y in zip(data_x, data_y):
        sx += x
        sx2 += x*x
        sy += y
        sy2 += y*y
        sxy += x*y
        n += 1
    dd = math.sqrt((sx2 / n - (sx / n * sx / n)) * (sy2 / n - (sy / n * sy / n)))
    if abs(dd)  < 1e-5:
        return None
    return (sxy / n - sx / n * sy / n) / dd
```

This coefficient indicates the degree of interdependence between two variables.
If, as one variable increases, the other also increases, then the correlation coefficient will be closer to 1.
If one variable increases while the other decreases, the correlation coefficient will be closer to -1.
If there is no relationship between the two variables, the correlation coefficient will approach 0.

If you calculate this coefficient for tests and detected cases, you can gain some insights into the processes occurring. For instance, if the correlation is negative, it might indicate that during the decline of the epidemic, the country increased the number of tests significantly. If the correlation is strong, then perhaps there were not enough tests initially, and with increased testing, detectability began to rise.
To draw confident conclusions, it is important to look at these values over time and take into account all relevant factors. The correlation value itself does not provide a definitive answer, but it can provide some clues. 

Write a function called float_with_precision that takes a country code as an argument and returns the value of the correlation coefficient between the number of tests conducted and the number of cases detected in August. If any of the values are missing for a particular day, assign it a value of 0.

Implement the "float_with_precision(country_code)" function, which calculates the correlation between the number of tests and the number of cases found in August for a given country code.

Sample input: float_with_precision("IND")
Sample output: 0.5935340285658485

[covid_3.py](https://github.com/annannannannanna/covid/blob/main/covid_3.py)

Now we want to determine the stability of the value_name parameter (for example, the number of reported cases). To do this, we can calculate the standard deviation - the square root of the variance. You have already encountered this indicator when completing tasks based on random variables. Recall that the mean and COE can be calculated as follows:

```python
def calc_mean_sigma(data):
    sx, sx2, n = 0.0, 0.0, 0
    for x in data:
        sx += x
        sx2 += x*x
        n += 1
    return (sx / n, math.sqrt(max(sx2 / n - sx / n * sx / n, 0)))
```

This parameter shows how far the indicator is from its average value.
In the previous task, this could give you some insights into the processes that are happening. If the spread is large, it may indicate a rapidly evolving process. Another possibility is that some countries do not publish statistics on weekends, while at the beginning of the week there are jumps. By looking at how the COEX system changes over time, you can formulate hypotheses and try to verify them. 

Your sigma function should take two parameters - "country_code" and "value_name" - and return one number - the standard deviation of the "value_name" for August.

Implement the "sigma(country_code" function.

Sample input: sigma('GBR', 'new_cases')
Sample output: 235.76391655560022

[covid_4.py](https://github.com/annannannannanna/covid/blob/main/covid_4.py)

In the previous problem, we calculated the standard deviation. However, it is difficult to compare this indicator across different countries as the average values of indicators vary significantly between countries.

To address this, let's attempt to normalize the COEX ratio by adjusting it to the expected value. The formulas for calculating the COE and average are provided in the previous problem. These calculations will help us determine whether the process is stable and the accounting system is ideal. Alternatively, the data may be artificially constrained within a specific range. To determine this, we will calculate the normalized COE for each indicator. 

The sigma_norm() function will take two parameters: country_code and value_name. 

The function should return a single value - the standard deviation divided by the expected value of the specified indicator in August.

Sample input: sigma(‘RUS’, ‘new_cases’)
Sample output: 0.05748491556302192

[covid_5.py](https://github.com/annannannannanna/covid/blob/main/covid_5.py)
