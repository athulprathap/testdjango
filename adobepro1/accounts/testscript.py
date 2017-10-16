from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch_dsl import Search, Q
# use certifi for CA certificates
import certifi
import requests
from datetime import datetime
from pprint import pprint
import pdb
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

class es_class():
    def __init__(self, server, user, passw):
        self.server = "https://476b88cf7673e52be40c536ef8ff2ff3.us-east-1.aws.found.io:9243/"
        self.user = "elastic"
        self.passw = "testdjango123$"



    def connect(self):
        #res = requests.get("https://476b88cf7673e52be40c536ef8ff2ff3.us-east-1.aws.found.io:9243/")
        #print(res)
        #return res
    # connect to our cluster
        es = Elasticsearch([{'host': '476b88cf7673e52be40c536ef8ff2ff3.us-east-1.aws.found.io', 'port': 9243}])
        res = es.index(index='adobe-index', doc_type='test11', id=1, body={'test': 'success'})
        return res