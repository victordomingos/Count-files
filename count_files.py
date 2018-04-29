#!/usr/bin/env python3
import os
import argparse

from pprint import pprint


parser = argparse.ArgumentParser(description='\nRecursively count all files in a directory, by file extension.')

parser.add_argument('path',
                    type=str,
                    help='The path to the folder containing the files to be counted.')

parser.add_argument('-nr',
                    action='store_true',
                    help="Don't recurse through subdirectories")

args = parser.parse_args()

filecount = dict()


if args.path:
    location = os.path.expanduser(args.path)
    loc_text = ':\n' + location
else:
    location = os.getcwd()
    loc_text = ' current directory'
    
if args.nr:
    recursive = False
    msg = f'\nCounting files in{loc_text}.\n'
    print(msg)
    
    for f in os.listdir(location):
        filename_parts = f.split('.')
        if len(filename_parts) == 1:
            extension = '[no extension]'
        else:
            extension = filename_parts[-1]
            
        if extension in filecount.keys():
            filecount[extension] += 1
        else:
            filecount[extension] = 1
            
else:
    recursive = True
    msg = f'Recursively counting all files in:\n{loc_text}.\n'
    print(msg)
    
    for root, dirs, files in os.walk(location):
        for f in files:
            filename_parts = f.split('.')
            if len(filename_parts) == 1:
                extension = '[no extension]'
            else:
                extension = filename_parts[-1]
                
            if extension in filecount.keys():
                filecount[extension] += 1
            else:
                filecount[extension] = 1
        
pprint(filecount)
