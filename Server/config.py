import os
# file to save database name and MySQL server password

class Config():
    DB_PASS = os.environ.get("DB_PASS")
    database_name = "restaurant"