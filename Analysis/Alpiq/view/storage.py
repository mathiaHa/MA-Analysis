import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client
import pydocumentdb.errors as errors

feedoptions = {
    'SSLCertFile':'C:\Users\hauretouze_m\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Azure Cosmos DB Emulator\documentdbemulatorcert.cer'
}

def Reader(db_id, coll_id, doc_query, storage_id):
	# Initialization
	docs = None
    
	try:
		client = document_client.DocumentClient(storage_id.host, {'masterKey': storage_id.master_key})
		db_query = "select * from r where r.id = '{0}'".format(db_id)
		db = list(client.QueryDatabases(db_query, options = feedoptions))[0]
		db_link = db['_self']
        
		coll_query = "select * from r where r.id = '{0}'".format(coll_id)
		coll = list(client.QueryCollections(db_link, coll_query, options = feedoptions))
		coll_link = coll[0]['_self']
        
		docs = list(client.QueryDocuments(coll_link, doc_query, options = feedoptions))
        
	except errors.DocumentDBError as e:
		if e.status_code == 404:
			print e
			raise
		else:
			raise
	except Exception as e:
		raise
	finally:
		if docs is not None:
			return docs
		else:
			return None
        
def GetDataBaseLink(client, db_id):
	db_query = "select * from r where r.id = '{0}'".format(db_id)
	db = list(client.QueryDatabases(db_query, options = feedoptions))[0]
	return db['_self']

def GetCollectionLink(client, db_id, coll_id):
	db_link = GetDataBaseLink(client, db_id)
	coll_query = "select * from r where r.id = '{0}'".format(coll_id)
	coll = list(client.QueryCollections(db_link, coll_query, options = feedoptions))
	return coll[0]['_self']

def ReaderbyResourceNames(db_id, coll_id, storage_id, res_names):
	# Initialization
	data = {}
	dividers = {}
	
	for res_name in res_names:
		
		doc_query = "select * from c where c.resourcename = '{0}'".format(res_name)
		
		docs = st.Reader(db_id, coll_id, doc_query, storage_id)
		
		if not len(docs) == 0:
			df = pd.DataFrame([item for doc in docs for item in doc["data"]])
			data[res_name] = df
			
			dividers[res_name] = getattr(cfg.groups, docs[0]["apiname"])
 	return data, dividers