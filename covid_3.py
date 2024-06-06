import json, math

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
    
    if abs(dd) < 1e-5:
        
        return None
    
    return (sxy / n - sx / n * sy / n) / dd

def float_with_precision(code):
    
    data = json.loads(open("/Users/imac/Documents/covid/covid.json", "rt").read())
    country_data = data[code]
    new_cases, new_tests = [], []
    
    for entry in country_data["data"]:
        
        if "date" not in entry:
            
            continue
        
        date = entry["date"]
        
        if date[:7] != "2020-08":
            
            continue
        
        new_cases.append(entry.get("new_cases", 0))
        new_tests.append(entry.get("new_tests", 0))
        
    return corr(new_cases, new_tests)

print(float_with_precision("IND"))