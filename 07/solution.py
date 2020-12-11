from collections import defaultdict
import re

def find_solution1(color_dict):
   ans = set()

   # search tree for 'shiny gold' and find set of connections
   solution1_helper("shiny gold", color_dict, ans)

   return len(ans)

def solution1_helper(color, color_dict, visited):
   for c in color_dict:
      if color in [col[0] for col in color_dict[c]]:
         visited.add(c)
         solution1_helper(c, color_dict, visited)


def find_solution2(color_dict):
   return solution2_helper("shiny gold", color_dict) - 1

def solution2_helper(color, color_dict):
   count = 1

   for col in color_dict[color]:
      count += col[1] * solution2_helper(col[0], color_dict)
   
   return count

if __name__ == "__main__":
   input_list = [x.replace('\n', '').replace(",", "").replace(".", "").replace("bags","").replace("bag","").replace("contain","") 
      for x in open("input.txt", "r").read().splitlines()]
   input_list = [[y.strip() for y in x.split("  ") if len(y) > 0]
                 for x in input_list]

   color_dict = {}

   for lugg in input_list:
      color_dict[lugg[0]] = []
      for idx in range(1, len(lugg)):
         if lugg[idx] != "no other":
            color_dict[lugg[0]].append([lugg[idx][2:], int(lugg[idx][0:1])])

   print(find_solution1(color_dict))
   print(find_solution2(color_dict))
