## covid

The data is up-to-date as of September 18th, 2020.

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
