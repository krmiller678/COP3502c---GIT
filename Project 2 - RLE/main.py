def consecutive_fours(arr):
    current = arr[0]
    count = 1
    for item in arr[1:]:
        if current == item:
            count += 1
        else: # item =2, current = 3
            current = item
            count = 1
            # append count for encode RLE when item != current and current into res
        if count >= 4: # special case, there are no more than 15 elements in a group
            return True

    return False


def sum_by_parity(arr):
    """
    :param arr:
    :return: list with sum of even, sum of odd integers
    """
    sum_even, sum_odd = 0, 0
    for index, item in enumerate(arr):
        if index % 2 == 0:
            sum_even += item
        else:
            sum_odd += item

    return [sum_even, sum_odd]


def expand_by_index(arr):
    res = []
    for index, item in enumerate(arr):
        for i in range(item):
            res.append(index)

    return res


def numerical_count(string):
    count = 0
    for item in string:
        if item.isdigit():
            count += 1
    return count



if __name__ == '__main__':
    #Project 2A inside
    # Import the Console Gfx Class
    from console_gfx import ConsoleGfx


    # Set up print menu function
    def print_menu():
        print('RLE Menu\n'
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


    # Set up main function
    def main():
        # Welcome message
        print('Welcome to the RLE image encoder!')
        print()

        # Print out display image and set data to None
        ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
        image_data = None
        print()
        print()

        while True:
            # print out RLE menu
            print_menu()

            # Prompt user for menu option
            menu_option = input('Select a Menu Option: ')

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

            # Conditional for menu_option = 6, Display Image
            if menu_option == 6:
                print('Displaying image...')

                if image_data == None:
                    print('(no data)')
                    continue

                ConsoleGfx.display_image(image_data)
                print()
                continue