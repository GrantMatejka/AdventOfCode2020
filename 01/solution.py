# for part 1 (accomplished first try)
def find_solution1(arr):
   # clearly O(n^2), I wonder if there's a faster way
   for x in arr:
      for y in arr:
         if x != y and x + y == 2020:
            return [x*y, x, y]

# for part 2 (accomplished first try)
def find_solution2(arr):
   # clearly O(n^3), I wonder if there's a faster way
   for x in arr:
      for y in arr:
         for z in arr:
            if x != y and y != z and x + y + z == 2020:
               return [x*y*z, x, y, z]

'''
You need to find the two entries that sum to 2020 
and then multiply those two numbers together.
'''
if __name__ == "__main__":
   input_list = [int(x) for x in open("input.txt", "r").read().splitlines()]
   print(find_solution1(input_list))
   print(find_solution2(input_list))

