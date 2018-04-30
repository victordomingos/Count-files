#!/usr/bin/env python3
# encoding: utf-8
"""
A little CLI utility written in Python to help you count files, grouped by
extension, in a directory. You can either pass it the path to the directory to
scan, or leave that argument empty and it will scan the current working
directory. The -nr (i.e., "no recursion") switch tells the application not to
scan recursively through the subdirectories.

© 2018 Victor Domingos, Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""
import os
import argparse

from pprint import pprint


def get_file_extension(file_path: str) -> str:
    filename_parts = file_path.split('.')
    if len(filename_parts) == 1:
        extension = '[no extension]'
    else:
        extension = filename_parts[-1]
    return extension
        

class WordCounter:
    def __init__(self):
        self.counters = dict()
        
    def count_word(self, word:str):
        if word in self.counters.keys():
            self.counters[word] += 1
        else:
            self.counters[word] = 1           

       
if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description='\nRecursively count all files in a directory, grouped by file extension.')
    
    parser.add_argument('path',
                        type=str,
                        help='The path to the folder containing the files to be counted.')
    
    parser.add_argument('-nr',
                        action='store_true',
                        help="Don't recurse through subdirectories")
    
    args = parser.parse_args()
    recursive = not args.nr
    
    fc = WordCounter()
        
    if args.path:
        location = os.path.expanduser(args.path)
        loc_text = ':\n' + location
    else:
        location = os.getcwd()
        loc_text = ' current directory'
    
                            
    if recursive:  
        print(f'Recursively counting all files in:\n{loc_text}.\n')
        
        for root, dirs, files in os.walk(location):
            for f in files:
                extension = get_file_extension(f)   
                fc.count_word(extension)
        
    else: 
        print(f'\nCounting files in{loc_text}.\n')
        
        for f in os.listdir(location):
            extension = get_file_extension(f)   
            fc.count_word(extension)
    
        
    pprint(fc.counters)
