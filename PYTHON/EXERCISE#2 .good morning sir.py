import time

time1 = int(time.strftime('%H'))
nowtime = time.strftime('%H:%M:%S')

def greeting():
    print('this is',nowtime)
    if(time1>=5 and time1<12):
        print("Good Moening Sir")
    elif(time1>= 12 and time1<17):
        print('Good afternoon sir')
    elif(time1>=17 and time1<19):
        print('Good evening sir')
    elif(time1>=19 and time1<23):
            print('Good night Sir')