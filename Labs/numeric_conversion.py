'''Lab 4 - Numeric Conversion'''
#This program is designed to use functions, loops, characters and arithmetic
#to take in binary and hexadecimal into decimal notation. Additionally, the program
#will enable the user to go straight to hexadecimal from binary

#To start, we will define functions for the program. String indexing will be used for the conversion.

#Define function print_menu
def print_menu():
    #print menu options
    print('Decoding Menu\n'
          '-------------\n'
          '1. Decode hexadecimal\n'
          '2. Decode binary\n'
          '3. Convert binary to hexadecimal\n'
          '4. Quit\n')
    
    #gather user input --- moving this out of function to avoid scope issues
    #menu_selection = input('Please enter an option: ')
    #numeric_string = input('Please enter the numeric string to convert: ')

#Define function hex_char_decode (called by hex_string_decode below)
def hex_char_decode(digit):
    upper = digit.upper()
    #note to self - unnecessary to call this for ints but put in because zybooks
    if ord(upper) in range(ord('0'),ord(':')):
        value = int(upper)
    else:
        value = ord(upper) - ord('A') + 10
    return value
    

#Define function hex_string_decode
def hex_string_decode(hex):
    #Adjust for prefix
    if hex[0:2].upper() == '0B' or hex[0:2].upper() == '0X':
        hex = hex[2:]
    sum = 0
    power = 0
    #for loop to work the string from end to start increasing power each time
    for i in range(len(hex)-1,-1,-1):
        if ord(hex[i]) in range(ord('0'),ord(':')):
            sum += int(hex[i]) * 16 ** power
        else:
            integer = hex_char_decode(hex[i])
            sum += integer * 16 ** power
        power += 1
    return sum

            

#Define function binary_string_decode
def binary_string_decode(binary):
    #Adjust for prefix
    if binary[0:2].upper() == '0B' or binary[0:2].upper() == '0X':
        binary = binary[2:]
    sum = 0
    power = 0
    #for loop to work the string from end to start increasing power each time
    for i in range(len(binary)-1,-1,-1):
        sum += int(binary[i]) * 2 ** power
        power += 1
    return sum

#Define function binary_to_hex
def binary_to_hex(binary):
    #Adjust for prefix
    if binary[0:2].upper() == '0B' or binary[0:2].upper() == '0X':
        binary = binary[2:]
    sum = 0
    power = 0
    #for loop to convert binary to decimal
    for i in range(len(binary)-1,-1,-1):
        sum += int(binary[i]) * 2 ** power
        power += 1

    #while loop to continue dividing by 16 to append string return
    hex_string = ''
    dividend = sum
    while dividend > 0:
        remainder = dividend % 16

        #if statement for alpha vs numeric
        if remainder < 10:
            hex_string = str(remainder) + hex_string
        else:
            hex_string = chr(remainder + ord('A') - 10) + hex_string

        dividend = dividend // 16
    #just in case you put in 0s
    if sum == 0:
        hex_string = '0'
    return hex_string
        




#main function build out
if __name__ == '__main__':
    while True:
        print_menu()

        #Gather user input
        menu_selection = input('Please enter an option: ')

        #Add continue statement for bad input
        if menu_selection not in ['1', '2', '3', '4']:
            print('BOOOO')
            continue
        
        #Early QUIT condition before receiving string
        if menu_selection == '4':
            print('Goodbye!')
            break

        numeric_string = input('Please enter the numeric string to convert: ')

        #if statements to determine which function to apply

        if menu_selection == '1':
            #hex_string_decode
            result = hex_string_decode(numeric_string)
            print(f'Result: {result}')
            print()
        elif menu_selection == '2':
            #binary_string_decode
            result = binary_string_decode(numeric_string)
            print(f'Result: {result}')
            print()
        else:
            #binary_to_hex - must be menu option 3
            result = binary_to_hex(numeric_string)
            print(f'Result: {result}')
            print()