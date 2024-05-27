import mysql.connector
from mysql.connector import errorcode

# mention your root password here. set the password going to the MySQL WORKBENCH
cnx = mysql.connector.connect(user='root', password='@password',
                              host='127.0.0.1',
                              database='argentina')
# \connect root@localhost:3306

cur = cnx.cursor()

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
    "  `Island_Name` varchar(50) NOT NULL, "
    "  `Hotel_Dest` varchar(50) NOT NULL, "
    "  `Survival_Cost` varchar(50) NOT NULL) ENGINE=InnoDB")


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
               "(Island_Name, Province, Hotel_Dest, Price, Survival_Cost) "
               "VALUES (%s, %s, %s, %s, %s)")


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


# Print the nested list
# print(suitable_airlines)

cnx.commit()

# print(argentina_islands)


cur.close()
cnx.close()




