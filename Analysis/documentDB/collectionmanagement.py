import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client
import pydocumentdb.errors as errors

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
    def read_collection(client, id, db_id):
        
        try:
            # read the collection, so we can get its _self
            collection_link = 'dbs/' + db_id + '/colls/{0}'.format(id)
            collection = client.ReadCollection(collection_link)

            # now use its _self to query for Offers
            offer = list(client.QueryOffers('SELECT * FROM c WHERE c.resource = \'{0}\''.format(collection['_self'])))[0]
            
            print('Found Offer \'{0}\' for Collection \'{1}\' and its offerType is \'{2}\''.format(offer['id'], collection['_self'], offer['offerType']))

        except errors.DocumentDBError as e:
            if e.status_code == 404:
                print('A collection with id \'{0}\' does not exist'.format(id))
            else: 
                raise errors.HTTPFailure(e.status_code)

        offer['offerType'] = 'S2'
        offer = client.ReplaceOffer(offer['_self'], offer)
        
        
                                
    @staticmethod
    def read_collection(client, id, db_id):

        try:
            collection_link = 'dbs/' + db_id + '/colls/{0}'.format(id)

            collection = client.ReadCollection(collection_link)
            

        except errors.DocumentDBError as e:
            if e.status_code == 404:
               print('A collection with id \'{0}\' does not exist'.format(id))
            else: 
                raise errors.HTTPFailure(e.status_code)
        
        return collection
    
    @staticmethod
    def list_collections(client, db_id):
        
        collections = list(client.ReadCollections('dbs/' + db_id))
        
        if not collections:
            return

        for collection in collections:
            print(collection['id'])
        
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

def run_sample():

    with IDisposable(document_client.DocumentClient(HOST, {'masterKey': MASTER_KEY} )) as client:
        try:
            try:
                client.CreateDatabase({"id": DATABASE_ID})
            
            except errors.DocumentDBError as e:
                if e.status_code == 409:
                   pass
                else: 
                    raise errors.HTTPFailure(e.status_code)
            
            try:
                client.DeleteDatabase('dbs/' + db_id)
            
            except errors.DocumentDBError as e:
                if e.status_code == 404:
                   pass
                else: 
                    raise errors.HTTPFailure(e.status_code)

        except errors.HTTPFailure as e:
            print('\nrun_sample has caught an error. {0}'.format(e.message))
        
        finally:
            print("\nrun_sample done")