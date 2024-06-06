import json

def day_with_max_value(value_name):
    
    data = json.loads(open("/Users/imac/Documents/covid/covid.json", "rt").read())
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

print(day_with_max_value('new_cases'))