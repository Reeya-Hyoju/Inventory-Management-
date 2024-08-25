import datetime
'create return_equipments function'
def return_equipments():
    'to print if okay to return'
    def applicable():
        print("\n------------------------------------------")
        print("You have the option to return the equipment.")
        print("------------------------------------------\n")

    'to print if not okay to return.'
    def unapplicable():
        print("\n--------------------------------------------------------------")
        print("The equipment you wish to return cannot be found in the database.")
        print("---------------------------------------------------------------\n")

    'to print if invalid input is entered.'
    def invalid_message():
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("invalid option. Please provide valid option.")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    def goods(dictionary):
        tfile = open("equipment.txt","w")#Opening equipment.txt in writing mode
        for i in dictionary.values():
            line = str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]))
            tfile.write(line)
            tfile.write("\n")
        tfile.close()
        
    'to create a text file after each transaction'
    def create_writefile(cname, phnumber, date, total, equipmentName, equipmentBrand, cfine):
        fileName = "Return_" + cname + "_" + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond) + str(datetime.datetime.now().hour) + ".txt"

        tfile = open(fileName, "w")#Opening fileName in writing mode
        tfile.write("Name of the customer : " + cname + "\n")
        tfile.write("Phone number: " + str(phnumber))
        tfile.write("Date of return : " + str(date) + "\n")
        tfile.write("Total price of equipment: " + str(total) + "\n")
        tfile.write("Returned equipment: " + "\n")
        tfile.write("Fine: " + str(cfine) + "\n")
       
        for i, j in zip(equipmentName,equipmentBrand):
            tfile.write(i + ":- " + j)
            tfile.write("\n")
        tfile.close()
        
    'to calculate the total price'
    def total_price(dictionary, quantitydet, equipmentID):
        price = float(dictionary[returnID][2].replace("$",""))
        print("The price of equipment:", price)
        priceperitem = price * quantitydet
        return priceperitem

    'to take number of equipment to return as input'
    def quantity_equipment(quantity_goods):
        exc = False
        while exc == False:
            try:
                quantity = int(input("\nEnter the number of equipment to return: "))
                exc = True
            except:
                invalid_message()
   
        while quantity <=0 :
            if quantity <= 0:
                print("\n----------------------------------------")
                print("Input is invalid. Please provide valid input.")
                print("---------------------------------------------\n")
            
            ex = False
            while ex == False:
                try:
                    quantity = int(input("Please enter a valid quantity: "))
                    ex = True
                except:
                    invalid_message()
            
        return quantity

    'to create dictionary and store data in it.'
    def return_dictionary():
        tfile = open("equipment.txt", "r")#Opening data.txt in reading mode
        counter = 0
        dictionary = {}#creating dictionary
        for b in tfile:
            counter = counter + 1
            b = b.replace("\n","")
            b = b.split(',')

            dictionary[counter] =  b

        return dictionary
        tfile.close()

    'to display data from the textfile in an organized way'
    def return_display():
        tfile = open("equipment.txt","r")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("\tID \tEquipment Name                           Equipment Brand         Price       Quantity")
        print("-----------------------------------------------------------------------------------------------------------------")
        counter = 0
        for b in tfile:
            counter = counter + 1
            print("\t", counter, "\t" + b.replace(",","\t"))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        tfile.close()
        
    'to check if the id is valid'
    def validID():
        exception = False
        while exception == False:
            try:
                valid_ID = int(input("Please enter the ID of equipment you want to return: "))
                exception = True
            except:
                invalid_message()
   
        while valid_ID <= 0 or valid_ID > len(return_dictionary()):
            try:
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("\nThe provided equipment ID is not valid. Please attempt again.\n")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                return_display()
                valid_ID = int(input("\n Please enter the ID of equipment you want to return: "))
            except:
                invalid_message()
        return valid_ID
    'calling functions'
    return_display()
        
    dictionary = return_dictionary()
    returnID = validID()

    returnNamelist = []
    returnBrandlist = []

    if int(dictionary[returnID][3]) > 0:
        applicable()

        quantity = quantity_equipment(int(dictionary[returnID][3]))
        dictionary[returnID][3] = int(dictionary[returnID][3]) + quantity#Adding quantity after returning

        
        returnNamelist.append(dictionary[returnID][0])
        returnBrandlist.append(dictionary[returnID][1])

        goods(dictionary)

        totalPrice = total_price(dictionary,quantity,returnID)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Would you like to return other equipment as well?")
        returnanother = input("Please enter 'y' if you want to return another equipment: ").lower()

        loop = True
        while loop == True:
            
            if returnanother == "y":
                return_display()
        
                dictionary = return_dictionary()
                returnID = validID()


                if int(dictionary[returnID][3]) > 0:
                    applicable()

                    quantity = quantity_equipment(int(dictionary[returnID][3]))
                    dictionary[returnID][3] = int(dictionary[returnID][3]) + quantity


                    returnNamelist.append(dictionary[returnID][0])
                    returnBrandlist.append(dictionary[returnID][1])

                    goods(dictionary)

                    totalPrice = total_price(dictionary,quantity,returnID) + totalPrice
                

                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("Do you want to return another equipment as well?")
                    returnanother = input("Please enter 'y' if you want to return another equipment: ").lower()
                        
            else:
                fineperequipment = 5
                Totalfine = 0
                name = input(" Pleade enter the name of customer: ")
                ab = True
                while ab == True:
                    try:
                        number = int(input("Please enter your phone number: "))
                        ab = False
                    except:
                        invalid_message()
                cd = True
                while cd == True:
                    try:
                        daysafter = int(input("How many days have passed since you rented it? Please enter: "))
                        cd = False
                    except:
                        invalid_message()
                tDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                listname = (str(returnNamelist)[1:-1])
                listbrand = (str(returnBrandlist)[1:-1])
                
                if daysafter > 5:
                    extradays = daysafter - 5
                    for k in returnNamelist:
                        Totalfine  += extradays*int(quantity)*fineperequipment
                else:
                    Totalfine = 0
                Totalcost = totalPrice + Totalfine
                'To print invoice/bill'
                print("\n-------------------------------------------------------------------")
                print("\t\t\t\t INVOICE")
                print("--------------------------------------------------------------------\n")
                print("\t\t\t\t\t", tDate)
                print("Customer Name:", name)
                print("Phone number: ", number)
                print("Total price of equipment:"," $", totalPrice)
                print("Name of returned equipment:", listname)
                print("Brand of returned equipment:", listbrand)
                print("Fine: ","$", Totalfine)
                print("Total cost: ", Totalcost)
                print("\n")
                print("\n The equipment has been returned.\n")
                print("\t\t\t\t Thank you.")
                create_writefile(name, number, tDate, totalPrice, listname, listbrand, Totalfine)
                loop = False#loop break
                
    else:
        unapplicable()


