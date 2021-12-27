x=int(input('mimdinare celi '))
a=int(input('dabadebis celi '))
if x<=a:
    print('sheiyvanet validuri celi')
    quit() 
y=int(input('mimdinare tve '))
b=int(input('dabadebis tve '))
if y>12 or b>12:
    print ('sheiyvane validuri tve')
    quit()
z=int(input('mimdinare ricxvi '))
c=int(input('dabadebis ricxvi '))
if z>31 or c>31:
    print ('sheiyvane validuri ricxvi')
    quit()
j=x-a
k=y-b
l=z-c
if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
    e=31
elif b==4 or b==6 or b==9 or b==11:
    e=30
else:
    e=28
if (x-2020)%4==0:
    e=29
if y>b and z>c:
    print ('tqven xart ', j, 'clis', k, 'tvis da', l, 'dgis')
elif y==b and z==c:
    print ('gilocavt!!! Tqven dges gaxdit ', j, 'clis')
elif y==b and z>c:
    print ('tqven xart ', j, 'clis da tqveni dabadebis dge iko', l,' dgis ukan')
elif y==b and z<c:
    print ('tqven xart ', j, 'clis da', l, ' dgeshi gaxdebit', j+1,' clis')
elif y>b and z==c:
    print ('tqven xart ', j, 'clis da tqveni dabadebis dge iyo, zustad', k,' tvis ukan')
elif y>b and z<c:#15-21
    print ('tqven xart ', j, 'clis da ', k, 'tvesa da', c-z,' dgeshi gaxdebit', j+1,' clis')
elif y<b and z<c:
    print ('tqven xart ', j-1, 'clis da ', b-y, 'tvesa da', c-z,' dgeshi gaxdebit', j,' clis')
elif y<b and z==c:
    print ('tqven xart ', j-1, 'clis da tqveni dabadebis dge iqneba, zustad', b-y,' tveshi da gaxdebit', j, 'clis')
elif y<b and z>c:
    print ('tqven xart ', j-1, 'clis da ', b-y, 'tvesa da', e-z+c, ' dgeshi gaxdebit', j,' clis')
    #this is my first program on python  