def account_1() :
    print(
        '''
    
    
    -------------------------------------------------
                Welcome to Access Bank
            type start to insert Atm card''')
    user_first_input = input("> ")
    if user_first_input == "start".lower() :
        def start() :
            print('''

                ACCESS BANK''')
            print("---------------------------------------")

            pin_code = int("5567")
            password_starts = 0
            password_ends = 3
            while password_starts < password_ends :
                code = int(input("input Pin>  "))
                print("---------------------------------------")
                password_starts += 1
                if code == pin_code :
                    def home_page() :
                        account_balance = 30000
                        pin_code = int("5567")
                        print('''
------------------------------------------------

    1 > Check Balance             2 > Withdraw


    3 > Cancel

------------------------------------------------     
            ''')
                        atm_options = input(">>> ")
                        if atm_options == "1" :  # this is to show account balance
                            print(f"Balance: ${account_balance}")
                            command = input('''
Do you still want to continue:  Y/N> ''')
                            if command == "y".lower() :
                                print(home_page())
                            else :
                                print("   Thank you for banking with us")
                                print(account_1())

                        elif atm_options == "2" :  # this is for withdrawals
                            withdraw_input = int(input("input amount>> "))
                            if withdraw_input < account_balance :
                                summation = account_balance - withdraw_input
                                summation2 = account_balance - summation
                                print(f'are you sure you want to withdraw ${summation2}  Y/N ')
                                confirmation = input(">> ")

                                if confirmation == "y".lower() :
                                    print('''pls take out your cash
                                        ''')
                                    print("Do you wish to continue  Y/N")
                                    withdraw_input2 = input(">> ")

                                    if withdraw_input2 == "y".lower() :
                                        print(home_page())
                                    elif withdraw_input2 == "n".lower() :
                                        print('''
Thank you for banking with us
                                            ''')
                                        print("please take out your card")
                                        print(account_1())
                                elif confirmation == "n".lower() :
                                    print(home_page())
                            else :
                                print("Sorry! sorry you can't withdraw such amount")
                                withdraw_input3 = input("Do you wish to continue Y/N> ")

                                if withdraw_input3 == "y".lower() :
                                    print("Thank you for banking with us")
                                    print(account_1())
                                else :
                                    print(
                                        '''
                                
                                        Thank you for banking with us
                                
                                        ''')
                                    print(start())

                        elif atm_options == "3" :  # this area is for returning the whole code to start---
                            # ---from the "def start():" function
                            print("Thank you for Banking With us")
                            print(account_1())

                        else :
                            print("sorry! invalid commands")
                            print(home_page())

                    home_page()
                else :
                    print("invalid pin")

        start()
    else :
        print("invalid input!")
        print(account_1())


account_1()














