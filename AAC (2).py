from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
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
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32973
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            result = self.collection.insert_one(data) # trys to insert the data
            return True if result.inserted_id else False # if data is inserted shows true and false if it doesnt
        except Exception as E:# handels the exception and ties it to varible E
            print("Nothing to save, because data parameter is empty") # if we cant insert data prints this 
            return False # if it cant complete this section it will return false

# Create method to implement the R in CRUD.
    def read(self, query):
        try:
            cursor = self.collection.find(query) # shows is the data with the query we searched 
            return list (cursor) # makes the cursor to a list of items
        except Exception as E: # handels the exception and ties it to varible E
            print("no query found") # if no items found prints this
            return [] # returns the query or prints the statement 
    def update(self, query, new_data):
        try:
            result = self.collection.update_many(query,{'$set':new_data})# updates the data where the $set is the colum we want to update with new data
            return result.modified_count# returns a number of things that were updated
        except Exception as E:# handels the exception and ties it to varible E
            print("can not update error")# if we cant update outputs this
            return 0
            
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)# deletes everything tied to the query we input
            return result.deleted_count# shows us how many thing  were deleted 
        except Exception as E:# handels the exception and ties it to varible E
            print("can not delete error")# if we cant delete a query outputs this
            return 0   
