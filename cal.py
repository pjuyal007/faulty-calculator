#faulty calculator which performs all calculations correctly and shows incorrect for only the few numbers which i have used in conditions  
print("enter the operator (+,-,*,/):")
op = input()
print("enter the numbers you want to perform operation on:")
num1 = int(input())
num2 = int(input())

if op=='*':
    if num1==45 and num2 ==3:
     print("555")
    else:
        print(num1*num2)
elif op=='+':              #use elif instead of if beacuse then it will run all the statements
    if num1==56 and num2==9:
     print("77")
    else:
        print(num1+num2)
elif op=='/':
    if num1==56 and num2==6:
     print("4")
    else:
        print(num1/num2)
elif op=='-':
    print(num1-num2)
else:
    print("invalid operator")