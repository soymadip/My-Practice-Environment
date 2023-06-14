x = int(input('enter bro: '))

print('here is if-else result:')
if (x==0):
    print('x is zero')
elif(x==4):
    print('case is 4')
elif(x!=90):
    print(x,'is not 90')
elif(x!=80):
    print(x,'is not 80')
else:
    print(x)



print('here is match case result:')
match x:
    case 0:
        print('x is zero')
    case 4:
        print('case is 4')
    case _ if x !=90:
        print(x,'is not 90')
    case _ if x !=80:
        print(x,'is not 80')
    case _:
        print(x)