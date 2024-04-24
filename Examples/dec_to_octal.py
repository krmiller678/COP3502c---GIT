def dec_to_octal(decimal):
    decimal = int(decimal)
    if decimal == 0:
        return '0'
    
    octal_string = ''
    while decimal != 0:
        remainder = decimal % 8
        octal_string = str(remainder) + octal_string
        decimal = decimal // 8
    return octal_string

def main():
    user_input = input()
    print(dec_to_octal(user_input))

if __name__ == '__main__':
    main()
