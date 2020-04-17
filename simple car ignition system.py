print('Welcome to Car Operation System')
# command = ''
engine_Off = True

while True:
    command = input('> ').lower()
    if command == "start" and engine_Off is True:
        print("car started")
        engine_Off = False
    elif command == "start" and engine_Off is False:
        print("Car is already working baby")
    elif command == "stop" and engine_Off is False:
        print("car stopped working")
        engine_Off = True
    elif command == "stop" and engine_Off is True:
        print("car already is not working")
    elif command == 'help' or command == '?':
        print('''Write:
Start: to start the engine
Stop: to stop the engine
help or ?: to see what to do
        ''')
    else:
        print("Sorry, I don't understand what you have written")