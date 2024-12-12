"""
Script to solve an advent of code problem.
"""

# Standard library imports
import os
import logging
import sys
import pandas as pd


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
      l1=[]; l2=[];
      print(l1)
      print(l2)
      for line in f:
         l1.append(int(str.split(line)[0]))
         l2.append(int(str.split(line)[1]))
      l1.sort()
      l2.sort()
      
      # Pour part 1
      res_1 = sum([abs(x-y) for x, y in zip(l1, l2)])
      print(res_1)

      # Pour part 2
      l1_unique = list(dict.fromkeys(l1))
      res_2 = sum([x * l2.count(x) for x in l1_unique])
      print(res_2)
      pass

if __name__ == "__main__":
   main()