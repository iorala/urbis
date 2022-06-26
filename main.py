from flask import Flask, redirect
from flask import render_template
from flask import request
from collections import defaultdict
from pymongo import MongoClient
import pprint

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
    #
    return render_template("viewer.html")


@app.route('/show_documents/<corpus_name>')
def show_documents(corpus_name):
    # Read the list of documents from the selected corpus
    # Display all the documents
    # let user select a document
    return render_template("show_documents.html", title=f"Documents in Corpus {corpus_name}")


@app.route('/document_view')
def document_view():
    # read the document contents of the selected document
    # display the content
    # navigation: back/prev-doc/next-doc
    return render_template("document_view.html")


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
