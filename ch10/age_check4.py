print('-- Age Checker V0.4 --')
print('Enter age or "stop" to quit')

while True:
    age = input('Enter age >')
    if age == 'stop': break
    try:
        print(f'You are {float(age) ** 2} years old!')
    except:
        print('enter a number or "stop"')
        
print('goodbye!')
