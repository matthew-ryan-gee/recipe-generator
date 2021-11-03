#!/usr/bin/env python
""" BLOCK 6
Objective: Remove stopwords from the corpus

Fill in your code within the 'WRITE YOUR CODE HERE' stub in function "block_stopwords_removal" in solutions.py file. Do
not attempt to modify any code in this file as they might affect your grading.

Input: Individual tuple containing an ID (corresponding to document ID) and a token (Output from block-4-stemmer.py),
        Optional: Path to a stopwords list file.
Output: Should yield a tuple containing an ID(document ID) and stemmed token which is not a stopword during every iteration.
        Number of iteration in the loop created for you should be equal to the number of tokens returned by your previous
        implementation.

Sample output structure: [1, "text"]
                         [1, "play"]....

Marking criteria:
     - The content of the output variable: structure and type
"""
import argparse
import json
import asserts
import solutions

parser = argparse.ArgumentParser(description='Process input path parameter')
args = asserts.init_params()

# Check Optional parameter stopwords list.
#  If a stopword list passed in when calling this block, read the content of the file in the path specified.
stopwords = None
if args.stopwords is not None:
    stopwords = args.stopwords.read()

for token in solutions.block_stopwords_removal((json.loads(line) for line in args.input_file), stopwords):
    # Validating output format
    asserts.block_6_stopwords_removal_validate(token)
    # Write results to stdout or file
    asserts.output(token)


