# import db
#
# orbis_db = db.DB()
# orbis_db.open()
# orbis_db.get_document_content('i249066098819041307839298364598451988672')
from pymongo import MongoClient
import pprint
client = MongoClient()
db = client.orbis
corpus = db.corpus
document = db.document
document_annotation = db.document_annotation
annotation = db.annotation
all_corpora = []
for doc in corpus.find():
    pprint.pprint(doc)

all_corpora = corpus.find()
print(all_corpora)

for doc in document.find({"corpus_sname": "education_extraction_corpus"}):
    pprint.pprint(doc)

#for doc in annotation.find():
#    pprint.pprint(doc)
