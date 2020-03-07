import math
selection = int(input("1. Hexadecimal to Denary | 2. Denary to Hexadecimal \n"))
def HEX(num):
    one = math.floor(num / 16)
    mod = num % 16
    if (mod == 10):
       mod = "A"
    if (mod == 11):
        mod = "B"
    if (mod == 12):
        mod = "C"
    if (mod == 13):
        mod = "D"
    if (mod == 14):
        mod = "E"
    if (mod == 15):
        mod = "F"
    return("0x"+str(one) + str(mod))
def split(num):
    return [ch for ch in str(num)]
def DENARY(num):
    a = split(num)
    num = int(a[0]) * 16
    two= a[1]
    if (two == "A" or two == "a"):
     two = 10
    elif (two == "B" or two == "b"):
     two = 11
    elif (two == "C" or two == "c"):
     two = 12
    elif (two == "D" or two == "d"):
     two = 13
    elif (two == "E" or two == "e"):
     two = 14
    elif (two == "F" or two == "f"):
     two = 15
    else:
     two = int(a[1]) * int(a[1])
    final = num + int(two)
    return(final)
if (selection == 2):
    print("-----DENARY TO HEX-----", "\n")
    num = int(input("Enter Denary Number: "))
    print("answer: ",HEX(num))
elif (selection == 1):
    print("-----HEX TO DENARY-----","\n")
    num = input("Enter Hex Number: ")
    print("answer: ",DENARY(num))
