import argparse
import json
import sys
from os import path


def init_params():
    parser = argparse.ArgumentParser(description='Process input path parameter')
    parser.add_argument('-i', '--input_file', default=sys.stdin, help='Input from file, default stdin')  # all blocks
    parser.add_argument('-o', '--output_file', default=sys.stdout, help='Output to file, default stdout')  # all blocks
    parser.add_argument('-p', '--path', help='Reuters collection directory')  # block 1
    parser.add_argument('-s', '--stopwords', default=None, help='Stopword list from file')  # block 6
    parser.add_argument('-t', '--query_type', default=None, choices=['AND', 'OR'], help='Query type to run')  # block 8
    parser.add_argument('-q', '--query', nargs='*', default=None, help='Query')  # block 8
    init_params.args = parser.parse_args()

    if type(init_params.args.input_file) is str:
        common_check_path(init_params.args.input_file)
        init_params.args.input_file = open(init_params.args.input_file)

    if type(init_params.args.output_file) is str:
        init_params.args.output_file = open(init_params.args.output_file, 'w')

    if type(init_params.args.stopwords) is str:
        common_check_path(init_params.args.stopwords)
        init_params.args.stopwords = open(init_params.args.stopwords)

    return init_params.args


def common_check_path(file):
    assert path.exists(file), "input file does not exists"


def output(structure):
    print(json.dumps(structure), file=init_params.args.output_file)


def block_1_reader_validate(reuters_files_content):
    assert type(reuters_files_content) is str, "Expected the elements in the list to be of type String"
    assert len(reuters_files_content), "List elements are empty"
    assert reuters_files_content.strip().startswith('<!DOCTYPE'), "sgm file content expected"


def block_2_document_segmenter_validate(document):
    assert type(document) is str, "Expected the elements in the list to be of type String"
    assert len(document), "List elements are empty"
    assert document.strip().startswith('<REUTERS'), "Elements in the list should start with tag <REUTERS>"
    assert document.strip().endswith('</REUTERS>'), "Elements in the list should end with tag </REUTERS>"


def block_3_extractor_validate(content_item):
    assert type(content_item) is dict, "Elements in the list should be of python dictionary data structure"
    assert len(content_item.keys()) == 2, "Dictionary should consist of 2 keys, ID and TEXT"
    assert 'ID' in content_item.keys(), "...no key ID in dictionary"
    assert 'TEXT' in content_item.keys(), "...no key TEXT dictionary"


def block_4_tokenizer_validate(post):
    assert type(post) in [list, tuple], "Elements in the list should be a list or a tuple"
    assert len(post) == 2, "List should consist of 2 elements"

def block_5_stemmer_validate(token):
    assert type(token) in [list, tuple], "Elements in the list should be a list or a tuple"
    assert len(token) == 2, "List should consist of 2 elements"


def block_6_stopwords_removal_validate(token):
    assert type(token) in [list, tuple], "Elements in the list should be a list or a tuple"
    assert len(token) == 2, "List should consist of 2 elements"
