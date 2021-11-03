#!/usr/bin/env python

""" BLOCK 5
Objective: Stemming tokens using NLTK library functionality

Fill in your code within the 'WRITE YOUR CODE HERE' stub in function "block_stemmer" in solutions.py file. Do not
attempt to modify any code in this file as they might affect your grading.

Input: Individual tuple containing an ID (corresponding to document ID) and a token (Output from block-4-tokenizer.py)
Output: Should yield a tuple containing an ID(document ID) and stemmed token during every iteration.
        Number of iteration in the loop created for you should be equal to the number of Tokens returned by your previous
        implementation.

Sample output structure: [1, "this"]
                         [1, "is"]
                         [1, "text"]
                         [1, "play"] ....

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
for stemmed_token in solutions.block_stemmer((json.loads(line) for line in args.input_file)):
    # Validating output format
    asserts.block_5_stemmer_validate(stemmed_token)
    # Write results to stdout or file
    asserts.output(stemmed_token)
