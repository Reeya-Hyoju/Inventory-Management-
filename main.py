import read
import write
import operation
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('               Welcome to Equipment Rental Shop')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#display invalid message
def invalid_message():
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("Invalid option. Please provide valid option.")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#create main function
def main():
    
        e = False
        while e == False:
            try:
                choice=int(input("\n\nSelect an option.\n (1) Enter '1' to view equipments. \n (2) Enter '2' to rent equipments. \n (3) Enter '3' to return equipments. \n (4) Enter '4' to exit. \n Enter your choice."))
                e = True
            except:
                invalid_message()

        if choice == 1:
            
            read.read()
            
        elif choice == 2:
            operation.rent_equipments()
            
        elif choice == 3:
            
            write.return_equipments()
        elif choice == 4:
            print('\n\n\n\t\t\tThank you for visiting us :)')
            loop = False
        else:
            invalid_message()
            
'calling main function'

loop = True
while loop == True:
    main()
    data = input("Do you want to continue (y/n) : ");
    if data == "n" : 
        loop = False
    else : 
         loop = True
    

