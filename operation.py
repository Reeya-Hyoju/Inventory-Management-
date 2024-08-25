import datetime
'to create function rent_equipments'
def rent_equipments():
    'to print if the  equipment is applicable to rent.'
    def applicable():
        print("\n--------------------------------------------------")
        print("The  equipment you want to rent is applicable.")
        print("----------------------------------------------------\n")

    'to print if the  equipment is not applicable.'
    def unapplicable():
        print("\n--------------------------------------------")
        print("The  equipment is unapplicable at the moment.")
        print("-------------------------------------------\n")

    'to print if invalid input is entered'
    def invalid_message():
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("Invalid option. Please provide valid option.")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    def goods(dictionary):
        tfile = open("equipment.txt","w")
        for i in dictionary.values():
            line = str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]))
            tfile.write(line)
            tfile.write("\n")
        tfile.close()

    'to create a text file after each transaction'    
    def create_operationfile(cname, phnumber, date, total, name_equipment, brand_equipment):
        tfile_name = "Rent_" + cname + "_" + str(datetime.datetime.now().second) + ".txt"

        tfile = open(tfile_name, "w")
        tfile.write("Name of the customer : " + cname + "\n")
        tfile.write("Phone number: " + str(phnumber))
        tfile.write("Date of rent : " + str(date) + "\n")
        tfile.write("Total price of  equipment: " + str(total) + "\n")
        tfile.write("Rented  equipment: " + "\n")
       
        for i, j in zip(name_equipment, brand_equipment):
            tfile.write(i + ":- " + j)
            tfile.write("\n")
        tfile.close()

    'to calculate the total price per item'
    def total_price(dictionary, quantitydet,  equipmentID):
        price = float(dictionary[rentID][2].replace("$",""))
        print("The price of  equipment:", price)
        priceperitem = price * quantitydet
        return priceperitem

    'to take the number of  equipment to rent as input.'
    def quantity_equipment(quantity_goods):
        exc = False
        while exc == False:
            try:
                quantity = int(input("\nEnter the number of  equipment to rent: "))
                exc = True
            except:
                invalid_message()
   
        while quantity <=0 or quantity > quantity_goods:
            if quantity <= 0:
                print("\n---------------------------------------------")
                print("Input is invalid. Please provide valid input.")
                print("------------------------------------------------\n")
            elif quantity > quantity_goods:
                print("\n------------------------------------------------------------------------------------")
                print("The quantity you've entered exceeds our available stock. Please input a new quantity..")
                print("------------------------------------------------------------------------------------\n")
            ex = False
            while ex ==False:
                try:
                   quantity = int(input("Please enter a valid quantity: "))
                   ex = True
                except:
                    invalid_message()
            
        return quantity
        
    'to create dictionary'   
    def rent_dictionary():
        tfile = open("equipment.txt", "r")
        counter = 0
        dictionary = {}
        for b in tfile:
            counter = counter + 1
            b = b.replace("\n","")
            b = b.split(',')

            dictionary[counter] =  b

        return dictionary
        tfile.close()

    'to display contents from textfile in an organized way'
    def rent_display():
        tfile = open("equipment.txt","r")
        print("-----------------------------------------------------------------------------------------------------")
        print("\tID \tEquipment Name                           Equipment Brand         Price       Quantity")
        print("-----------------------------------------------------------------------------------------------------")
        counter = 0
        for a in tfile:
            counter = counter + 1
            print("\t", counter, "\t" + a.replace(",","\t"))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        tfile.close()
    
    'to check if the id entered is valid or not'
    def validID():
        exception = False
        while exception == False:
            try:
                valid_ID = int(input("Please enter the ID of  equipment you want to rent: "))
                exception = True
            except:
                invalid_message()
   
        while valid_ID <= 0 or valid_ID > len(rent_dictionary()):
            try:
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("\nThe provided equipment ID is not valid. Please attempt again.\n")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                rent_display()
                valid_ID = int(input("\nEnter the ID of  equipment you want to rent: "))
            except:
                invalid_message()
        return valid_ID

    rent_display()
        
    dictionary = rent_dictionary()
    rentID = validID()

    rentNamelist = []
    rentBrandlist = []

    if int(dictionary[rentID][3]) > 0:
        applicable()

        quantity = quantity_equipment(int(dictionary[rentID][3]))
        dictionary[rentID][3] = int(dictionary[rentID][3]) - quantity
        file = open("equipments.txt","w")
        for values in dictionary.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
            file.write("\n")
        file.close()
                                

        
        rentNamelist.append(dictionary[rentID][0])
        rentBrandlist.append(dictionary[rentID][1])

        goods(dictionary)

        totalPrice = total_price(dictionary,quantity,rentID)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Would you like to rent additional equipment as well?")
        rentanother = input("Please enter 'y' if you want to rent another  equipment: ").lower()

        loop = True
        while loop == True:
            
            if rentanother == "y":
                rent_display()
        
                dictionary = rent_dictionary()
                rentID = validID()


                if int(dictionary[rentID][3]) > 0:
                    applicable()

                    quantity = quantity_equipment(int(dictionary[rentID][3]))
                    dictionary[rentID][3] = int(dictionary[rentID][3]) - quantity
                    
                
                    file = open("equipment.txt","w")
                    for values in dictionary.values():
                        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
                        file.write("\n")
                    file.close()
                                                   
                    rentNamelist.append(dictionary[rentID][0])
                    rentBrandlist.append(dictionary[rentID][1])

                    goods(dictionary)

                    totalPrice = total_price(dictionary,quantity,rentID) + totalPrice
                

                    print("=======================================================================")
                    print("Do you also wish to rent other equipment?")
                    rentanother = input("Please enter 'y' if you want to rent another  equipment: ").lower()
                        
            else:
                name = input("Please enter the name of customer: ")
                ab = True
                while ab == True:
                    try:
                        number = int(input("Please enter your phone number:"))
                        ab = False
                    except:
                        invalid_message()
                tDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                listname = (str(rentNamelist)[1:-1])
                listbrand = (str(rentBrandlist)[1:-1])

                print("\n-------------------------------------------------------------------")
                print("\t\t\t\t INVOICE")
                print("--------------------------------------------------------------------\n")
                
                print("\t\t\t\t\t", tDate)
                print("Customer Name:", name)
                print("Phone number: ", number)
                print("Total price:"," $", totalPrice)
                print("Name of rented  equipment:", listname)
                print("Brand of rented  equipment:", listbrand)
                print("\n")
                print("The  equipment has been rented.")
                print("Ensure that you bring back the equipment within a 5-day period to prevent any fines.")
                print("\t\t\t\t Thank you.")
                create_operationfile(name, number, tDate, totalPrice, listname, listbrand)
                loop = False #loop break
                
    else:
        unapplicable()
        
