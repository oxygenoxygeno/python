a,b,c = map(float, input().split())
print(a,'+',b,'+',c,'=',a+b+c)
print(a,'*',b,'*',c,'=',a*b*c)
z = (a+b+c)/3
z = round(z,3)
print('(',a,'+',b,'+',c,')/3=',z)