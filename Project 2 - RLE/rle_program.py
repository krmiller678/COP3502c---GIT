""" Project 2 - RLE with Images Python
The purpose of this project is to encode and decode data for images
utilizing run length encoding. Encoding and decoding of raw data,
conversion between data and strings, and display of information by
creating procedures that can be called from within the programs and externally
"""

# Import the Console Gfx Class
from console_gfx import ConsoleGfx


# Set up print menu function
def print_menu():
    """
    This function prints the menu options to collect user input
    :return:
    """
    print('RLE Menu\n'
          '--------\n'
          '0. Exit\n'
          '1. Load File\n'
          '2. Load Test Image\n'
          '3. Read RLE String\n'
          '4. Read RLE Hex String\n'
          '5. Read Data Hex String\n'
          '6. Display Image\n'
          '7. Display RLE String\n'
          '8. Display Hex RLE Data\n'
          '9. Display Hex Flat Data\n')


def to_hex_string(data):
    """
    Takes in RLE or raw data and returns a hex string representing data
    :param data:
    :return: hex_string
    """
    hex_string = ""
    for value in data:
        if 0 <= value < 10:
            hex_string += str(value)
        elif 10 <= value < 16:
            hex_string += chr(87+value)
        else:
            print("Invalid")
            return 0

    return hex_string


def count_runs(flat_data):
    """
    Returns number of runs of data in data set, double this for length of encoded (RLE) list
    :param flat_data:
    :return: runs (integer)
    """
    runs = 1
    for index, value in enumerate(flat_data):
        if index > 0:
            if value != flat_data[index-1]:
                runs += 1
            # conditional for start of new row
            elif index % 16 == 0:
                runs += 1
    return runs


def encode_rle(flat_data):
    """
    Returns encoding in RLE of raw data, generate RLE list
    :param flat_data:
    :return: rle_list
    """
    current = flat_data[0]
    count = 1
    rle_list = []
    for item in flat_data[1:]:
        if count == 15:
            rle_list.append(count)
            rle_list.append(current)
            current = item
            count = 1
        elif item == current:
            count += 1
        else:
            rle_list.append(count)
            rle_list.append(current)
            current = item
            count = 1

    # add on whatever is left at end of list
    rle_list.append(count)
    rle_list.append(current)

    return rle_list


def get_decoded_length(rle_data):
    """
    Returns decompressed size of RLE data
    :param rle_data:
    :return: size (integer)
    """
    size = 0
    for index, value in enumerate(rle_data):
        if index % 2 == 0:
            size += value
    return size


def decode_rle(rle_data):
    """
    Returns decoded data set from RLE encoded data
    :param rle_data:
    :return: raw_data_list
    """
    raw_data_list = []
    for index, value in enumerate(rle_data):
        if index % 2 == 0:
            for i in range(value):
                raw_data_list.append(rle_data[index+1])
    return raw_data_list


def string_to_data(data_string):
    """
    Takes in hexadecimal format string and returns byte_data
    :param data_string:
    :return: byte_data (list)
    """
    byte_data = []
    for element in data_string:
        if element.isdigit():
            element = int(element)
            byte_data.append(element)
        else:
            decimal_num = ord(element.upper()) - 55
            byte_data.append(decimal_num)

    return byte_data


def to_rle_string(rle_data):
    """
    Translates RLE data into readable representation
    :param rle_data:
    :return: rle_string (run_length, hex_value, ':', next run)
    """
    rle_string = ""
    for index, element in enumerate(rle_data):
        if index > 0 and index % 2 == 0:
            rle_string += ':'
        if element < 10 or index % 2 == 0:
            rle_string += str(element)
        else:
            rle_string += chr(87+element)
    return rle_string


def string_to_rle(rle_string):
    """
    Opposite of to_rle_string -> Readable string to RLE byte date
    :param rle_string:
    :return: rle_byte_data (list)
    """
    rle_byte_data = []
    rle_temp = rle_string.split(':')
    for element in rle_temp:
        rle_byte_data.append(int(element[:-1]))
        if element[-1].isdigit():
            rle_byte_data.append(int(element[-1]))
        else:
            decimal_num = ord(element[-1].upper()) - 55
            rle_byte_data.append(decimal_num)

    return rle_byte_data



# Set up main function
def main():
    # Welcome message
    print('Welcome to the RLE image encoder!')
    print()

    # Print out display image and set data to None
    print('Displaying Spectrum Image:')
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    image_data = None
    print()
    print()

    while True:
        # print out RLE menu
        print_menu()

        # Prompt user for menu option
        menu_option = input('Select a Menu Option: ')

        #break and end program if '0' input
        if menu_option == '0':
            break

        # Verify valid menu input, if not valid continue to start of loop
        if menu_option not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Error! Invalid input.')
            print()
            continue
        else:
            menu_option = int(menu_option)

        # Conditional for menu_option = 1, Load File
        if menu_option == 1:
            filename = input('Enter name of file to load: ')
            image_data = ConsoleGfx.load_file(filename)
            print()
            continue

        # Conditional for menu_option = 2, Load Test Image
        if menu_option == 2:
            image_data = ConsoleGfx.test_image
            print('Test image data loaded.')
            print()
            continue

        # Conditional for menu_option = 3, Read RLE String
        if menu_option == 3:

            user_input = input("Enter an RLE string to be decoded: ")
            image_data = string_to_rle(user_input)
            image_data = decode_rle(image_data)
            continue

        # Conditional for menu_option = 4, Read RLE Hex String
        if menu_option == 4:

            user_input = input("Enter the hex string holding RLE data: ")
            image_data = string_to_data(user_input)
            image_data = decode_rle(image_data)
            continue

        # Conditional for menu_option = 5, Read Data Hex String
        if menu_option == 5:

            user_input = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(user_input)
            image_data = decode_rle(image_data)
            continue

        # Conditional for menu_option = 6, Display Image
        if menu_option == 6:
            print('Displaying image...')

            if image_data == None:
                print('(no data)\n')
                continue

            ConsoleGfx.display_image(image_data)
            print()
            continue

        # Conditional for menu_option = 7, Display RLE String
        if menu_option == 7:

            if image_data == None:
                print('RLE representation: (no data)\n')
                continue

            output = encode_rle(image_data)
            print(f"RLE representation: {to_rle_string(output)}\n")
            continue

        # Conditional for menu_option = 8, Display Hex RLE Data
        if menu_option == 8:

            if image_data == None:
                print('RLE hex values: (no data)\n')
                continue

            output = encode_rle(image_data)
            print(f"RLE hex values: {to_hex_string(output)}\n")
            continue

        # Conditional for menu_option = 9, Display Hex Flat Data
        if menu_option == 9:

            if image_data == None:
                print('Flat hex values: (no data)\n')
                continue

            print(f"Flat hex values: {to_hex_string(image_data)}\n")
            continue



if __name__ == '__main__':
    main()
