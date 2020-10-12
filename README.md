# Restaurant_Menu

### Inroduction

This is a web application that lists the items of a restaurants menu. 

### Features

- **Sort**: sort items according to the requirements of the restaurant according to the sequence defined by the restaurant.
- **Default Selection:** The first category will be automatically selected and items of that category will be displayed in the onload.
- **Search:** search for items within the category
- **Filter:** filter for veg items only
- **Pagination:** maximum 10 items per page.

### Tech Stack

For the Back End server:

- Python
- Flask
- MySQL

For the Front End:

- HTML
- CSS
- Javascript
- Bootstrap
- Jquery

## Setting up the server

1. Create a database in MySQL server.
2. Update database name and database password in the [config.py](http://config.py) file in the server folder.

```python
#update the following details in the config.py file
class Config():
    DB_PASS = os.environ.get("DB_PASS")
    database_name = "restaurant"
```

3.Activate the virtual environment -"restaurant_env" and set up flask

```bash
#in the windows terminal. change directory to the server folder.
virtualenv name

name\scripts\activate

#once in the virtual environment install the following packages:-
pip install Flask
pip install flask-sqlalchemy
pip install flask-mysqldb
pip install mysql-connector-python
pip install flask-cors
pip install flask-migrate

#set up the server environment
set FLASK_ENV=development
set FLASK_APP=server.py
```

4.Migrate all database models to the MySQL database to create the required tables

```bash
#in the windows terminal inside the virtual environment
flask db init
flask db migrate 
flask db upgrade
```

5.All the data is currently stored in CSV files in the data folder inside the server folder. To transfer data to the from csv to the database run the load_data.py file.

```bash
#in the windows terminal inside the virtual environment
load_data.py
```

6.Once data is loaded, run the server.

```bash
#in the windows terminal inside the virtual environment
flask run
```

7.open the index.html file in the browser. you should see something like this.

![Restaurant%20Menu%20aad6b85b25644dee93559815ac0e77a3/restaurant_menu_snapshot.png](Restaurant%20Menu%20aad6b85b25644dee93559815ac0e77a3/restaurant_menu_snapshot.png)