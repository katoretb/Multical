import math
while True:
    print('\x1b[1;31;40m' + '1.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Find longest side' + '\x1b[0m')
    print('\x1b[1;31;40m' + '2.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Find another side' + '\x1b[0m')
    print('\x1b[1;31;40m' + '3.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Find root' + '\x1b[0m')
    print('\x1b[1;31;40m' + '4.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Area finder' + '\x1b[0m')
    g = input('\x1b[1;31;40m' + '4.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Please choose' + '\x1b[0m' + '>')
    if g > 4:
        continue
    elif g == 1:
        a = input('\x1b[1;32;40m' + 'insert some side' + '\x1b[0m' + '>')
        b = input('\x1b[1;32;40m' + 'insert another side' + '\x1b[0m' + '>')
        x = a*a
        y = b*b
        z = x+y
        f = math.sqrt(z)
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        print(f)
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        continue
    elif g == 2:
        x = input('\x1b[1;32;40m' + 'insert longest side' + '\x1b[0m' + '>')
        y = input('\x1b[1;32;40m' + 'insert another side' + '\x1b[0m' + '>')
        a = x*x
        b = y*y
        c = a-b
        z = math.sqrt(c)
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        print(z)
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        continue
    elif g == 3:
        x = input('\x1b[1;32;40m' + 'insert Number' + '\x1b[0m' + '>')
        y = math.sqrt(x)
        print(y)
        continue
    elif g == 4:
        print('\x1b[1;31;40m' + '1.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Triangle' + '\x1b[0m')
        print('\x1b[1;31;40m' + '2.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Square' + '\x1b[0m')
        print('\x1b[1;31;40m' + '3.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Trapezoid' + '\x1b[0m')
        print('\x1b[1;31;40m' + '4.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Circle' + '\x1b[0m')
        h = input()
        if h > 4:
            continue
        elif h == 1:
            x = input('\x1b[1;32;40m' + 'insert base' + '\x1b[0m' + '>')
            y = input('\x1b[1;32;40m' + 'insert high' + '\x1b[0m' + '>')
            z = x*y/2
            print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
            print(z)
            print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
            continue
        elif h == 2:
            x = input('\x1b[1;32;40m' + 'insert Frist side' + '\x1b[0m' + '>')
            y = input('\x1b[1;32;40m' + 'insert Second side' + '\x1b[0m' + '>')
            z = x*y
            print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
            print(z)
            print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
            continue
        elif h == 3:
            x = input('\x1b[1;32;40m' + 'insert Frist Parallel side' + '\x1b[0m' + '>')
            y = input('\x1b[1;32;40m' + 'insert Second Parallel side' + '\x1b[0m' + '>')
            z = input('\x1b[1;32;40m' + 'insert High' + '\x1b[0m' + '>')
            a = x+y
            b = a*z
            c = b/2
            print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
            print(c)
            print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
            continue
        elif h == 4:
            x = input('\x1b[1;32;40m' + 'insert R' + '\x1b[0m' + '>')
            y = x*x
            z = 3.14*y
            print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
            print(z)
            print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
            continue