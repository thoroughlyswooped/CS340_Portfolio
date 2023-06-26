from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER =  username
        PASS =  password
        HOST = '127.0.0.1'
        PORT =27017
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        

# Method to create document in database
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  # data should be dictionary   
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Method to remove document in database
    def remove(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count;
        else:
            raise Exception("Nothing to remove, becuase query parameter is empty")
            return 0;
# Method to read document in database 
    def read(self, query):
        if query is not None:
            result = self.collection.find(query)
            return list(result)
        else:
            raise Exception("Nothing to read, becuase query parameter is empty")
            return []
# Method to update document in database
    def update(self, query, values):
        if (query is not None) and (values is not None):
            result = self.collection.update_many(query, values)
            return result.modified_count
        else:
            raise Exception("Nothing to read, becuase query parameter or values paramter is empty")
            return 0


shelter = AnimalShelter('aacuser', 'password123')
print(shelter.read({}))
