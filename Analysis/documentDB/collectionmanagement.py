import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client
import pydocumentdb.errors as errors
 
feedoptions = {
    "SSLCertFile":"C:\Users\hauretouze_m\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Azure Cosmos DB Emulator\documentdbemulatorcert.cer"
}
class IDisposable:
    """ A context manager to automatically close an object with a close method
    in a with statement. """

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        # extra cleanup in here
        self = None

class CollectionManagement:
    @staticmethod
    def find_collection(client, id, db_id):
        print('Query for Collection')
        
        collections = list(client.QueryCollections(
            'dbs/' + db_id,
            {
                "query": "SELECT * FROM r WHERE r.id=@id",
                "parameters": [
                    { "name":"@id", "value": id }
                ]
            }
        ))

        if len(collections) > 0:
            print('Collection with id \'{0}\' was found'.format(id))
        else:
            print('No collection with id \'{0}\' was found'. format(id))
        
    @staticmethod
    def create_collection(client, id, db_id):
        try:
            collection = client.CreateCollection('dbs/' + db_id, {"id": id})
            print('Collection with id \'{0}\' created'.format(id))

        except errors.DocumentDBError as e:
            if e.status_code == 409:
               collection = find_collection(client, id, db_id)
            else: 
                raise errors.HTTPFailure(e.status_code)               

        
    @staticmethod
    def read_documents(client, id, db_id):
        
        try:
            # read the collection, so we can get its _self
            collection_link = 'dbs/' + db_id + '/colls/{0}'.format(id)
            collection = client.ReadCollection(collection_link, options = feedoptions)

            # now use its _self to query for Offers
            documents = list(client.QueryOffers('SELECT * FROM c', options = feedoptions))
            
        except errors.DocumentDBError as e:
            if e.status_code == 404:
                print('A collection with id \'{0}\' does not exist'.format(id))
            else: 
                raise errors.HTTPFailure(e.status_code)
                
        if not documents:
            return
        
        return documents

                   
    @staticmethod
    def read_collection(client, id, db_id):
        print("dd")
        try:
            collection_link = 'dbs/' + db_id + '/colls/{0}'.format(id)

            collection = client.ReadCollection(collection_link, feedoptions)
            print("couou")
        except errors.DocumentDBError as e:
            if e.status_code == 404:
               print('A collection with id \'{0}\' does not exist'.format(id))
            else: 
                print(e)
                raise errors.HTTPFailure(e.status_code)
        
        return collection
    
    @staticmethod
    def list_collections(client, db_id):
        
        collections = list(client.ReadCollections('dbs/' + db_id))
        
        if not collections:
            return

        return collections
        
    @staticmethod
    def delete_collection(client, id, db_id):
        print("Delete Collection")
        
        try:
           collection_link = 'dbs/' + db_id + '/colls/{0}'.format(id)
           client.DeleteCollection(collection_link)

           print('Collection with id \'{0}\' was deleted'.format(id))

        except errors.DocumentDBError as e:
            if e.status_code == 404:
               print('A collection with id \'{0}\' does not exist'.format(id))
            else: 
                raise errors.HTTPFailure(e.status_code)   
