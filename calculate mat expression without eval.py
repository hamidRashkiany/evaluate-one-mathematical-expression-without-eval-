def multiplication(num1,num2):
    return (num1*num2)

def subtraction(num1,num2):
    return (num1-num2)

def summation(num1,num2):
    return (num1+num2)

s=input("input your mathematical expresion:")
str_l=[]
int_numbers=[]
operators=[]
result=0
flag=True

for i in range(len(s)):
    str_l.append(s[i])

for i in range(1,len(s),2):
    operators.append(s[i])

int_numbers.append(int(s[0]))
for i in range (0,len(s)-2,2):#bring out only numbers and change them to int
    int_numbers.append(int(s[i+2]))

if str_l[0]=="*" or str_l[0]=="/" or str_l[0]=="+" or str_l[0]=="-":
    print("Syntax Error: the expresion should start with number.")
else:
    if operators[0]=="+":
        result=summation(int_numbers[0],int_numbers[1])
    elif operators[0]=="*":
        result=multiplication(int_numbers[0],int_numbers[1])
    else:
        result=subtraction(int_numbers[0],int_numbers[1])
    j=1
    for i in range(2,len(int_numbers)):
        if operators[j]=="+":
            result+=int_numbers[i]
        elif operators[j]=="*":
            result*=int_numbers[i]
        else:
            result-=int_numbers[i]
        j+=1
            
    print(result)
