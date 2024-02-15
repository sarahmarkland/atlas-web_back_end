#!/usr/bin/env python3
""" task 11 - python module """


def schools_by_topic(mongo_collection, topic):
    """ function that returns the list of school having a specific topic """
    cursor = mongo_collection.find({"topics": topic})

    all_documents = []

    for document in cursor:
        all_documents.append(document)

    return all_documents
