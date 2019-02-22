def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1/num2

def modulo(num1,num2):
    return num1%num2


ch = input('Enter 1 add/2 subtract/3 mul/4 div/5 mod :')

num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))

if ch == '1':
    print(num1 ,'+' ,num2,'=' ,add(num1,num2))
elif ch=='2':
    print(num1 ,'-' ,num2 ,'=' ,subtract(num1,num2))
elif ch=='3':
    print(num1 ,'*' ,num2 ,'=' ,multiply(num1,num2))
elif ch=='4':
    print(num1 ,'/' ,num2 ,'=' ,divide(num1,num2))
elif ch=='5':
    print(num1 ,'%' ,num2 ,'=' ,modulo(num1,num2))
