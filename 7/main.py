"""
Script to solve an advent of code problem.
"""

# Standard library imports
import os
import logging
import sys
import re
import numpy as np
import itertools


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

def _initialize_data(f):
   f_lines = f.readlines()
   numbers = [[int(s) for s in re.findall(r'\d+',line)] for line in f_lines]
   # answers = [sl.pop(0) for sl in numbers]
   return numbers

operate = lambda x,y,o : x+y if o==0 else (x*y if o==1 else int(str(x)+str(y)))

str_ope = lambda o : " + " if o==0 else (" * " if o == 1 else " || ")

def _apply_ops(list, operators):
   total = list[0]
   for i in range(len(list)-1):
      total = operate(total,list[i+1],operators[i])
   return total

def _print_test(answer,terms,operators):
   ans = str(answer)+" ?= "+str(terms[0])
   for i in range(len(terms)-1):
      ans = ans + str_ope(operators[i])
      ans = ans + str(terms[i+1])
   return ans

def _find_operators(numbers,problem_part):
   """Find a set of operators such that if applied to numbers[1:], one gets numbers[0]. If impossible, is_feasible returns 0
      True = ADD ; False = MULTIPLY"""
   expected_answer = numbers[0]
   terms = numbers[1:]
   nb_ops = len(terms)-1
   is_feasible = False
   ope_range = [0,1] if problem_part == 1 else [0,1,2]
   for operators in itertools.product(ope_range, repeat=nb_ops):
      ans = _apply_ops(terms,operators)
      #print(_print_test(expected_answer, terms, operators))
      if ans == expected_answer:
         is_feasible = True
         break
   return is_feasible

def _solve_problem_part1(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 1
   with open(data_file, 'r') as f:
      numbers_lines = _initialize_data(f)
      total_calibration_results = [numbers[0] for numbers in numbers_lines if _find_operators(numbers,1)]
      total = sum(total_calibration_results)
      print("Part 1 score : "+str(total))

def _solve_problem_part2(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 2
   with open(data_file, 'r') as f:
      numbers_lines = _initialize_data(f)
      total_calibration_results = [numbers[0] for numbers in numbers_lines if _find_operators(numbers,2)]
      total = sum(total_calibration_results)
      print("Part 2 score : "+str(total))

if __name__ == "__main__":
   main()