import argparse 
import os
import json
import re

def main(): 
    # Parser utama untuk command line
    parser = argparse.ArgumentParser(usage="mytool positional [-optional1 OPTIONAL1] [-optional2 OPTIONAL2]")
    parser.add_argument('inputfile', type=str, help='Source file path.', action='store')
    parser.add_argument('-t', type=str, dest='format', help="Format to convert (either 'json' or 'text') with plaintext default.", action='store', default='text') 
    parser.add_argument('-o', type=str, dest='destination', help='Destination file path. If not provided, a new file with similar name is created.', action='store') 
    args = parser.parse_args()
    handleFile(args.inputfile, args.destination, args.format)

def handleFile(source, destination, format):
    # Verifikasi format termasuk format yang diperbolehkan
    if (format != "text") and (format != "json"):
        print("Error in format choice, choose either json or text.")
    # Verifikasi file source ada
    checkexists = os.path.isfile(source)
    if not checkexists:
        print("Error in input file, file does not exist.")
    else:
        form = ".txt" if (format == "text") else ".json"
        dest = destination if destination is not None else os.path.splitext(source)[0].lower() + form
        # Verifikasi ekstensi file destinasi
        if not (dest.lower().endswith(form)):
            print("Error with destination file extension, please name according to the intended format.")
        else:
            if (format == "text"):
                copyTextFile(source, dest)
            else:
                copyJSONFile(source, dest)

def copyTextFile(source, destination):
    # Konversi ke .txt
    with open(source,'r') as firstfile, open(destination,'w') as secondfile:
        for line in firstfile:
            secondfile.write(line)

def copyJSONFile(source, destination):
    # Konversi ke .json
    i = 1
    result = {}
    with open(source,'r') as firstfile, open(destination,'w') as secondfile:
        lines = firstfile.readlines()
        for line in lines:
            result[i] = line
            i += 1
        json.dump(result, secondfile)