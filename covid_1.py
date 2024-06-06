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