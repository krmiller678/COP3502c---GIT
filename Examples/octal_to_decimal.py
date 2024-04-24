def octal_string_decode(oct):
    if oct[0] == '0':
        oct = oct[1:]
    new_num = 0
    power = 0
    for i in range(len(oct)-1, -1, -1):
        new_num += int(oct[i])*8**power
        power += 1
    return new_num



def main():
    octal = input()
    thingy_to_print = octal_string_decode(octal)
    print(thingy_to_print)

if __name__ == '__main__':
    main()