def is_weekend(day):
    return day in (6, 7)

def get_discount(amount):
    return round((amount >= 5000 and amount * 0.1) or (amount >= 1000 and amount * 0.05) or 0, 2)

def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    digits = {1: "однозначное", 2: "двузначное", 3: "трехзначное"}
    return f"{parity} {digits[len(str(n))]} число"

def convert_to_meters(unit_number, length_in_units):
    conversion = {
        1: 0.1,       # дециметр
        2: 1000,      # километр
        3: 1,         # метр
        4: 0.001,     # миллиметр
        5: 0.01       # сантиметр
    }
    return length_in_units * conversion[unit_number]

def describe_age(age):
    tens = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        10: "сто"
    }
    
    ones = {
        0: "",
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }
    
    years = {
        1: "год",
        2: "года",
        3: "года",
        4: "года",
        5: "лет",
        6: "лет",
        7: "лет",
        8: "лет",
        9: "лет",
        0: "лет"
    }
    
    if age == 100:
        return "сто лет"
        
    ten, one = divmod(age, 10)
    year_form = years[one] if one != 0 else "лет"
    one_str = f" {ones[one]}" if one != 0 else ""
    
    return f"{tens[ten]}{one_str} {year_form}"