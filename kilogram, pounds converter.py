print('Welcome to kg/pounds weight converter')
proper_name = False
name = ''
while not proper_name:
    name = input("Whats your name? ")
    if 3 > len(name) or len(name) > 50:
        print('\nname is either too short or too long')
    else:
        proper_name = True
else:
    print('Welcome ' + name)
    weight = float(input("Whats your weight in kilogram|pounds: "))
    convert_To = input("press k to convert your weight to kilogram, or l to convert your weight to pounds: ").lower()
    if convert_To == 'k':
        realWeight = round(float(weight) / 2.20462, 2)
        print(f'You are {realWeight}  kilos')
    elif convert_To == 'l':
        realWeight = round(float(weight) * 2.20462, 2)
        print(f'You are {realWeight}  pounds')
    else:
        print('please either write k or l')