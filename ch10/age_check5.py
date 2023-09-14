print('-- Age checker V0.5 --')
print('enter age or "stop" to quit')

while True:
    reply = input('enter age >')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('enter a number or "stop"')
    else:
        age = int(reply)
        if age < 20:
            print('you are young!')
        else:
            print(f'you are {age ** 2} years old!')

print('goodbye!')
