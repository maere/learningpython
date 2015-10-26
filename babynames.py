#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:

 -Extract the year and print it
 
 -Extract the names and rank numbers and just print them
 
 -Get the names data into a dict and print it (#bc no dupes?)
    add an if statement to see if it exist and if it does, v = higher num
    
 -Build the [year, 'name rank', ... ] list and print it
 
 -Fix main() to use the extract_names list
"""
#utility function to sort alphabettically on name
def alphabetize((k, v)):
  return k

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  #open file and feed data
  f = open(filename, 'rU')
  data = f.read()
  
  #then do something with the data - put it somewhere in mem
  #set year 
  match = re.search("(<.*?>)(\w+\s\w+\s)(\d\d\d\d)(<.*?>)", data)
  year = match.group(3)
  
  #get list of tuples - note when match group is converted to tuple indexing changes to 0-based
  nameslist = re.findall("<.*?><.*?>(\d+)<.*?><.*?>(\w+)<.*?><.*?>(\w+)</td>", data)
  
  all_names = {}
  
  for tuple in nameslist:
    rank = tuple[0] 
    boy = tuple[1] 
    girl = tuple[2]
    all_names[boy] = rank
    all_names[girl] = rank
  
  #can call .items() on the dict to build a list of it's tuples
  two_tuple_list = all_names.items()
  
  #write function to sort by v (above) &   #create sorted(list)
  final_list = sorted(two_tuple_list, key=alphabetize)
  final_list.insert(0, (year, ""))
  #for tup in final_list:
  #  print tup[0], tup[1]
  f.close()
  return final_list
  


#print to screen function | no flag given
def print_to_console(final_list):
   for tup in final_list:
     print tup[0], tup[1]

#create and write to file function | --summary file flag given
def print_to_file(final_list, new_file):
  f = open(new_file, 'w')
  for tup in final_list:
     line = tup[0] + ' ' + tup[1] + '\n'
     f.write(line)
  f.close()




def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  for item in args:
    final_list = extract_names(item)
    if summary==False:
        print_to_console(final_list)
    elif summary==True:
        new_file = item + ".summary"
        print_to_file(final_list, new_file)  
    
  
  
  

  
  
  
if __name__ == '__main__':
  main()
