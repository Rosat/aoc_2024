"""
Script to solve an advent of code problem.
"""

# Standard library imports
import os
import logging
import sys
import re


def main():
   script_directory = os.path.dirname(os.path.abspath(__file__))

   _solve_problem(f"{script_directory}/data_small.txt")
   # Uncomment following line when the problem can be solved with the small data.
   _solve_problem(f"{script_directory}/data.txt")


def _solve_problem(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   # Ensure that data file exists
   if not os.path.isfile(data_file):
      logging.error("Data file does not exist.")
      sys.exit(1)

   # Ensure that input exists
   if os.path.getsize(data_file) <= 0:
      logging.error("Data file is still empty.")
      sys.exit(1)

   with open(data_file, 'r') as f:
      # Read data and solve the problem here instead of passing
      n1_tmp=[]; l2_tmp=[]
      l1=[]; l2=[]
      f_str = f.read()
      occurrences = re.findall("mul\([0-9][0-9]?[0-9]?\,[0-9][0-9]?[0-9]?\)",f_str)
      total = 0
      for s in occurrences:
         pair=re.findall("[0-9][0-9]?[0-9]?",s)
         total+= int(pair[0]) * int(pair[1])
      print(total)
      pass

if __name__ == "__main__":
   main()