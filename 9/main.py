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
import math

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

def _solve_problem_part1(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 1
   with open(data_file, 'r') as f:
      disk_map = [int(i) for i in f.read()]
      disk_files = [k for k in range(int(len(disk_map)/2)+1) for i in range(disk_map[2*k])]
      total = 0
      curr_mult = 0
      while disk_files :
         file_space = disk_map.pop(0)
         empty_space = disk_map.pop(0)
         # print("Next op : (file = "+str(file_space)+") -- (empty = "+str(empty_space)+")")
         while disk_files and file_space > 0:
            file_space -= 1
            total += curr_mult * disk_files.pop(0)
            curr_mult += 1
         while disk_files and empty_space > 0:
            empty_space -= 1
            total += curr_mult * disk_files.pop(-1)
            curr_mult += 1
      print("Part 1 score : "+str(total))

def _solve_problem_part2(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 2
   with open(data_file, 'r') as f:

      # Useful lambdas
      value = lambda x : int(x/2) if x % 2 == 0 else -1
      str_with_dotX = lambda x : "X" if x >= 0 else "."
      minone_to_zero = lambda x : 0 if x == -1 else x

      # Get disk map as given
      disk_map = [int(i) for i in f.read()]
      n_files = int(len(disk_map) / 2) + 1

      # Get corresponding disk state, where -1 correspond to empty spots (and file slots have their file numbers)
      disk = [value(k) for k in range(len(disk_map)) for i in range(disk_map[k])]

      # Create the corresponding string that has "X" for file space and "." for empty space
      # This one will be used to look for empty spots where files could be inserted during defragmentation
      disk_str = "".join(map(str_with_dotX,disk))
      
      # Get the start index and length of files
      disk_files_starts = [disk.index(k) for k in range(n_files)]
      disk_files_lengths = [disk_map[2*k] for k in range (n_files)]

      # Iterate from last to first file and look for the right spot to insert for each one in the disk string
      for file_nb in range(len(disk_files_starts)-1,0,-1):
         file_len = disk_files_lengths[file_nb]
         file_start = disk_files_starts[file_nb]
         # We want to insert the file at the first occurrence of a repetion of [file len] times character "."
         first_empty_bigenough = disk_str.find("." * file_len)
         if first_empty_bigenough >= 0 and first_empty_bigenough < file_start:
            # Switch the file with the empty spot both in disk and in disk_str
            disk_str = disk_str[:first_empty_bigenough] + ("X"*file_len) + disk_str[(first_empty_bigenough+file_len):]
            disk_str = disk_str[:file_start] + ("."*file_len) + disk_str[(file_start+file_len):]
            for k in range(file_len):
               disk[first_empty_bigenough + k] = file_nb
               disk[file_start + k] = -1
      
      # To compute the sumproduct, we need to replace -1 with 0 in the disk (empty spaces do not count in the sum)
      disk = [minone_to_zero(k) for k in disk]
      list_one_N = [k for k in range(len(disk))]
      total = sum([x * y for x,y in zip(disk,list_one_N)])
      print("Part 2 score : "+str(total))

if __name__ == "__main__":
   main()