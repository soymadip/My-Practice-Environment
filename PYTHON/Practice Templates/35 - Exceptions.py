
# Make a programme for calculating number table with custom error handeling:



a = int(input('enter your number:'))

try:
    for i in range(0,11):
        print(f'{a}*{i} is: {a*i}')

except Exception as e:
    print(e)