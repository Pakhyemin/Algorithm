c = int(input("과목 갯수를 입력하시오: "))
a = list(map(int,input().split(",")))
b = max(a)

for i in range(c):
    a[i] = a[i]/b*100
    r=sum(a)/len(a)
print("%.2f"%r)