print('-- Age Checker V0.2 --')
print('Enter age or "stop" to quit')

while True:
    age = input('Enter age >')
    if age == 'stop': 
        break
    elif not age.isdigit():
        print('enter a number or "stop"')
    else:
        print(f'You are {int(age) ** 2} years old!')

print('goodbye!')
