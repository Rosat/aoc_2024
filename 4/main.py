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
   _solve_problem_part2(f"{script_directory}/data_small_part-2.txt")
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

def _solve_problem_part1(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 1
   with open(data_file, 'r') as f:

      # Get the lines and size
      f_str_lines = [line.rstrip('\n') for line in f]
      M = len(f_str_lines)
      N = len(f_str_lines[0])

      # Generate the columns
      f_str_cols = ["".join([i[j] for i in f_str_lines]) for j in range(N)]
      # Generate the ascending diagonals
      f_str_ascdiag = ["".join([f_str_lines[tot-j][j]  for j in range(tot+1) if j<M and tot-j<N]) for tot in range(M+N-1)]
      # Generate the descending diagonals
      f_str_descdiag = ["".join([f_str_lines[i][tot-(M-1)+i] for i in range(M) if 0 <= tot-(M-1)+i and tot-(M-1)+i < N]) for tot in range(M+N-1)]
      # Aggregating every direction
      f_str_alldir = f_str_lines + f_str_cols + f_str_ascdiag + f_str_descdiag

      # Searching for pattern
      occurrences = [re.findall("(?=(XMAS|SAMX))",line) for line in f_str_alldir]
      total = sum([len(line) for line in occurrences])

      print("Part 1 score : "+str(total))

def _solve_problem_part2(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 2
   with open(data_file, 'r') as f:

      # Get the lines and size
      f_str_lines = [line.rstrip('\n') for line in f]
      M = len(f_str_lines)
      N = len(f_str_lines[0])

      # Generate diagonal strings from original text
      f_str_ascdiag = ["".join([f_str_lines[tot-j][j]  for j in range(tot+1) if j<M and tot-j<N]) for tot in range(M+N-1)]
      f_str_descdiag = ["".join([f_str_lines[i][tot-(M-1)+i] for i in range(M) if 0 <= tot-(M-1)+i and tot-(M-1)+i < N]) for tot in range(M+N-1)]

      # Find the indices of 'A' in the matches for "MAS" and "SAM" in ascending and descending diagonals
      f_matches_ascdiag = [[(m.start(0)+1) for m in re.finditer("(?=(MAS|SAM))",line)] for line in f_str_ascdiag]
      f_matches_descdiag = [[(m.start(0)+1) for m in re.finditer("(?=(MAS|SAM))",line)] for line in f_str_descdiag]

      # Precompute inverse mapping from diagonal indices to original indices
      ascdiag_idx = [[[tot-j,j]  for j in range(tot+1) if j<M and tot-j<N] for tot in range(M+N-1)]
      descdiag_idx = [[[i,tot-(M-1)+i] for i in range(M) if 0 <= tot-(M-1)+i and tot-(M-1)+i < N] for tot in range(M+N-1)]
      
      # Recover original i,j from diagonal indices of 'A's (as found from SAM/MAS)
      f_matches_asc_origpos = [ascdiag_idx[x][y] for x in range(len(f_matches_ascdiag)) for y in f_matches_ascdiag[x]]
      f_matches_desc_origpos = [descdiag_idx[x][y] for x in range(len(f_matches_descdiag)) for y in f_matches_descdiag[x]]

      # Compute the number of common 'A' locations in the lists of original indices of 'A's
      has_match = lambda a,l: sum([a[0] == b[0] and a[1] == b[1] for b in l])
      f_xmas = [has_match(a,f_matches_desc_origpos) for a in f_matches_asc_origpos]
      total = sum(f_xmas)
      
      print("Part 2 score : "+str(total))


if __name__ == "__main__":
   main()