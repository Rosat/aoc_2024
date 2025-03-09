"""
Script to solve an advent of code problem.
"""

# Standard library imports
import os
import logging
import sys
import re
import numpy as np


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

def _read_data(f):
   """Function to read the data and extract ordering rules and updates"""
   ordrules_pairs = []
   updates_lists = []
   is_reading_ordrules = True
   for line in f:
      if not (("|" in line) or ("," in line)):
         is_reading_ordrules = False
      elif is_reading_ordrules:
         ordrules_pairs.append([int(s) for s in line.split("|")])
      else:
         updates_lists.append([int(s) for s in line.split(",")])
   return ordrules_pairs, updates_lists

def _prec_matrix(ordrules_pairs, updates_lists):
      """Returns the precedence matrix A where A[i,j] = 1 if i must be before j, and 0 otherwise."""
      max_page = max([pair[0] for pair in ordrules_pairs]+[pair[1] for pair in ordrules_pairs]+[p for update in updates_lists for p in update])
      prec_matrix = np.zeros((max_page+1,max_page+1))
      for pair in ordrules_pairs:
         prec_matrix[pair[0],pair[1]] = 1
      return prec_matrix

def _update_score(update, prec_matrix):
   """Returns  the score of the update, i.e., the number of incorrectly ordered pages in that update."""
   return sum([prec_matrix[update[i],update[j]] for i in range(len(update)) for j in range(i) ])

middle_number = lambda l : l[int(len(l)/2)]

def _sort_incorr_update(incorr_update,prec_matrix):
   """Returns the correctly-ordered update, given the precendence matrix that imposes pages precedence rules."""
   sub_incorr_update = incorr_update.copy()
   correct_order = []
   # Principle of the while-loop :
   # The page in the correct order is th one with no predecessors, i.e., argmin() of the sum of the number of explicitely defined predecessors in the precedence matrix.
   # Using that, we can determine the (correct) first page, remove it, and iterate to find the second one, etc.
   while sub_incorr_update != []:
      nb_of_explicit_pred_per_page = prec_matrix[sub_incorr_update,:][:,sub_incorr_update].sum(axis = 0) # Nb of explicitely defined predecessors for each page of the pages that we still have to sort
      id_min_pred = nb_of_explicit_pred_per_page.argmin()                                                # Id of the page with the least (0) predecessors in this sub-update
      correct_order.append(sub_incorr_update[id_min_pred])                                               # This element is the next in the list
      sub_incorr_update.pop(id_min_pred)                                                                 # We remove it from the sub-list and iterate to find the next one
   return correct_order

def _solve_problem_part1(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 1
   with open(data_file, 'r') as f:
      ordrules_pairs, updates_lists = _read_data(f)
      # Computing the precedence matrix
      prec_matrix = _prec_matrix(ordrules_pairs, updates_lists)
      # Computing the sum of middle pages numbers for updates that are already in the correct order (update_score == 0)
      total = sum([middle_number(update) for update in updates_lists if _update_score(update,prec_matrix) == 0])
      print("Part 1 score : "+str(total))

def _solve_problem_part2(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 2
   with open(data_file, 'r') as f:
      ordrules_pairs, updates_lists = _read_data(f)
      # Computing the precedence matrix
      prec_matrix = _prec_matrix(ordrules_pairs, updates_lists)
      # Extracting incorrect updates only (update_score != 0)
      incorr_updates_lists = [update for update in updates_lists if _update_score(update,prec_matrix) != 0]
      # Re-ordering pages of incorrect updates
      corrected_incorr_update_lists = [_sort_incorr_update(update,prec_matrix) for update in incorr_updates_lists]
      # Computing the sum of middle pages numbers
      total = sum([middle_number(update) for update in corrected_incorr_update_lists])
      print("Part 2 score : "+str(total))

if __name__ == "__main__":
   main()