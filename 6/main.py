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

def _initialize_data(f):
   f_str = f.readlines()
   faces = "N"
   nb_steps_taken = 0
   f_str_N = f_str.copy()
   f_str_E = f_str.copy()
   f_str_S = f_str.copy()
   f_str_W = f_str.copy()
   for i in range(len(f_str)):
      line = f_str[i]
      for j in range(len(line)):
         if line[j] == "^":
            return f_str,i,j,faces,nb_steps_taken,f_str_N,f_str_E,f_str_S,f_str_W

def _replace_char(s, idx, new_char):
   return s[:idx] + new_char + s[idx+1:]

def _move_guard(f_str,i,j,faces,f_str_N,f_str_E,f_str_S,f_str_W):
   nb_steps_taken = 0
   new_i = i
   new_j = j
   new_faces = faces
   max_i = len(f_str)-1
   max_j = len(f_str[i])-1

   if faces == "N":
      if i == 0                  : nb_steps_taken = -1
      elif f_str[i-1][j] == "#"  : new_faces = "E"
      elif f_str_N[i][j] == "X"  : nb_steps_taken = -2
      else                       : new_i = i-1 ; nb_steps_taken = 1
      f_str_N[i] = _replace_char(f_str_N[i], j, "X")

   elif faces == "E":
      if j == max_j              : nb_steps_taken = -1
      elif f_str[i][j+1] == "#"  : new_faces = "S"
      elif f_str_E[i][j] == "X"  : nb_steps_taken = -2
      else                       : new_j = j+1 ; nb_steps_taken = 1
      f_str_E[i] = _replace_char(f_str_E[i], j, "X")
   
   elif faces == "S":
      if i == max_i              : nb_steps_taken = -1
      elif f_str[i+1][j] == "#"  : new_faces = "W"
      elif f_str_S[i][j] == "X"  :nb_steps_taken = -2
      else                       : new_i = i+1 ; nb_steps_taken = 1
      f_str_S[i] = _replace_char(f_str_S[i], j, "X")

   elif faces == "W":
      if j == 0                  : nb_steps_taken = -1
      elif f_str[i][j-1] == "#"  : new_faces = "N"
      elif f_str_W[i][j] == "X"  :nb_steps_taken = -2
      else                       : new_j = j-1 ; nb_steps_taken = 1
      f_str_W[i] = _replace_char(f_str_W[i], j, "X")
   
   else:
      print("Houston, we have a problem")

   f_str[i] = _replace_char(f_str[i], j, "X")

   return nb_steps_taken, new_i, new_j, new_faces


def _solve_problem_part1(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 1
   with open(data_file, 'r') as f:
      f_str_init,i_init,j_init,faces,nb_steps_taken,f_str_N,f_str_E,f_str_S,f_str_W = _initialize_data(f)
      f_str = f_str_init.copy()
      i = i_init
      j = j_init
      while nb_steps_taken != -1:
         nb_steps_taken, i, j, faces = _move_guard(f_str, i, j, faces,f_str_N,f_str_E,f_str_S,f_str_W)
      total = sum([line.count("X") for line in f_str])
      print("Part 1 score : "+str(total))

def _solve_problem_part2(data_file):
   "Function to solve the corresponding advent of code problem using the data in 'data_file'."
   _check_data(data_file)
   # Solving part 2
   with open(data_file, 'r') as f:
      f_str_init,i_init,j_init,faces_init,nb_steps_taken,f_str_N_init,f_str_E_init,f_str_S_init,f_str_W_init = _initialize_data(f)
      f_str = f_str_init.copy()
      i = i_init
      j = j_init
      faces = faces_init
      f_str_N = f_str_N_init.copy()
      f_str_E = f_str_E_init.copy()
      f_str_S = f_str_S_init.copy()
      f_str_W = f_str_W_init.copy()
      i_max = len(f_str)
      j_max = len(f_str[0])
      f_str_looping_obstacles = f_str_init.copy()

      while nb_steps_taken != -1:
         nb_steps_taken, i, j, faces = _move_guard(f_str, i, j, faces,f_str_N,f_str_E,f_str_S,f_str_W)

      for i0 in range(len(f_str)):
         for j0 in range(len(f_str)):
            if f_str[i0][j0] == "X" and (not (i0 == i_init and j0 == j_init)):
               nb_steps_taken = 0
               i = i_init
               j = j_init
               faces = faces_init
               f_str_N_new = f_str_N_init.copy()
               f_str_E_new = f_str_E_init.copy()
               f_str_S_new = f_str_S_init.copy()
               f_str_W_new = f_str_W_init.copy()
               f_str_new = f_str_init.copy()
               f_str_new[i0] = _replace_char(f_str_new[i0], j0, "#")
               while nb_steps_taken != -1 and nb_steps_taken != -2:
                  nb_steps_taken, i, j, faces = _move_guard(f_str_new, i, j, faces,f_str_N_new,f_str_E_new,f_str_S_new,f_str_W_new)

               if nb_steps_taken == -2:
                  f_str_looping_obstacles[i0] = _replace_char(f_str_looping_obstacles[i0], j0, "O")

      """
      while nb_steps_taken != -1:
         # Vérifier si on peut démarrer une loop ici
         i0 = i if faces in ["E","W"] else (i-1 if faces == "N" else i+1)
         j0 = j if faces in ["N","S"] else (j-1 if faces == "W" else j+1)
         # Le nouvel obstacle est dans le range, n'était pas déjà présent, et n'est pas la position de départ
         if 0<=i0 and i0<i_max and 0<=j0 and j0<j_max and (not (f_str_init[i0][j0] == "#")) and (not (i0 == i_init and j0 == j_init)):
            f_str_copy = f_str.copy()
            f_str_copy[i0] = _replace_char(f_str_copy[i0], j0, "#")
            i_copy = i
            j_copy = j
            faces_copy = faces
            f_str_N_copy = f_str_N.copy()
            f_str_E_copy = f_str_E.copy()
            f_str_S_copy = f_str_S.copy()
            f_str_W_copy = f_str_W.copy()
            nb_steps_taken_copy = 0
            while nb_steps_taken_copy != -1 and nb_steps_taken_copy != -2:
               nb_steps_taken_copy, i_copy, j_copy, faces_copy = _move_guard(f_str_copy, i_copy, j_copy, faces_copy,f_str_N_copy,f_str_E_copy,f_str_S_copy,f_str_W_copy)
            
            if nb_steps_taken_copy == -2:
               f_str_looping_obstacles[i0] = _replace_char(f_str_looping_obstacles[i0], j0, "O")

         nb_steps_taken, i, j, faces = _move_guard(f_str, i, j, faces,f_str_N,f_str_E,f_str_S,f_str_W)
      
      print("".join(f_str_looping_obstacles))
      """

      total = sum([line.count("O") for line in f_str_looping_obstacles])
      total_1 = sum([line.count("X") for line in f_str])
      print("Part 2 score : "+str(total)+" [original:"+str(total_1)+"]")


if __name__ == "__main__":
   main()