def getinput1():
    num1 = int(input("Please enter the range Up to get feb : "))
    if num1 <= 0:
        print("Enter valid input other than Zero and Positive Number ")
        num1 = getinput1()
    return num1
def getans():
    try:
        num01 = getinput1()
    except ValueError:
        print("Please enter integer value only")
        getans()
    else:
        print("OutPut is :",end=" ")
        a, b = 0, 1
        while True:
            print(a, end=" ")
            a, b = b, a
            b += a
            if a > num01 + 1:
                break

getans()
input()
