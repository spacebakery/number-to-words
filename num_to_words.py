import math 
# Words for digits and place values
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
thousands = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]

def convert_hundreds(n):
    if n == 0:
        return ""
    elif n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ("-" + ones[n % 10] if n % 10 != 0 else "")
    else:
        return ones[n // 100] + " hundred" + (" " + convert_hundreds(n % 100) if n % 100 != 0 else "")

def convert_number_to_words(n):
    if n == 0:
        return "zero"
    
    num_str = str(n)
    chunks = [int(num_str[max(i - 3, 0):i]) for i in range(len(num_str), 0, -3)]
    
    words = []
    for i, chunk in enumerate(chunks):
        if chunk > 0:
            words.append(convert_hundreds(chunk) + (" " + thousands[i] if thousands[i] else ""))
    
    return ' '.join(reversed(words)).strip()

def convert_currency_to_words(currency_value):
    # Clean input and ensure it's treated as a string
    currency_value = str(currency_value).replace(",", "").strip()
    
    try:
        number = float(currency_value)
    except ValueError:
        return "Invalid input."

    # Round the number to two decimal places
    number = round(number + 1e-8, 2)  # slight correction for floating point errors

    # Split into whole and decimal parts
    whole_part = int(math.floor(number))
    decimal_part = int(round((number - whole_part) * 100))

    # Convert whole part and decimal part
    whole_part_in_words = convert_number_to_words(whole_part)
    
    if decimal_part > 0:
        decimal_part_in_words = convert_number_to_words(decimal_part) + " cent" + ("s" if decimal_part > 1 else "")
        return f"{whole_part_in_words} dollars and {decimal_part_in_words}"
    
    return f"{whole_part_in_words} dollars"

# Example usage
currency_value = input("Enter a currency value: ")
result = convert_currency_to_words(currency_value)
print(result)
