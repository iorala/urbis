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
annotation_id = "623de0b196f0d234ae863f99"
document_id = "i249066098819041307839298364598451988672"
start_tag = "<div class='p-3 mb-2 bg-info text-dark'>"
end_tag = "</div>"

document_content = document.find_one({"id": document_id})['content']
#doc_annotations = document.find_one({'_id': ObjectId(annotation_id)})

for doc in annotation.find({'_id': ObjectId(annotation_id)}):
    doc_annotations = doc['annotations']



anot_tuples = []
for anot in doc_annotations['annotations']:
    anot_tuples.append((anot['start'],anot['end'],anot['type'],anot['surface_form']))


output = ""
start_char = 0

for anot in sorted(anot_tuples):
    output += document_content[start_char:anot[0]]
    output += start_tag
    output += document_content[anot[0]:anot[1]]
    output += end_tag
    start_char= anot[1]


print(output.replace("\n", "<br>"))


#pprint.pp(doc_annotations)



