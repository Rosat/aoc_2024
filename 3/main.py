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
   _solve_problem_part1(f"{script_directory}/data.txt")
   _solve_problem_part2_inelegant(f"{script_directory}/data_small_part-2.txt")
   _solve_problem_part2_inelegant(f"{script_directory}/data.txt")
   _solve_problem_part2_elegant(f"{script_directory}/data_small_part-2.txt")
   _solve_problem_part2_elegant(f"{script_directory}/data.txt")

def _check_data(data_file):
   # Ensure that data file exists
   if not os.path.isfile(data_file):
      logging.error("Data file does not exist.")
      sys.exit(1)

   # Ensure that input exists
   if os.path.getsize(data_file) <= 0:
      logging.error("Data file is still empty.")
      sys.exit(1)


def _solve_problem_part1(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 1
   with open(data_file, 'r') as f:
      
      f_str = f.read()
      muls = re.findall(r"mul\([0-9][0-9]?[0-9]?\,[0-9][0-9]?[0-9]?\)",f_str) # Extracting all mul(x,y) in a list where x,y are integers and 0 <= x,y <=999
      pairs = [re.findall(r"[0-9][0-9]?[0-9]?",s) for s in muls]              # Extracting all x,y pairs from previous list
      total = sum([int(p[0])*int(p[1]) for p in pairs])                       # Sum product of all x,y pairs

      print("Part 1            : "+str(total))


def _solve_problem_part2_inelegant(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 2 with more separators and a for loop
   with open(data_file, 'r') as f:

      f_str = f.read()
      occurrences = re.findall(r"mul\([0-9][0-9]?[0-9]?\,[0-9][0-9]?[0-9]?\)|do\(\)|don't\(\)",f_str)  # Part 2 - Adding do() and don't() to the regex
      total = 0
      active = 1
      for s in occurrences:
         if s == "do()" :
            active = 1
         elif s == "don't()" :
            active = 0
         elif active == 1 :
            pair=re.findall(r"[0-9][0-9]?[0-9]?",s)
            total+= int(pair[0]) * int(pair[1])

      print("Part 2 (for loop) : "+str(total))


def _solve_problem_part2_elegant(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 2 with regexes only
   with open(data_file, 'r') as f:

      f_str = "do()" + f.read() + "don't()"                                   # Part 2 - Ensuring that all relevant multiplications are between a do() and a don't()
      f_str = "".join(re.findall(r"do\(\)(.*?)don't\(\)",f_str,re.DOTALL))    # Part 2 - Extracting relevant multiplications, newlines do not break instructions
      muls = re.findall(r"mul\([0-9][0-9]?[0-9]?\,[0-9][0-9]?[0-9]?\)",f_str) # No change
      pairs = [re.findall(r"[0-9][0-9]?[0-9]?",s) for s in muls]              # No change
      total_2 = sum([int(p[0])*int(p[1]) for p in pairs])                     # No change
      
      print("Part 2 (regex)    : "+str(total_2))

if __name__ == "__main__":
   main()