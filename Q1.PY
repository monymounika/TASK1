num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
output=num1+num2+num3+num4+num5
if((num1<=0) or (num2<=0) or (num3<=0) or (num4<=0) or (num5<=0)):
    print("please enter only positive numbers")
else:
    print(output)


f=open("./python/TASK_1/output1.txt", "a")
f.write(str(output))
f.close()
