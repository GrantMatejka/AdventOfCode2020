# (accomplished first try)
def find_solution1(mat):
   tree_count = 0
   x = 0
   y = 0

   while (y < len(mat) - 1):
      x += 3
      y += 1

      if x >= len(mat[y]):
         x = x - len(mat[y])
      
      # Hit a tree
      if mat[y][x] == '#':
         tree_count += 1

   return tree_count

# (accomplished first try)
def find_solution2(mat):
   tree_total = 1
   slopes_to_check = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

   for slope in slopes_to_check:
      tree_count = 0
      x = 0
      y = 0
      dx = slope[0]
      dy = slope[1]

      while (y < len(mat) - 1):
         x += dx
         y += dy

         if x >= len(mat[y]):
            x = x - len(mat[y])

         # Hit a tree
         if mat[y][x] == '#':
            tree_count += 1

      if tree_count > 0:
         tree_total *= tree_count

   return tree_total

if __name__ == "__main__":
   input_matrix = [x for x in open("input.txt", "r").read().splitlines()]
   print(find_solution1(input_matrix))
   print(find_solution2(input_matrix))
