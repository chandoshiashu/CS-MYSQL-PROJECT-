import mysql.connector
from mysql.connector import errorcode

# mention your root password here. set the password going to the MySQL WORKBENCH
cnx = mysql.connector.connect(user='root', password='NonuAshish1234)(*&',
                              host='127.0.0.1',
                              database='argentina')

# \connect root@localhost:3306

cur = cnx.cursor()
def Invalid_Repeat(User_None):
    if (User_None):
        print("\n\t\tKindly Input Valid Value According to the Menu :(( ")
        Press_Key = input("\t\t\tPress Enter Key to Try Again :)) (For Exit, Press E) \n\t\t\t:-- ")
        if (Press_Key == "E"): exit(1)

def Q_Province():

    Query = ("Select Distinct Province from islands;")
    cur.execute(Query)
    provinces = [x[0] for x in cur]

    User_Province = -1
    User_None = False
    print()
    while(User_Province > len(provinces) or User_Province <= 0):
        Invalid_Repeat(User_None)
        User_None = True

        for count in range(len(provinces)):
            print(f"{count + 1}. {provinces[count]}")

        print("\n\t\t From the above islands in Argentina, your trip to which island ? ")
        print("\t\t For selecting province, press the numeric value assigned to it (1/2/3/4/5) \n")

        User_Province = int(input("\t\t\tPlease enter :-- "))

    User_Province = provinces[User_Province - 1]
    return User_Province


def Q_Island(User_Province):

    Query = (f"Select Island_Name from islands WHERE Province='{User_Province}'")
    cur.execute(Query)
    islands = [x[0] for x in cur]

    User_Island = -1
    User_None = False

    while(User_Island > len(islands) or User_Island <= 0):
        Invalid_Repeat(User_None)
        User_None = True

        print(f"\nIn your selected province {User_Province}, Following Islands are Found :- \n")
        for count in range(len(islands)):
            print(f"{count + 1}. {islands[count]}")

        print("\n\t\tFor selecting island, press the numeric value assigned to it (1/2/3/4/5)")
        print()
        User_Island = int(input("\t\t\tPlease enter :-- "))

    return islands[User_Island-1]


def Q_Airline(island):

    Query = (f"Select Airline from airlines WHERE Island_Name='{island}'")
    cur.execute(Query)
    Airlines = [x[0] for x in cur]

    User_Airline = -1
    User_None = False

    while(User_Airline > len(Airlines) or User_Airline <= 0):
        Invalid_Repeat(User_None)
        User_None = True

        print(f"\nFor {island} island, you have selected, Following Airlines are Found :- \n")
        for count in range(len(Airlines)):
            print(f"{count + 1}. {Airlines[count]}")

        print("\n\t\tFor selecting Airline, press the numeric value assigned to it (1/2/3/4/5) \n")
        User_Airline = int(input("\t\t\tPlease enter :-- "))

    return Airlines[User_Airline-1]

def Q_Hotel(User_Province, Airline):
    Query = f"Select Distinct Hotel from Hotels WHERE province='{User_Province}'"
    cur.execute(Query)
    Hotels = [data[0] for data in cur]


    Count_Var = 1
    FloorWise = []

    User_Hotel = "N1"
    User_None = False
    print(ord(User_Hotel[1])-48, len(Hotels))

    Condition = False
    while(Condition == False):
        Invalid_Repeat(User_None)
        Count_Var = 1

        User_None = True
        print(
            f"\nCongrats ! You chose the {Airline} Airline For your Trip, \n \t \t At the province {User_Province}, Following Hotels are Found :-  \n")
        for Hotel in Hotels:
            print(f"H{Count_Var}. {Hotel}")
            Count_Var += 1
            cur.execute(f"Select Hotel_Cost from Hotels WHERE province='{User_Province}' AND Hotel='{Hotel}'")
            FloorWise = [dataSet[0] for dataSet in cur]
            for element in FloorWise[:2]:
                print(element)

            print("Other Options Available..... \n")

        print("\t\tFor Selecting the Hotel, Press the value assigned to it (H1/H2/H3/H4/H5) :-- \n")
        User_Hotel = input("\t\t\tPlease Enter :-- ")
        Condition = (User_Hotel[0] == "H" and (ord(User_Hotel[1])-48 <= len(Hotels) and ord(User_Hotel[1])-48 != 0))

    return (Hotels[int(User_Hotel[1]) - 1], FloorWise)


def Q_Hotel_Floor(FloorWise, User_Hotel):

    User_Hotel_Floor = "N1"
    User_None = False

    Condition = False
    while(Condition == False):
        Invalid_Repeat(User_None)
        User_None = True

        print(f"You have choosen the Hotel named {User_Hotel}")
        for element in FloorWise:
            print(element)

        print(f"\n\t\tWhich Hotel you want to get into ? ... ")
        print(f"\t\tPress the Floor Number to proceed further (F1/F2/F3/F4) :-- ")
        User_Hotel_Floor = input("\n\t\t\tPlease Enter :-- ")
        Condition = (User_Hotel_Floor[0] == "F" and ord(User_Hotel_Floor[1])-48 <= len(FloorWise) and ord(User_Hotel_Floor[1])-48 != 0)

    return User_Hotel_Floor


add_receipt = ("INSERT INTO receipts "
               "(Username, Name_Id, Island, Province, Trip_Id) "
               "VALUES (%s, %s, %s, %s, %s)")
New_Trip = True

def Questioner():

    global New_Trip
    New_Trip = False
    Username = input("Enter your full name here :- ")
    User_Province = Q_Province()
    User_Island = Q_Island(User_Province)
    User_Airline = Q_Airline(User_Island)
    User_Hotel = Q_Hotel(User_Province, User_Airline)
    User_Hotel_Floor = Q_Hotel_Floor(User_Hotel[1], User_Hotel[0])

    User_Id = (Username.replace(" ", "")).capitalize() + "_0FUSER2027"
    Trip_Id = (User_Province.replace(" ", "")+"_"+User_Island.replace(" ", "")).capitalize() + "_0FTRIP2027"

    cur.execute(add_receipt, (Username, User_Id, User_Island, User_Province, Trip_Id))

    print("\n \n \t\t\t\tThank You :)) ")
    print("\t\tYour Trip have been confirmed :)) ")


    User_Ask = None
    while User_Ask != 4:
        User_Ask = int(input("Press (1/2/3) accordingly \n1. Show my trip details \n2. Cancel my Current Trip\n3. To establish my new trip\n4. Exit\n \t\t\t:-- "))
        if(str(User_Ask) not in "1234"):
            print("Invalid Input \nKindly Re-enter :)\n If you want to exit, press 4")

        else:
            if User_Ask == 1:
                print("\t\t\tYour Current Trip Details... \n\n")
                print(
                    f"\t\t\t Username : {Username} (User_Id : {User_Id}) \n\t\t\t Trip_Id : {Trip_Id} \n\t\t\t Island : {User_Island} \n\t\t\t Province : {User_Province} \n\t\t\t Airline : {User_Airline} \n\t\t\t "
                    f"Hotel : {User_Hotel[0]} \n\t\t\t Hotel In-Depth Address : {User_Hotel_Floor} \n")

            elif User_Ask == 2:
                cur.execute(f"DELETE from receipts where Name_Id = '{User_Id}' and Trip_Id = '{Trip_Id}' ")
                print("Your Trip has been cancelled !! ")


            elif User_Ask == 3: New_Trip = True; User_Ask = 4



Questioner()
while(New_Trip != False):
    Questioner()

print("Thank You :)) ")

cnx.commit()

cur.close()
cnx.close()
