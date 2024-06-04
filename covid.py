import json

def max_value(value_name):
    with open("/Users/imac/Documents/covid/covid.json", "rt") as file:
        data = json.loads(file.read())
    
    max_country = None
    max_value = float('-inf')
    
    for country_data in data.values():
        country = country_data["location"]
        value = country_data.get(value_name)
        
        if value is not None and value > max_value:
            max_value = value
            max_country = country
    
    return max_country

value_name = 'median_age'
print(max_value(value_name))