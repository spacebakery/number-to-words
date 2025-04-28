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
    
    # Split into whole and decimal parts
    if '.' in currency_value:
        whole_part, decimal_part = currency_value.split('.')
    else:
        whole_part, decimal_part = currency_value, "00"
    
    # Fix decimal part to always be two digits
    decimal_part = (decimal_part + "00")[:2]
    
    # Format whole part with commas
    formatted_whole_part = f"{int(whole_part):,}"
    
    # Convert the whole and decimal parts
    whole_part_in_words = convert_number_to_words(int(whole_part))
    
    if int(decimal_part) > 0:
        decimal_part_in_words = convert_number_to_words(int(decimal_part)) + " cent" + ("s" if int(decimal_part) > 1 else "")
        return f"{whole_part_in_words} dollars and {decimal_part_in_words}"
    
    return f"{whole_part_in_words} dollars"

# Example usage
currency_value = input("Enter a currency value: ")
result = convert_currency_to_words(currency_value)
print(result)
