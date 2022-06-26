from flask import Flask, redirect
from flask import render_template
from flask import request
from collections import defaultdict
from pymongo import MongoClient
import pprint
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

    return render_template("viewer.html", corpus=corpus)


@app.route('/show_documents/<corpus_name>')
def show_documents(corpus_name):
    # Read the list of documents from the selected corpus
    # Display all the documents
    # let user select a document
    return render_template("show_documents.html", corpus_name=corpus_name, document=document, title=f"Documents in Corpus {corpus_name}")


@app.route('/view_document/<corpus_name>/<document_no>/<document_id>')
def view_document(corpus_name,document_id,document_no):
    # read the document contents of the selected document
    # display the content
    # navigation: back/prev-doc/next-doc
    document_content = document.find_one({"id": document_id})
    return render_template("view_document.html", document_no=document_no, document_content=document_content, corpus_name=corpus_name, document=document, document_id=document_id, title=f"View Document #{document_no}")


@app.route('/show_annotations')
def show_annotations():
    # Read the list of annotations from the selected corpus
    # Display all the documents
    # let user select a document
    return render_template("show_annotations.html")

@app.route('/annotation_view')
def annotation_view():
    # read the contents of the slected annotation
    # display the content
    # navigation: back/prev-doc/next-doc
    return render_template("annotation_view.html")

# run app (debug mode)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
