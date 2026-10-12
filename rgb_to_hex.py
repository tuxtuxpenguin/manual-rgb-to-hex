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
    
    # Reject invalid RGB values to ensure valid colour values
    if not isinstance(r, int) or isinstance(r, bool) or (r < 0) or (r > 255):
        raise ValueError("Red must be an integer between 0 and 255")
    if not isinstance(g, int) or isinstance(g, bool) or (g < 0) or (g > 255):
        raise ValueError("Green must be an integer between 0 and 255")
    if not isinstance(b, int) or isinstance(b, bool) or (b < 0) or (b > 255):
        raise ValueError("Blue must be an integer between 0 and 255")
        
    # Convert red RGB value into two hexadecimal digits

    # Calculate the first hexadecimal digit with integer division
    r_digit_one = r // 16

    # Calculate the second hexadecimal digit using the remainder
    r_digit_two = r % 16

    # Convert numerals from 10-15 into letters using the hex_lookup dictionary
    r_digit_one = hex_lookup.get(str(r_digit_one), r_digit_one)
    r_digit_two = hex_lookup.get(str(r_digit_two), r_digit_two)
    
    # Convert green RGB value into two hexadecimal digits
    
    # Calculate the first hexadecimal digit with integer division
    g_digit_one = g // 16

    # Calculate the second hexadecimal digit using the remainder
    g_digit_two = g % 16

    # Convert numerals from 10-15 into letters using the hex_lookup dictionary
    g_digit_one = hex_lookup.get(str(g_digit_one), g_digit_one)
    g_digit_two = hex_lookup.get(str(g_digit_two), g_digit_two)

    # Convert blue RGB value into two hexadecimal digits
    
    # Calculate the first hexadecimal digit with integer division
    b_digit_one = b // 16

    # Calculate the second hexadecimal digit using the remainder
    b_digit_two = b % 16

    # Convert numerals from 10-15 into letters using the hex_lookup dictionary
    b_digit_one = hex_lookup.get(str(b_digit_one), b_digit_one)
    b_digit_two = hex_lookup.get(str(b_digit_two), b_digit_two)

    # Combine all hexadecimal digits into a hex code
    return('#' + str(r_digit_one) + str(r_digit_two) + str(g_digit_one) + str(g_digit_two) + str(b_digit_one) + str(b_digit_two))

# Run the function and set returned output to a variable (optionable of course)
complete_hex_code = rgb_to_hex(r=119, g=119, b=199)

# Print the variable
print(complete_hex_code)