# import db
#
# orbis_db = db.DB()
# orbis_db.open()
# orbis_db.get_document_content('i249066098819041307839298364598451988672')
from pymongo import MongoClient
import pprint
from bson import ObjectId
client = MongoClient()
db = client.orbis
corpus = db.corpus
document = db.document
document_annotation = db.document_annotation
annotation = db.annotation
all_corpora = []


#all_corpora = corpus.find()
#print(all_corpora)

#for doc in document.find({"corpus_sname": "education_extraction_corpus"}):
#    pprint.pprint(doc)

for doc in annotation.find({'annotations.d_id': 'i144060182061221316117763556074914515571'}):
    pprint.pprint(doc)
#anot = annotation.find({"da_id": ObjectId("623de0b196f0d234ae863f98")})
#anotb = annotation.find({"annotations": {'d_id': 'i144060182061221316117763556074914515571'}})
#print(anotb)

{'annotations.d_id': 'i249066098819041307839298364598451988672'}