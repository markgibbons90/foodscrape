import ConfigParser
import MySQLdb
import peewee as pw

# Get the MySQL password
config = ConfigParser.ConfigParser()
config.read('settings.ini')
db_pass = config.get('Database', 'mysql_root_password')

print db_pass

# Set the database instance
db = pw.MySQLDatabase('foodscrape', user='root', host='localhost', password=db_pass)

class BaseModel(pw.Model):
    """
    Base model class which specifies the database. All models extend this class.
    """
    class Meta:
        database = db

class Restaurant(BaseModel):
    """
    Restaurant model
    """
    name = pw.CharField()
    url = pw.CharField()

def create_tables():
    """
    Create the database tables
    """
    db.connect()
    db.create_tables([Restaurant])
