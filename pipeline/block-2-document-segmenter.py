#!/usr/bin/env python

""" BLOCK 2
Objective: To make sure you look into the corpus provided and decide the scope of each news document. Split each .sgm
            file content into a number of news documents based on the characteristic you observe in the corpus provided.
            Do not attempt to perform any cleaning or extraction from the file content in this block. A simple split of
            documents would be suffice to satisfy the objective of this block.

Fill in your code within the 'WRITE YOUR CODE HERE' stub in function "block_document_segmenter" in solutions.py file. Do not attempt
to modify any code in this file as they might affect your grading.

Input: Individual .sgm file content (Output from Block-1-reader.py)
Output: Individual news documents. Each element yielded should correspond to a news document within the input .sgm file.
        Number of iteration in the loop created for you should be equal to the number of documents inside the corpus.

Marking criteria:
     - The content of the output variable: structure, type and size
"""
import json
import asserts
import solutions

args = asserts.init_params()

# Calling your solution. Execute your solution in the following method in solutions.py file
for document in solutions.block_document_segmenter((json.loads(line) for line in args.input_file)):
    # # Validating output format
    # asserts.block_2_document_segmenter_validate(document)
    # # Write results to stdout or file
    # asserts.output(document)