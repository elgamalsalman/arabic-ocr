# ----- IMPORTS -----

import os
import sys
import random

# ----- GLOBALS -----

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ALPHABET = [
    '\u0627', '\u0628', '\u062A', '\u062B', '\u062C', '\u062D', '\u062E', '\u062F', '\u0630', '\u0631', '\u0632',
    '\u0633', '\u0634', '\u0635', '\u0636', '\u0637', '\u0638', '\u0639', '\u063A', '\u0641', '\u0642', '\u0643',
    '\u0644', '\u0645', '\u0646', '\u0647', '\u0648', '\u064A', '\u0621', '\u0623', '\u0624', '\u0625', '\u0626',
    '\u0649'
]
ALPHABET_SIZE = len(ALPHABET)

# ----- HELPER FUNCTIONS -----

# ----- MAIN PROGRAM -----

def main():
    # check for correct number of arguments
    if len(sys.argv) < 3:
        print("ARGUMENTS: <input_file> <output_file>")
        return

    # get the arguments
    input_file = open(sys.argv[1], "r")
    output_file = open(sys.argv[2], "w")

    # extract text
    input_text = input_file.read()
    
    # for
    word = ""
    for char in input_text:
        # if arabic letter
        if char in ALPHABET:
            word += char
        # if anything else
        else:
            # write current word if not empty
            if word != "":
                output_file.write(word + '\n')
            word = ""

    input_file.close()
    output_file.close()

if __name__ == "__main__":
    main()
