import csv
import json
import sys
 
import logging
logging.basicConfig(level=logging.INFO)
 
from rdflib import Graph, URIRef, Namespace
from rdflib_jsonld.parser import to_rdf
#from utils import ns_mgr, DATA_NAMESPACE
 
D = Namespace('http://vivo.school.edu/individual/')
 
import uuid
 
def uuid_uri(prefix='n'):
	return D[str(prefix) + str(uuid.uuid4())]
 
#Data namespace
ns = "http://vivo.school.edu/individual/"
 
org_ctx = {
	"@context": {
        "@base": D,
        "a": "@type",
        "uri": "@id",
        "foaf": "http://xmlns.com/foaf/0.1/",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "vcard": "http://www.w3.org/2006/vcard/ns#",
        "label": "rdfs:label",
        "vco": {
        	"@id": "vcard:Organization",
        	"@type": "@id"
        }
    }
}
 
 
 
orgs = []
 
with open(sys.argv[1]) as infile:
	for row in csv.DictReader(infile):
		print row
		#tax_id = row.get('EIN')

		#print "tax_id: " + str(tax_id)
		d = {}
		d['uri'] = uuid_uri()
		
		d['label'] = row.get('NAME')
		print "NAME: " + str(d['label'])
		d['a'] = 'foaf:Organization'
		d.update(org_ctx)
		vco = uuid_uri()
 
		vcard_address = {}
		vcard_address['uri'] = uuid_uri()
		#vco['vcard:hasAddress'] = vcard_address
 
		d['vco'] = vco
 
 
 
		orgs.append(d)
 
print orgs
 
 
g = Graph()
out = to_rdf(orgs, g)
#out.namespace_manager = ns_mgr
print out.serialize(format='turtle')