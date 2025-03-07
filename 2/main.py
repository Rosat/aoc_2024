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
   _solve_problem_part2(f"{script_directory}/data_small.txt")
   _solve_problem_part2(f"{script_directory}/data.txt")

def _check_data(data_file):
   # Ensure that data file exists
   if not os.path.isfile(data_file):
      logging.error("Data file does not exist.")
      sys.exit(1)

   # Ensure that input exists
   if os.path.getsize(data_file) <= 0:
      logging.error("Data file is still empty.")
      sys.exit(1)


# Operators for list comparison and alternatives generation (easier to read)
multiand = lambda a,b: [x and y for (x,y) in zip(a,b)]
multior = lambda a,b: [x or y for (x,y) in zip(a,b)]
all_alternatives_for_one_line = lambda a,b: a if (b==-1) else [a[n] for n in range(len(a)) if n != b]

def _nb_of_correct_in_list(numbers):
      """Function to count how many lines are correct in a list of lines of int"""
      diffs = [[(l_num[n] - l_num[n+1]) for n in range(len(l_num)-1)] for l_num in numbers]
      # Check the three conditions separately
      incrs = [all([diff>0  for diff in line_diff]) for line_diff in diffs]
      decrs = [all([diff<0 for diff in line_diff]) for line_diff in diffs]
      difok = [all([(0<abs(diff) and abs(diff)<4) for diff in line_diff]) for line_diff in diffs]
      # Check conditions together
      allcond = multiand(multior(incrs,decrs),difok)
      total = sum(allcond)
      return total

def _solve_problem_part1(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 1
   with open(data_file, 'r') as f:
      numbers = [[int(number) for number in line.split(" ")] for line in f]
      print("Part 1 score : "+str(_nb_of_correct_in_list(numbers)))

def _solve_problem_part2(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 2 with more separators and a for loop
   with open(data_file, 'r') as f:
      numbers = [[int(number) for number in line.split(" ")] for line in f]
      # Générer les sous-listes pour chaque ligne (avec tous les records ou tous sauf 1)
      alternatives = [[all_alternatives_for_one_line(numline,b) for b in range(-1,len(numline))] for numline in numbers]
      # Si au moins 1 alternative (i.e., original ou moins 1 entrée) est ok, alors la ligne est ok
      is_one_alt_ok = [(_nb_of_correct_in_list(alt_for_line) > 0) for alt_for_line in alternatives]
      total = sum(is_one_alt_ok)
      print("Part 1 score : "+str(total))


if __name__ == "__main__":
   main()