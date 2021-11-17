#!/usr/bin/env python
"""BLOCK 1
Objective: Is to make sure you read the .sgm files from the Reuters collection.
        Do not attempt to perform any cleaning or extraction from the file content in this block. A simple read of
        individual files iteratively is suffice to satisfy the objectives of this block.

Fill in your code within the 'WRITE YOUR CODE HERE' stub in function "block_reader" in solutions.py file. Do not attempt
to modify any code in this file as they might affect your grading.

Input: Reuters Folder path (which you downloaded from Moodle). Path to the folder should be passed in as a parameter when
        calling this block for execution. See README.txt to see how to execute each block.
Output: Individual .sgm file content as a string returned iteratively. Number of iteration in the loop created for you
        should be equal to the number of files in the Reuters folder. i.e. Each element yielded should correspond
         to each .sgm file in the folder.

Marking criteria:
    - The content of the output variable: structure, type and size
"""

import asserts
import functions

## Read command line arguments
args = asserts.init_params()
## Set necessary variables. This variable contains the path to the Reuters folder passed in as a parameter when calling
## this python script for execution
path = args.path
path = "C:\\Users\\matth\\Documents\\workspace\\python\\bonAppetitScraper\\recipe-generator\\pipeline"
## Check pre-conditions
# asserts.common_check_path(path)

## Calling your solution. Execute your solution in the following method in solutions.py file
for reuters_file_content in functions.block_reader(path):
    ## Validating output format
    # asserts.block_1_reader_validate(reuters_file_content)
    ## Write results to stdout or file
    asserts.output(reuters_file_content.to_json())
    

# functions.block_reader(path)
print("Block 1 Complete")


