import mysql.connector
import random
import math
from mysql.connector import errorcode

# mention your root password here. set the password going to the MySQL WORKBENCH
cnx = mysql.connector.connect(user='root', password='NonuAshish1234)(*&',
                              host='127.0.0.1')

# \connect root@localhost:3306

cur = cnx.cursor()

try:
    cur.execute("DROP DATABASE argentina;")
except mysql.connector.Error as err:
    print("Database doesn't exist !!! Going to created...")

cur.execute("CREATE DATABASE argentina;")

cnx.database = "argentina"

TABLES = {}

TABLES["PLACE"] = (
    "CREATE TABLE `ISLANDS` ("
    "  `Island_Name` varchar(50) NOT NULL,"
    "  `Province` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`Island_Name`)"
    ") ENGINE=InnoDB")


# Later add price, country_init and other things...
TABLES["PATH_FINDER"] = (
    "CREATE TABLE `AIRLINES` ("
    "  `Airline` varchar(50) NOT NULL,"
    "  `Island_Name` varchar(50) NOT NULL"
    ") ENGINE=InnoDB")


TABLES["SURVIVAL"] = (
    "CREATE TABLE `HOTELS` ("
    "  `Province` varchar(50) NOT NULL, "
    "  `Hotel` varchar(50) NOT NULL, "
    "  `Hotel_Cost` varchar(50) NOT NULL) ENGINE=InnoDB")


for DATA_TYPE in TABLES:
    DATA_DESC = TABLES[DATA_TYPE]
    try:
        print("Creating table {}: ".format(DATA_TYPE), end='')
        cur.execute(DATA_DESC)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")



add_place = ("INSERT INTO islands "
               "(Province, Island_Name) "
               "VALUES (%s, %s)")

add_path_finder = ("INSERT INTO airlines "
               "(Island_Name, Airline) "
               "VALUES (%s, %s)")

add_survivor = ("INSERT INTO hotels "
               "(Province, Hotel, Hotel_Cost) "
               "VALUES (%s, %s, %s)")


argentina_islands = {
    "Buenos Aires Province": ["Martín García Island", "Juncal Island", "Oyarvide Island"],
    "Tierra del Fuego Province": ["Isla Grande de Tierra del Fuego", "Isla de los Estados", "Isla Martillo"],
    "Chubut Province": ["Isla Escondida", "Isla Vernaci", "Isla Tova"],
    "Santa Cruz Province": ["Isla Pavón", "Isla Pingüino", "Isla Leones"],
    "Río Negro Province": ["Isla Huemul", "Isla Victoria", "Isla de los Césares"]
}

airlines = ["LATAM Airlines", "American Airlines", "Eastern Airlines", "Copa Airlines",
            "Aerolíneas Argentinas", "Flybondi"]




for province in argentina_islands.keys():
    for item_island in argentina_islands[province]:
        cur.execute(add_place, (province, item_island))
        pass


# Create a nested list to store suitable airlines for each island
suitable_airlines = {}

# Check each island and add suitable airlines to the nested list
for province, islands in argentina_islands.items():
    for island in islands:
        # Check if Aerolíneas Argentinas or Flybondi can fly to the island
        if island in ["Martín García Island", "Juncal Island", "Oyarvide Island",
                      "Isla Grande de Tierra del Fuego", "Isla de los Estados", "Isla Martillo"]:
            suitable_airlines[island] = ["Aerolíneas Argentinas", "Flybondi"]

        else:
            suitable_airlines[island] = airlines

for item in suitable_airlines:
    for airline in suitable_airlines[item]:
        cur.execute(add_path_finder, (item, airline))
        pass

# Print the nested list
# print(suitable_airlines)

def Random_Suffix():
    Letters = ['F', 'D', 'X', 'Y']
    Str = "0x"
    for i in range(12):
        if(bool(random.choice((0, 1)))):
            Str += random.choice(Letters)

        else:
            Str += chr(random.randint(48, 57))

    return Str

Hotel_type_prefixes = ["Advanced", "Minecraft", "Minimal", "Rudiment", "Minecraft","Advanced", "Rudiment", "Minimal"]
Hotel_Prices = {"Advanced":[], "Minimal":[], "Minecraft":[], "Rudiment":[]}

def Set_PriceHotels():
    for count in range(len(Hotel_Prices)):
        Hotel_Prices[list(Hotel_Prices.keys())[count]] = [
            f"Floor {i + 1} Hotels :- ${(random.randint(450 // (count + 1), 550 // (count + 1)))}" for i in
            range(random.randint(3, 4))]
        # print(Hotel_Prices[list(Hotel_Prices.keys())[count]])

for province in argentina_islands:
    for i in range(random.randint(1, 4)):
        Element = random.choice(Hotel_type_prefixes)
        random.shuffle(Hotel_type_prefixes)
        Set_PriceHotels()
        Hotel_Naming = f"Hotel_{Element}_{Random_Suffix()}"
        for j in range(len(Hotel_Prices[Element])):
            cur.execute(add_survivor, (province, Hotel_Naming, Hotel_Prices[Element][j]))
            # print(Hotel_Naming)

cnx.commit()
# print(argentina_islands)
cur.close()
cnx.close()




