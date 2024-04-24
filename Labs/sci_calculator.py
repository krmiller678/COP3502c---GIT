'''Lab 3: Scientific Calculator'''

import math
program_run = True
current_result = 0.0
list_of_calculations = []
calculations = 0
menu_select = 0

while program_run == True:
    #Display menu
    if menu_select != 7 and menu_select in range(0,8):
        print(f'Current Result: {current_result}\n\n'
        'Calculator Menu\n'
        '---------------\n'
        '0. Exit Program\n'
        '1. Addition\n'
        '2. Subtraction\n'
        '3. Multiplication\n'
        '4. Division\n'
        '5. Exponentiation\n'
        '6. Logarithm\n'
        '7. Display Average\n')

    #Request user input
    menu_select = input('Enter Menu Selection: ')

    if int(menu_select) in range(0,8):
        menu_select = int(menu_select)
    else:
        print()
        print('Error: Invalid selection!')
        print()
        continue

    #set breakpoint if EXIT 0 command is entered
    if menu_select == 0:
        program_run = False
        print()
        print('Thanks for using this calculator. Goodbye!')
        break

    #If option 1-6, request the operands, add in conditional for RESULT
    if menu_select in range(1,7):
        op1 = input('Enter first operand: ')
        if op1 == 'RESULT':
            op1 = current_result
        else:
            op1 = float(op1)
        op2 = input('Enter second operand: ')
        if op2 == 'RESULT':
            op2 = current_result
        else:
            op2 = float(op2)

    #For options 1-6, calculate current result
    if menu_select == 1:
        current_result = op1 + op2
        print()
    elif menu_select == 2:
        current_result = op1 - op2
        print()
    elif menu_select == 3:
        current_result = op1 * op2
        print()
    elif menu_select == 4:
        current_result = op1 / op2
        print()
    elif menu_select == 5:
        current_result = op1 ** op2
        print()
    elif menu_select == 6:
        current_result = math.log(op2,op1)
        print()
    #Display the Average
    elif menu_select == 7:
        if len(list_of_calculations) != 0:
            sum = 0
            for i in list_of_calculations:
                sum += i
            print(f'Sum of calculations: {sum}\n'
                  f'Number of calculations: {calculations}\n'
                  f'Average of calculations: {round(sum/calculations,2)}\n')
            print()
            continue
        else:
            print('Error: No calculations yet to average!')
            print()
            continue

    #Add to number of calculations and concatenate list of calculations        
    calculations += 1
    list_of_calculations.append(current_result)
        