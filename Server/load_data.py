import csv
import mysql.connector
from config import Config
# file to load data from csv folder to the database

# sql connection
config_data = Config()
cnx = mysql.connector.connect(user='root', password=config_data.DB_PASS,
                              host='localhost',
                              database=config_data.database_name)
curr = cnx.cursor()

# transferring data from category csv to categories table
with open('Data\\category.csv','r') as file_handler:
    csv_reader = csv.reader(file_handler)
    for i in csv_reader: 
        tup = (i[1],i[2])
        add_user = ("INSERT INTO categories "
               "(name,category_sequence) "
               "VALUES (%s,%s)")
       
        curr.execute(add_user,tup)
cnx.commit()
curr.close()

# transferring data from starters csv to starters table
curr = cnx.cursor()
with open('Data\\starter.csv','r') as file_handler:
    csv_reader = csv.reader(file_handler)
    for i in csv_reader: 
        tup = (i[1],i[0],i[2],i[3],i[4],i[5])
        add_user = ("INSERT INTO starters "
               "(name,item_sequence,price,available,veg,description) "
               "VALUES (%s,%s,%s,%s,%s,%s)")
        curr.execute(add_user,tup)
cnx.commit()
curr.close()

# transferring data from salads csv to salads table
curr = cnx.cursor()
with open('Data\\salads.csv','r') as file_handler:
    csv_reader = csv.reader(file_handler)
    for i in csv_reader: 
        tup = (i[1],i[0],i[2],i[3],i[4],i[5])
        add_user = ("INSERT INTO salad "
               "(name,item_sequence,price,available,veg,description) "
               "VALUES (%s,%s,%s,%s,%s,%s)")
        curr.execute(add_user,tup)
cnx.commit()
curr.close()

# transferring data from desserts csv to desserts tables
curr = cnx.cursor()
with open('Data\\desserts.csv','r') as file_handler:
    csv_reader = csv.reader(file_handler)
    for i in csv_reader: 
        tup = (i[1],i[0],i[2],i[3],i[4],i[5])
        add_user = ("INSERT INTO desserts "
               "(name,item_sequence,price,available,veg,description) "
               "VALUES (%s,%s,%s,%s,%s,%s)")
        curr.execute(add_user,tup)
cnx.commit()
curr.close()

# transferring data from beverages csv to beverages tables
curr = cnx.cursor()
with open('Data\\beverages.csv','r') as file_handler:
    csv_reader = csv.reader(file_handler)
    for i in csv_reader: 
        tup = (i[1],i[0],i[2],i[3],i[4],i[5])
        add_user = ("INSERT INTO beverages "
                "(name,item_sequence,price,available,veg,description) "
                "VALUES (%s,%s,%s,%s,%s,%s)")
        curr.execute(add_user,tup)
cnx.commit()
curr.close()

# transferring data from burgers csv to burgers tables
curr = cnx.cursor()
with open('Data\\burgers.csv','r') as file_handler:
    csv_reader = csv.reader(file_handler)
    for i in csv_reader: 
        tup = (i[1],i[0],i[2],i[3],i[4],i[5])
        add_user = ("INSERT INTO burgers "
                "(name,item_sequence,price,available,veg,description) "
                "VALUES (%s,%s,%s,%s,%s,%s)")
        curr.execute(add_user,tup)
cnx.commit()
curr.close()   

# transferring data from hotdogs csv to hotdogs tables
curr = cnx.cursor()
with open('Data\\hotdog.csv','r') as file_handler:
    csv_reader = csv.reader(file_handler)
    for i in csv_reader: 
        tup = (i[1],i[0],i[2],i[3],i[4],i[5])
        add_user = ("INSERT INTO hotdogs "
                "(name,item_sequence,price,available,veg,description) "
                "VALUES (%s,%s,%s,%s,%s,%s)")
        curr.execute(add_user,tup)
cnx.commit()
curr.close()


cnx.close()
