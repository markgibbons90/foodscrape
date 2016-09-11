import ConfigParser
import MySQLdb
import peewee as pw

class BaseModel(pw.Model):
    """
    Base model class which specifies the database. All models extend this class.
    """
    class Meta:
        # Set the database.
        # @TODO: This is kind of messy at the moment. Clean up
        config = ConfigParser.ConfigParser()
        config.read('settings.ini')
        db_pass = config.get('Database', 'mysql_root_password')
        db = pw.MySQLDatabase('foodscrape', user='root', host='localhost', password=db_pass)
        database = db

class Restaurant(BaseModel):
    """
    Restaurant model
    """
    name = pw.CharField()
    url = pw.CharField()

def get_mysql_password():
    """
    Get the MySQL password
    """
    config = ConfigParser.ConfigParser()
    config.read('settings.ini')
    db_pass = config.get('Database', 'mysql_root_password')

    return db_pass

def create_database():
    """
    Create the database if it doesn't already exist
    """
    # Get the mysql password
    db_pass = get_mysql_password()

    # Connect to mysql
    db = MySQLdb.connect('localhost', 'root', db_pass)
    cursor = db.cursor()

    # Create the database if it doesn't exist
    cursor.execute('CREATE DATABASE IF NOT EXISTS foodscrape')

def drop_database():
    """
    Drop the database
    """
    # Get the mysql password
    db_pass = get_mysql_password()

    # Connect to mysql
    db = MySQLdb.connect('localhost', 'root', db_pass)
    cursor = db.cursor()

    # Drop the database
    cursor.execute('DROP DATABASE IF EXISTS foodscrape')

def create_tables():
    """
    Create the database tables
    """
    # Get the mysql password
    db_pass = get_mysql_password()

    # Connect to the database if it exists
    db = pw.MySQLDatabase('foodscrape', user='root', host='localhost', password=db_pass)
    db.connect()

    # Create the table(s)
    db.create_tables([Restaurant])
