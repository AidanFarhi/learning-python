print('-- Age Checker V0.1 --')
print('Enter age or "stop" to quit')

while True:
    age = input('Enter age >')
    if age == 'stop': break
    print(f'You are {int(age) ** 2} years old!')

print('goodbye!')
