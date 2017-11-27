import os
import json
from glob import glob
import progressbar

# path to the datasets
BASE_PATH ='../dataset'

def get_subfolders(path):
    """get all subfolders """
    return [x[0] for x in os.walk(path)][1:]

def collect_json(path):
    """concatenate all json files"""
    subfolder_list = get_subfolders(BASE_PATH + "/" + path)
    
    documents = []
    
    with progressbar.ProgressBar(max_value=len(subfolder_list)) as bar:        
        for i,sub in enumerate(subfolder_list):
            pattern = os.path.join(sub, '*.json')
            for file_name in glob(pattern):
                with open(file_name) as json_data:
                    temp_data = json.load(json_data)
                    temp_doc = temp_data['response']['docs']
                    documents += temp_doc
            bar.update(i)

    return documents

def get_all_json():

    # only forlder containing data
    folders = next(os.walk(BASE_PATH))[1]

    # get all json files from the folder
    documents = collect_json(folders[0])

    number_documents = len(documents)

    # check all primary keys in documents
    full_keys_names = set()
    for doc in documents:
        full_keys_names |= set(list(doc.keys()))

    # return number of documents, list of keys, list of documents
    return number_documents, full_keys_names, documents