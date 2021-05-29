def menu():
    ussd = int(input("Please type in your ussd: "))
    print("1>Quick banking\n2>Open an account\n3>Loans\n4>FirstMonie")
    print('')
    option = int(input('select an option\n : '))
    if option == 1:
       print("1>Transfer money\n2>Airtime (self)\n3>Airtime (others)\n4>Enquiry services\n5>Data\n6>Pay bills\n7>Next page")
       print('')
       option2 = int(input("Please select an option\n: "))
       if option2 == 1:
           amount = int(input("Enter amount: "))
           account = int(input("Enter Account number: "))
           name = ("Abdulsalam Aliyu Nasir")
           print("Select recipient bank")
           print('')
           bank = int(input("1>First bank\n 2>Access bank\n 3>GTBank\n: "))
           if bank == 1:
               pin = int(input("Enter pin\n: "))
               if pin == 111:
                 print("Do youn want to tranfer", amount, "to", name, "?")
                 print('')
                 assure = int(input("1>Yes\n2>No:" ))
                 if assure == 1:
                    print("tansaction succeful")
                 else:
                     exit()
           elif bank == 2:
               pin = int(input("Enter pin\n: "))
               if pin == 111:
                 print("Do youn want to tranfer", amount, "to", name, "?")
                 assure = int(input("1>Yes\n2>No:" ))
                 if assure == 1:
                    print("tansaction succeful")
                 else:
                    print("Transaction decline")
                    exit()
           elif bank == 3:
               pin = int(input("Enter pin\n: "))
               if pin == 111:
                 print("Do youn want to tranfer", amount, "to", name, "?")
                 assure = int(input("1>Yes\n2>No:" ))
                 if assure == 1:
                    print("tansaction succeful")
                 else:
                    print("Transaction decline")
                    exit()
           else:
                print("wrong input")
       elif option2 == 2:
             airtime = int(input("1>For (self)\n2>For (others\n: )"))
             print('')
             if airtime == 1:
                amount = int(input("Enter amount: "))
                print("Transaction sucessful")
             elif airtime == 2:
                 amount = int(input("Enter amount: "))
                 number = int(input("Enter number: "))
                 print("Do you want to transfer", amount,"naira to", number,"?:\n 1>Yes\n 2>No ")
                 print('')
                 assure = int(input( ":"))
                 if assure == 1:
                   print("Transaction sucesseful")
                 elif assure == 2:
                     exit()
       elif option2 == 3:
           number = int(input("Enter number: "))
           amount = int(input("Enter amount: "))
           print("Do you want to send", amount,"naira to", number,"?:\n 1>Yes\n 2>No ")
           print('')
           assure = int(input())
           if assure == 1:
             print("Transaction sucesseful")
             print('')
             top = int(input("ENTER 1 TO RETURN TO MENU\n ENTER 2 TO END"))
             if top == 1:
                menu()
             elif top == 2:
                exit()
       elif option2 == 4:
           print("Please select a service")
           print('')
           enquiry = int(input("1>Balance Enquiry\n 2>BVN Enquiry\n 3>Account Number Enquiry\n 4>Mini Statement"))
           if enquiry == 1:
            print("Your Account is 10,000")
           elif enquiry == 2:
              print("Your BVN is 772255684")
           elif enquiry == 3:
              print("Your Account number is 3142399269")
           elif enquiry == 4:
              print("WELCOME TO FIRST BANK")
       elif option2 == 5:
            data = int(input("1>Self\n 2>Third party"))
            if data == 1:
              amount = int(input("Enter amount"))
              number = int(input("Enter number"))
              print("Do you want to recharge", amount,"naira to", number,"?:\n 1>Yes\n 2>No ") 
              print("Transaction sucesseful")
              top = int(input("ENTER 1 TO RETURN TO MENU\n ENTER 2 TO END"))
              if top == 1:
                 menu()
              elif top == 2:
                 exit()
            elif data == 2:
               amount = int(input("Enter amount"))
               number = int(input("Enter number"))
               print("Do you want to recharge", amount,"naira to", number,"?:\n 1>Yes\n 2>No ") 
               print("Transaction sucesseful")
               print('')
               top = int(input("ENTER 1 TO RETURN TO MENU\n ENTER 2 TO END"))
               if top == 1:
                   menu()
               elif top == 2:
                  exit()
       elif option2 == 6:
            bills = int(input("1>Cable TV\n 2>Electricity\n 3>Renewable energy\n 4>Gift and Bewad\n 5>Investment and Insurance\n 6>Next page"))
            if bills == 1:
               print("We move")
       elif option2 == 7:
             pages = int(input("1>Insurance\n2>Other services\n3>Merchant services\n4>Card control\n5>Reserve cash\n6>Prev page"))
             if pages == 5:
                print("Movement")
             else:
                print("We are working on this site, we'll get back to you later")
    elif option == 2:
         print("You are about to open a personal saving account")
         account = int(input("1>OPen with BVN\n2>OPen without BVN\n:"))
         if account == 1:
             bvn = int(input("Enter BVN\n:"))
             name = input("Enter your first name\n:")
             middleName = input("Enter your middle name\n:")
             lastName = input("Emter your last name\n:")
             dateOfBirth  = int(input("Enter your date of birth (ddmmyyyy). For example 2nd june, 2000 Enter 02062000\n:"))
             number = int(input("Enter your number\n:"))
             print("Account open sucesseful\n Welcome to firts bank, You firs!!")
         elif account == 2:
            name = input("Enter your first name\n:")
            middleName = input("Enter your middle name\n:")
            lastName = input("Enter your last name\n:")
            dateOfBirth  = int(input("Enter your date of birth (ddmmyyyy). For example 2nd june, 2000 Enter 02062000\n: ")) 
    elif option == 3:
        print("First Advance")
        advance = [5000, 10000, 15000, 20000, 25000, 30000]
        loan = input(": ")
        for loan in advance:
            # print(loan)
             print("Do youn want to take the loan of", loan, "?")
             assure = int(input("1>Yes\n2>No:" ))
             if assure == 1:
                print("Congrattulations you have succefully take the loan of", loan,"\n You are expected to have pay back before the end of the year")   
             elif assure == 2:
                print("loan decline")
                exit()
             break
    elif option == 4:
        account = int(input("Do you want to link your account to fistMonie ?\n1>Yes\n2>No\n :"))
        if account == 1:
            print("You have sucesseful link your bank account to firstMonie")
        elif account == 2: 
            exit()
menu()
if ussd == 894:
   menu()