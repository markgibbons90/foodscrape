import ConfigParser
import MySQLdb

# Get the MySQL password
config = ConfigParser.ConfigParser()
config.read('settings.ini')
db_pass = config.get('Database', 'mysql_root_password')

# Connect to db
db = MySQLdb.connect('localhost', 'root', db_pass)
cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute('CREATE DATABASE IF NOT EXISTS foodscrape')
