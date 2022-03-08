"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    def __init__(self, file):
        """Create attribute for words and print out number of words read"""
        self.file = file
        self.words = self.read(file)
        self.count()

    def __repr__(self):
        return f"WordFinder file = {self.file} words = {self.words} count = {self.count()}"
    
    def read(self, file):
        """Create a list of words from a file"""
        file = open(file)
        words_list = [line.strip() for line in file]
        file.close()
        return words_list

    def count(self):
        """Count how many words were read in the file"""
        print (f"{len(self.words)} words read")

    def random(self):
        return random.choice(self.words)