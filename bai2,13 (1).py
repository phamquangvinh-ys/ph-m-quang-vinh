a=int(input('Nhap a:'))
b=int(input('Nhap b:'))
c=int(input('Nhap c:'))
import math
deltha = b ** 2 - 4 * a * c
if deltha < 0:
    print(" Phuong trinh vo nghiem ")
elif deltha == 0:
    x = -b / (2 * a)
    print('Phuong trinh có nghiệm kép x1=x2=',x)
else:
    print('Phuong trình có 2 nghiệm phân biệt:')
    x1 = (-b - (math.sqrt(deltha))) / (2 * a)
    print(" Nghiem x1=",x1)
    x2 = (-b + (math.sqrt(deltha))) / (2 * a)
    print(" Nghiem x2=",x2)

