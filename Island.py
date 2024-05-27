import mysql.connector
from mysql.connector import errorcode

# mention your root password here. set the password going to the MySQL WORKBENCH
cnx = mysql.connector.connect(user='root', password='@password',
                              host='127.0.0.1',
                              database='argentina')

# \connect root@localhost:3306

cur = cnx.cursor()

def Questioner():

    print("From the above islands in Argentina, your trip to which island ? ")


    Query = ("Select Distinct Province from islands;")
    cur.execute(Query)
    provinces = [x[0] for x in cur]
    for count in range(len(provinces)):
        print(f"{count+1}. {provinces[count]}")

    print("For selecting province, press the numeric value assigned to it (1/2/3/4/5)")
    print()
    User_Province = int(input("Please enter :-- "))
    User_Province = provinces[User_Province-1]



    print(f"In your selected province {User_Province}, Following Islands are Found :- ")

    Query = (f"Select Island_Name from islands WHERE Province='{User_Province}'")
    cur.execute(Query)
    islands = [x[0] for x in cur]
    for count in range(len(islands)):
        print(f"{count + 1}. {islands[count]}")

    print("For selecting island, press the numeric value assigned to it (1/2/3/4/5)")
    print()
    User_Island = int(input("Please enter :-- "))



    print(f"For {islands[User_Island-1]} island you have selected, Following Airlines are Found :- ")

    Query = (f"Select Airline from airlines WHERE Island_Name='{islands[User_Island-1]}'")
    cur.execute(Query)
    Airlines = [x[0] for x in cur]
    for count in range(len(Airlines)):
        print(f"{count + 1}. {Airlines[count]}")



Questioner()


cnx.commit()


cur.close()
cnx.close()

















