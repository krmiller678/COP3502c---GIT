'''Four Function Calculator'''

#Gather operand information from user
op1 = float(input('Enter first operand: '))
op2 = float(input('Enter second operand: '))
print()

#Display menu
print('Calculator Menu\n'
'---------------\n'
'1. Addition\n'
'2. Subtraction\n'
'3. Multiplication\n'
'4. Division\n')

#Get user input on what operation to perform
op_selection = int(input('Which operation do you want to perform? '))
print()

#if statement branches to perform operations
if op_selection == 1:
    print(f'The result of the operation is {op1+op2}. Goodbye!')
elif op_selection == 2:
    print(f'The result of the operation is {op1-op2}. Goodbye!')
elif op_selection == 3:
    print(f'The result of the operation is {op1*op2}. Goodbye!')
elif op_selection == 4:
    print(f'The result of the operation is {op1/op2}. Goodbye!')
else:
    print("Error: Invalid selection! Terminating program.")