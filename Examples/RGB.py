red_part = int(input('Enter red: '))
green_part = int(input('Enter green: '))
blue_part = int(input('Enter blue: '))

min_value = red_part

if green_part < min_value:
    min_value = green_part

if blue_part < min_value:
    min_value = blue_part

print(red_part - min_value,
      green_part - min_value,
      blue_part - min_value)