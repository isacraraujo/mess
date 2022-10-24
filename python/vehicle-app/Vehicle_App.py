def app_in():
    app_in_lib = {0:exit_app, 1:oil_in}
    # 2:fuel_in, 3:dist_in}

    appInOption = True

    while appInOption != False:
        appInOption = int(input('Hello! Welcome to your vehicle app...\n' +
                                'What do you want to know about vehicle?\n' +
                                '1 - Oil\n' +
                                '2 - Fuel\n' +
                                '3 - Distance\n' +
                                '0 - Exit\n' +
                                '\n Your option: '))
        print(app_in_lib[appInOption]())

def oil_in():
    oil_ent1 = print('Your vehicle have {} liters of oil'.format(oil_r))

#def fuel_in():


#def dist_in():



def reg_v():
    try:
        fuel_r = int(input('What is the capacity of the GAS tank? '))
        oil_r = int(input('What is the capacity of the OIL tank? '))
        dist_r = int(input('How many miles your vehicle has already? '))
        return app_in()
    except ValueError:
        print ('Please, insert numbers!')
        return reg_v()
def exit_app():
    print('GoodBye')
    exit()
def startApp():
    auto_lib = {0:exit_app, 1:reg_v}

    auto_option = True

    while auto_option != False:
        auto_option = int(input('Welcome to your vehicle!\n' +
                                'To begin, you must choose one option:\n' +
                                '1 - Register a vehicle\n' +
                                '2 - Choose a template\n' +
                                '0 - Exit\n' +
                                '\n Your option: '))
        print(auto_lib[auto_option]())

startApp()
