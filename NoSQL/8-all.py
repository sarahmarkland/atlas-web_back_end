#!/usr/bin/env python3
""" task 8 - use the PyMongo library to interact with MongoDB from Python """


def list_all(mongo_collection):
    """ list all documents in a collection"""
    cursor = mongo_collection.find({})

    all_documents = []

    for document in cursor:
        all_documents.append(document)
    
    return all_documents
