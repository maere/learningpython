#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.


Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

1. For the --count flag, 
implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). 

Store all the words as lowercase, so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. 
Get it to an intermediate milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.


"""

import sys

# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it. # Then print_words() and print_top() can just call the utility function.
# can we consider f a stream?
    
 # utilty function
def read_file_into_mem(filename):    
    # create dict to store words/counts
    word_count = {}
    
    #open stream and iterate through file
    f = open(filename, 'rU')
    for line in f:
    
        # split the line on the white space and push into a listarray
        line_list = line.split()
        
        # check to see if the key is in the dict
        i=0
        while i < len(line_list):
            # if key is not in dict, add key and create count
            next_word = line_list[i]
            next_word = next_word.lower()
            if next_word in word_count:
                word_count[next_word] +=1
            # if key is in dict, iterate count
            else:
                word_count[next_word] = 1
            i+=1
    f.close()  
    return word_count    
    

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
def print_words(filename):

    #calls utility to build dict from file
    in_mem_dict = read_file_into_mem(filename)
    dict_as_tuples_list = in_mem_dict.items()
    final_list = sorted(dict_as_tuples_list)
    
    #print them all on a new line
    for item in final_list:
        print item[0], item[1]
        

def print_top(filename):

    def count((k, v)):
        return v

    #calls utility to build dict from file
    in_mem_dict = read_file_into_mem(filename)
    dict_as_tuples_list = in_mem_dict.items()
    
    #do custom sort for largest count by second item in tuple
    high_count_list = sorted(dict_as_tuples_list, key=count, reverse=True) 
    
    #iterate through pulling top 20 counts
    for i in range(20):
        item = high_count_list[i]
        print item[0], item[1]
    


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
