area_code, prefix_num, line_num = input().split()

area_code = int(area_code)
prefix_num = int(prefix_num)
line_num = int(line_num)

print("Country  Phone Number")
print("-------  ------------")
print(f"U.S.     +1 ({area_code}){prefix_num}-{line_num}" )
print(f"Brazil   +55 ({area_code}){prefix_num+100}-{line_num}" )
print(f"Croatia  +385 ({area_code}){prefix_num}-{line_num+50}" )
print(f"Egypt    +20 ({area_code+30}){prefix_num}-{line_num}" )
print(f"France   +33 ({prefix_num}){area_code}-{line_num}" )