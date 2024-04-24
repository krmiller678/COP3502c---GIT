a, b = input().split()
a, b = int(a), int(b) #a=500, b=10000

#Range 1-10 will only give 1, 2, 3 ... 9
for i in range(a, b+1):
    #i = 500, 501, 502 ... 10000
    #look at specific number 678

    #1. how many digits: n
    #len(str(i)) can convert to string and give you number of digits that way
    num_digits = 0
    temp = i
    while temp > 0:
        last_digit = temp % 10
        num_digits += 1
        temp //= 10

    #2. look at each digit, raise digit to n and sum
    total = 0
    temp = i
    while temp > 0:
        last_digit = temp % 10
        total += last_digit ** num_digits #8^3 + 7^3 + 6^3
        temp //= 10
    
    if total == i:
        print(total)