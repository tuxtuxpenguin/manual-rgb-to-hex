# Map decimal values 10-15 to their hexadecimal letters
hex_lookup = {
    "10": "A",
    "11": "B",
    "12": "C", 
    "13": "D",
    "14": "E",
    "15": "F"
}

def rgb_to_hex(r, g, b):
    
    # Reject invalid RGB values
    if not isinstance(r, int) or isinstance(r, bool) or (r < 0) or (r > 255):
        raise ValueError("Red must be an integer between 0 and 255")
    if not isinstance(g, int) or isinstance(g, bool) or (g < 0) or (g > 255):
        raise ValueError("Green must be an integer between 0 and 255")
    if not isinstance(b, int) or isinstance(b, bool) or (b < 0) or (b > 255):
        raise ValueError("Blue must be an integer between 0 and 255")
        
    # Red part of RGB
    # Divide by 16 to find first hexadecimal digit
    r_division_str = str(r / 16)
    r_parts = r_division_str.split(".")

    # Check if whole number maps to hex letter and if it doesnt keep it as a number
    r_digit_one = hex_lookup.get(r_parts[0])
    if r_digit_one is None:
        r_digit_one = int(r_parts[0])

    # Recovering the fractional part and multiplying it by 16 to get the second digit and find the hexadecimal digit
    r_decimal = (int(r_parts[1]) / (10 ** len(str(r_parts[1])))) * 16
    r_digit_two = hex_lookup.get(str(int(r_decimal)))
    if r_digit_two is None:
        r_digit_two = int(r_decimal)

    # Green part of RGB
    # Divide by 16 to find first hexadecimal digit
    g_division_str = str(g / 16)
    g_parts = g_division_str.split(".")

    # Check if whole number maps to hex letter and if it doesnt keep it as a number
    g_digit_one = hex_lookup.get(g_parts[0])
    if g_digit_one is None:
        g_digit_one = int(g_parts[0])

    # Recovering the fractional part and multiplying it by 16 to get the second digit and find the hexadecimal digit
    g_decimal = (int(g_parts[1]) / (10 ** len(str(g_parts[1])))) * 16
    g_digit_two = hex_lookup.get(str(int(g_decimal)))
    if g_digit_two is None:
        g_digit_two = int(g_decimal)
    
    # Blue part of RGB
    # Divide by 16 to find first hexadecimal digit
    b_division_str = str(b / 16)
    b_parts = b_division_str.split(".")

    # Check if whole number maps to hex letter and if it doesnt keep it as a number
    b_digit_one = hex_lookup.get(b_parts[0])
    if b_digit_one is None:
        b_digit_one = int(b_parts[0])

    # Recovering the fractional part and multiplying it by 16 to get the second digit and find the hexadecimal digit
    b_decimal = (int(b_parts[1]) / (10 ** len(str(b_parts[1])))) * 16
    b_digit_two = hex_lookup.get(str(int(b_decimal)))
    if b_digit_two is None:
        b_digit_two = int(b_decimal)

    # Combine it all to make a complete hex colour code and return it
    return('#' + str(r_digit_one) + str(r_digit_two) + str(g_digit_one) + str(g_digit_two) + str(b_digit_one) + str(b_digit_two))

# Run the function and set returned output to a variable (optionable of course)
complete_hex_code = rgb_to_hex(r=119, g=119, b=199)

# Print the variable
print(complete_hex_code)