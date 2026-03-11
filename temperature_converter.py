def celsius_to_fahrenheit(c):
    f=(c*(9/5)) +32
    return f
def fahrenheit_to_celsius(f) :
    c= (f-32)*(5/9)
    return c 

def kelvin_to_celsius(k) :
    c= k-273.15
    return c 
def convert_all(temps, from_unit,to_unit):
    if from_unit=="celsius":
        return list(map(lambda x: celsius_to_fahrenheit(x) ,temps))
    elif from_unit=="fahrenheit":
        return (list(map(lambda x: fahrenheit_to_celsius(x),temps)))
    else:
        return (list(map(lambda x:kelvin_to_celsius(x),temps)))
    

temps = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(convert_all(temps,"celsius","fahrenheit"))
print(convert_all(temps,"fahrenheit","celsius"))
print(convert_all(temps,"kelvin","celsius"))