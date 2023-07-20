def convert_to_celsius(fahrenheit):
    result = 0

    if round((fahrenheit-32)/1.8, 2) == (fahrenheit-32)//1.8+1:
        result = round((fahrenheit-32)/1.8, 2)
    else:
        result = (fahrenheit-32)/1.8
    return result
