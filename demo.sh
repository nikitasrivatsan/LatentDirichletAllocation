#!/bin/bash

# Usage: ./demo.sh <K>

echo "Retrieving information\n"
./grab_info.py
echo "Running LDA\n"
./run-LDA.sh bios output $1 0.1 0.01 1100 1000
echo "Printing results\n"
./analyze.py output
