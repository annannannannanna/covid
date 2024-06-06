## covid

The data is up-to-date as of September 18th, 2020.

The data is stored in the **"covid.json"** file, under the **"[first](http://https://github.com/annannannannanna/covid/releases/tag/first "first")"** tag .


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

```python
import json

def max_value(value_name):
    data = json.loads(open("/Users/imac/Documents/covid/covid.json", "rt").read())
    result = []
    
    for code, country_data in data.items():
        country = country_data["location"]
        
        if value_name not in country_data:
            continue 
        
        value = country_data[value_name]
        result.append((country, value))
    result = sorted(result, key = lambda x: -x[1])
    
    return result[0][0]

value_name = 'median_age'
print(max_value(value_name))
```

Now let's take a look at the daily indicators. Let's find the day in August when the total value of the "value_name" indicator was the highest for all countries.

We will write a function called "day_with_max_value" that will return the string indicating this date.

The function "day_with_max_value" will take in a parameter "value_name" and return the date (in the format "2020-08-dd") of the day when the total "value_name" was the maximum for all countries in August.

Sample input: "day_with_max_value('new_cases')"
Sample output: "2020-08-13"

```python
import json
def day_with_max_value(value_name):
    data = json.loads(open("data/covid.json", "rt").read())
    result = [0.0 for _ in range(31)]
    for code, country_data in data.items():
        country = country_data["location"]
        for entry in country_data["data"]:
            if "date" not in entry:
                continue
            date = entry["date"]
            if date[:7] != "2020-08":
                continue
            day = int(date[8:]) - 1
            result[day] += entry.get(value_name, 0.0)
    max_day = 0
    for i in range(31):
        if result[i] > result[max_day]:
            max_day = i
    return "2020-08-%02d" % (max_day + 1)
```

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
