#!/usr/bin/env python

""" BLOCK 4
Objective: Split a long text into tokens using NLTK library functionality

Fill in your code within the 'WRITE YOUR CODE HERE' stub in function "block_tokenizer" in solutions.py file. Do not
attempt to modify any code in this file as they might affect your grading.

Input: Individual Python dictionaries containing an ID (corresponding to document ID) and TEXT (corresponding to the text
        extracted from each news documents). (Output from block-3-extractor.py)
Output: Should yield a tuple containing an ID(document ID) and token (from the tokenized string) during every iteration.
        Number of iteration in the loop created for you should be equal to the number of documents inside the corpus.

Sample output structure: [1, "This"]
                         [1, "is"]
                         [1, "text"]
                         [1, "playing"] .....

Marking criteria:
     - The content of the output variable: structure and type
"""

import argparse
import json
import asserts
import solutions

parser = argparse.ArgumentParser(description='Process input path parameter')
args = asserts.init_params()

# Calling your solution. Execute your solution in the following method in solutions.py file
for post in solutions.block_tokenizer((line) for line in args.input_file):
    # # Validating output format
    # asserts.block_4_tokenizer_validate(post)
    # # Write results to stdout or file
    asserts.output(post)
