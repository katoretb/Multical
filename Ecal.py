while True:
    print("please select");
    print('\x1b[1;31;40m' + '1.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Ohm Includer' + '\x1b[0m')
    print('\x1b[1;31;40m' + '2.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Ohm finder' + '\x1b[0m')
    print('\x1b[1;31;40m' + '3.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Amp finder' + '\x1b[0m')
    print('\x1b[1;31;40m' + '4.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Voltage finder' + '\x1b[0m')
    print('\x1b[1;31;40m' + '5.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Watt finder' + '\x1b[0m')
    print('\x1b[1;31;40m' + '6.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Resister color reader' + '\x1b[0m')
    g = input()
    if g == 1:
        print('\x1b[1;32;40m' + 'You has select Ohm Includer' + '\x1b[0m')
        print("insert Parallel Circuit resistor 1")
        x = input()
        print("insert Parallel Circuit resistor 2")
        y = input()
        print("insert Series Circuit resistor")
        print('\x1b[1;31;40m' + 'If have Series Circuit resistor more than 1 you should do like this' + '\x1b[0m')
        print('\x1b[1;32;40m' + '4+5+7' + '\x1b[0m')
        z = input()
        a = x*y
        b = x+y
        c = a/b
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        print(c+z)
        print("Ohm")
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
    elif g == 2:
        print("please insert Amp")
        x = input()
        print("please insert Voltage")
        y = input()
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        print(x*y)
        print("Ohm")
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
    elif g == 3:
        print("please insert Voltage")
        x = input()
        print("please insert Ohm")
        y = input()
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        print(x/y)
        print("Amp")
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
    elif g == 4:
        print("please insert Amp")
        x = input()
        print("please insert Ohm")
        y = input()
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        print(x*y)
        print("Voltage")
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
    elif g == 5:
        print("please insert Voltage")
        x = input()
        print("please insert Amp")
        y = input()
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        print(x*y)
        print("Watt")
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
    elif g == 6:
        print('\x1b[1;31;40m' + '0.' + '\x1b[0m' + '\x1b[5;30;47m' + 'Black' + '\x1b[0m')
        print('\x1b[1;31;40m' + '1.' + '\x1b[0m' + '\x1b[2;33;40m' + 'Brown' + '\x1b[0m')
        print('\x1b[1;31;40m' + '2.' + '\x1b[0m' + '\x1b[1;31;40m' + 'Red' + '\x1b[0m')
        print('\x1b[1;31;40m' + '3.' + '\x1b[0m' + '\x1b[3;33;40m' + 'Orange' + '\x1b[0m')
        print('\x1b[1;31;40m' + '4.' + '\x1b[0m' + '\x1b[1;33;40m' + 'Yellow' + '\x1b[0m')
        print('\x1b[1;31;40m' + '5.' + '\x1b[0m' + '\x1b[1;32;40m' + 'Green' + '\x1b[0m')
        print('\x1b[1;31;40m' + '6.' + '\x1b[0m' + '\x1b[1;34;40m' + 'Blue' + '\x1b[0m')
        print('\x1b[1;31;40m' + '7.' + '\x1b[0m' + '\x1b[1;35;40m' + 'purple' + '\x1b[0m')
        print('\x1b[1;31;40m' + '8.' + '\x1b[0m' + '\x1b[1;30;47m' + 'Gray' + '\x1b[0m')
        print('\x1b[1;31;40m' + '9.' + '\x1b[0m' + '\x1b[1;37;40m' + 'White' + '\x1b[0m')
        print('\x1b[1;31;40m' + 'please remember this' + '\x1b[0m')
        print("please insert first color bar")
        x = input()
        print("please insert second color bar")
        y = input()
        print("please insert third color bar")
        z = input()
        a = 10**z
        b = x*10
        c = b+y
        f = c*a
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
        print(f)
        print("Ohm")
        print('\x1b[1;33;40m' + '=====================' + '\x1b[0m')
