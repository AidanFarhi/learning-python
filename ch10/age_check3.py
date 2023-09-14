print('-- Age Checker V0.3 --')
print('Enter age or "stop" to quit')

while True:
    age = input('Enter age >')
    if age == 'stop': break
    try:
        age = int(age)
    except:
        print('enter a number or "stop"')
    else:
        print(f'You are {age ** 2} years old!')
        
print('goodbye!')
