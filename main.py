from flask import Flask, redirect
from flask import render_template
from flask import request
from collections import defaultdict
from pymongo import MongoClient
import pprint
from bson import ObjectId
client = MongoClient()
db = client.orbis
corpus = db.corpus
document = db.document
document_annotation = db.document_annotation
annotation = db.annotation


app = Flask("urbis")


@app.route('/')
def home():
    ## show a menu of funtions
    #
    return render_template("index.html", title="Urbis Prototype")


@app.route('/viewer')
def viewer():
    # Read list of corpora from mongodb
    # display
    # let user select a corpus - for each corpus the user has three links
    # - show_documents
    # - Show Document-Annotations
    # - show EvaluationsRuns

    return render_template("viewer.html", corpus=corpus, title="Urbis - Document Viewer")


@app.route('/show_documents/<corpus_name>')
def show_documents(corpus_name):
    # Read the list of documents from the selected corpus
    # Display all the documents
    # let user select a document
    return render_template("show_documents.html", corpus_name=corpus_name, document=document, title=f"Urbis - Documents in Corpus {corpus_name}")


@app.route('/view_document/<corpus_name>/<document_no>/<document_id>')
def view_document(corpus_name,document_id,document_no):
    # read the document contents of the selected document
    # display the content
    # navigation: back/prev-doc/next-doc
    document_content = document.find_one({"id": document_id})['content']
    document_content = document_content.replace("\n\n", "\n")
    document_content = document_content.replace("\n\n", "\n")
    document_content = document_content.replace("\n", "<br>")
    return render_template("view_document.html", document_no=document_no, document_content=document_content, corpus_name=corpus_name, document=document, document_id=document_id, title=f"Urbis - View Document #{document_no}")


@app.route('/show_annotations/<corpus_name>/<document_no>/<document_id>')
def show_annotations(corpus_name,document_id,document_no):
    # Read the list of annotations for the selected Documents
    # Display all the documents
    # let user select a document

    return render_template("show_annotations.html",document_id=document_id, document_no=document_no, corpus_name=corpus_name, annotation=annotation, title=f"Urbis - Show Annotations for Document #{document_no}")

@app.route('/view_annotation/<corpus_name>/<document_no>/<document_id>/<annotation_id>')
def view_annotation(corpus_name,document_id,document_no,annotation_id):
    # read the contents of the selected annotation
    # display the content
    # navigation: back/prev-doc/next-doc
    start_tag = "<div class='anot'>"
    end_tag = "</div>"
    document_content = document.find_one({"id": document_id})['content']

    for doc in annotation.find({'_id': ObjectId(annotation_id)}):
        doc_annotations = doc['annotations']

    anot_tuples = []
    for anot in doc_annotations['annotations']:
        anot_tuples.append((anot['start'], anot['end'], anot['type'], anot['surface_form'], anot['key']))

    output = ""
    start_char = 0
    anot_tuples = sorted(anot_tuples)
    for anot in anot_tuples:
        output += document_content[start_char:anot[0]]
        output += start_tag
        output += document_content[anot[0]:anot[1]]
        output += end_tag
        start_char = anot[1]
    output = output.replace("\n\n", "\n")
    output = output.replace("\n\n", "\n")
    output = output.replace("\n", "<br>")

    return render_template("view_annotation.html", anot_tuples=anot_tuples, output=output, annotation_id=annotation_id, document_no=document_no, corpus_name=corpus_name, document=document, document_id=document_id, title=f"Urbis - View Annotation #{annotation_id}")

# run app (debug mode)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
