#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Create a parser for command line arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')

# Add arguments for sequence and motif
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# If no arguments are provided, print help and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the command line arguments
args = parser.parse_args()

# Convert the sequence to uppercase
args.seq = args.seq.upper()

# Check if the sequence is valid (only contains ACGTU)
if re.search('^[ACGTU]+$', args.seq):
    # If the sequence contains T, it's DNA
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    # If the sequence contains U, it's RNA
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    # If the sequence contains neither T nor U, it could be either DNA or RNA
    else:
        print ('The sequence can be DNA or RNA')
# If the sequence is not valid, print an error message
else:
    print ('Invalid sequence source')

# If a motif is provided, search for it in the sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    # If the motif is found in the sequence, print a success message
    if re.search(args.motif, args.seq):
        print("HERE are a motif")
    # If the motif is not found, print an error message
    else:
        print("SORRY BUT NO MOTIF FOUND")
