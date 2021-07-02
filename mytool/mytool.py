import argparse 
import os
import json

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile', type=str, help='Source file path.', action='store')
    parser.add_argument('-t', type=str, dest='format', help="Format to convert (either 'json' or 'text') with plaintext default.", action='store', default='text') 
    parser.add_argument('-o', type=str, dest='destination', help='Destination file path. If not provided, a new file with similar name is created', action='store') 
    args = parser.parse_args()
    handleFile(args.inputfile, args.destination, args.format)

def handleFile(source, destination, format):
    if (format != "text") and (format != "json"):
        print("Error in format choice, choose either json or text.")
    checktype = os.path.splitext(source)[-1].lower()
    if (checktype != ".log"):
        print("Error in input file extension, only .log files are allowed.")
    else:
        form = ".txt" if (format == "text") else ".json"
        dest = destination if destination is not None else source + form
        if not (dest.lower().endswith(form)):
            print("Error with destination file extension, please name according to the intended format.")
        else:
            if (format == "text"):
                copyTextFile(source, dest)
            else:
                copyJSONFile(source, dest)

def copyTextFile(source, destination):
    with open(source,'r') as firstfile, open(destination,'w') as secondfile:
        for line in firstfile:
            secondfile.write(line)

def copyJSONFile(source, destination):
    i = 1
    result = {}
    with open(source,'r') as firstfile, open(destination,'w') as secondfile:
        lines = firstfile.readlines()
        for line in lines:
            result[i] = line
            i += 1
        json.dump(result, secondfile)