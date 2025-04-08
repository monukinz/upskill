n = 73
if n % 2 == 0:
    print('even')
if n % 3 == 0:
    print('divisible by 3')

if n % 3 != 0 and n % 2 != 0:
    print('not odd, not divisible by 3')


commands = 1, 2, 3, 4
command = 1

match command:
    case 1:
        pass
    case 2:
        pass
    case _:
        print('Another value')

if command == 1:
    pass
elif command == 2:
    pass
else:
    print('Another value')
