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

   _solve_problem_part1(f"{script_directory}/data_small.txt")
   # Uncomment following line when the problem can be solved with the small data.
   _solve_problem_part1(f"{script_directory}/data.txt")
   
   _solve_problem_part2(f"{script_directory}/data_small_part-2.txt")
   # Uncomment following line when the problem can be solved with the small data.
   _solve_problem_part2(f"{script_directory}/data.txt")


def _solve_problem_part1(data_file):
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
      f_str = f.read()
      muls = re.findall("mul\([0-9][0-9]?[0-9]?\,[0-9][0-9]?[0-9]?\)",f_str)
      pairs = [re.findall("[0-9][0-9]?[0-9]?",s) for s in muls]
      total = sum([int(p[0])*int(p[1]) for p in pairs])
      print(total)


def _solve_problem_part2(data_file):
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
      # Inelegant but easier way (using for loop)
      f_str = f.read()
      occurrences = re.findall("mul\([0-9][0-9]?[0-9]?\,[0-9][0-9]?[0-9]?\)|do\(\)|don't\(\)",f_str)
      total = 0
      active = 1
      for s in occurrences:
         if s == "do()" :
            active = 1
         elif s == "don't()" :
            active = 0
         elif active == 1 :
            pair=re.findall("[0-9][0-9]?[0-9]?",s)
            total+= int(pair[0]) * int(pair[1])
      print("Inelegant score : "+str(total))
   
   # Elegant way (with regex only)
   with open(data_file, 'r') as f:
      f_str = "do()" + f.read() + "don't()"
      f_str = "".join(re.findall("do\(\)(.*?)don't\(\)",f_str,re.DOTALL))
      muls = re.findall("mul\([0-9][0-9]?[0-9]?\,[0-9][0-9]?[0-9]?\)",f_str)
      pairs = [re.findall("[0-9][0-9]?[0-9]?",s) for s in muls]
      total_2 = sum([int(p[0])*int(p[1]) for p in pairs])

      print("Elegant score   : "+str(total_2))

if __name__ == "__main__":
   main()