import json, math

def calc_mean_sigma(data):
    
    sx, sx2, n = 0.0, 0.0, 0
    
    for x in data:
        
        sx += x
        sx2 += x*x
        n += 1
        
    return sx / n, math.sqrt(max(sx2 / n - sx / n * sx / n, 0))


def sigma_norm(country_code, value_name):
    
    data = json.loads(open("/Users/imac/Documents/covid/covid.json", "rt").read())
    country_data = data[country_code]
    values = []
    
    for entry in country_data["data"]:
        
        if "date" not in entry:
            
            continue
        
        date = entry["date"]
        
        if date[:7] != "2020-08":
            
            continue
        
        values.append(entry.get(value_name, 0))
        
    m, s = calc_mean_sigma(values)
    
    return s / m

print(sigma_norm('RUS', 'new_cases'))