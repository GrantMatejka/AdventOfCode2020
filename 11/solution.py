# these are getting dirty but I've lost the holiday spirit
def find_solution1(mat):
   new_mat = [row[:] for row in mat]

   while True:
      for rowi in range(len(mat)):
         for coli in range(len(mat[rowi])):
            # check adjacent seats
            num_occupied = 0
            for i in [-1, 0, 1]:
               for j in [-1, 0, 1]:
                  if i == 0 and j == 0:
                     # seat we are on
                     continue;
                  # check bounds
                  if rowi + i >= 0 and rowi + i < len(mat) and coli + j >= 0 and coli + j < len(mat[rowi]):
                     if mat[rowi+i][coli+j] == '#':
                        num_occupied += 1
            
            # rules
            if mat[rowi][coli] == 'L' and num_occupied == 0:
               new_mat[rowi] = new_mat[rowi][:coli] + \
                   '#' + new_mat[rowi][coli+1:]
            elif mat[rowi][coli] == '#' and num_occupied >= 4:
               new_mat[rowi] = new_mat[rowi][:coli] + \
                   'L' + new_mat[rowi][coli+1:]

      if new_mat == mat:
         break
      else:
         mat = [row[:] for row in new_mat]

   count = 0
   for rowi in range(len(mat)):
       for coli in range(len(mat[rowi])):
          if mat[rowi][coli] == '#':
             count += 1
   return count


def find_solution2(mat):
   new_mat = [row[:] for row in mat]
   while True:
      for rowi in range(len(mat)):
         for coli in range(len(mat[rowi])):
            # check adjacent seats
            # dont even mess with floors
            if mat[rowi][coli] != '.':
               num_occupied = 0
               for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                  ridx = rowi
                  colidx = coli
                  while True:
                     ridx += i
                     colidx += j
                     if ridx < 0 or ridx >= len(mat) or colidx < 0 or colidx >= len(mat[rowi]):
                        break
                     # check bounds
                     if mat[ridx][colidx] == '#':
                        num_occupied += 1
                        break;
                     if mat[ridx][colidx] == 'L':
                        break;

               # rules
               if mat[rowi][coli] == 'L' and num_occupied == 0:
                  new_mat[rowi] = new_mat[rowi][:coli] + \
                     '#' + new_mat[rowi][coli+1:]
               elif mat[rowi][coli] == '#' and num_occupied >= 5:
                  new_mat[rowi] = new_mat[rowi][:coli] + \
                     'L' + new_mat[rowi][coli+1:]

      if new_mat == mat:
         break
      else:
         mat = [row[:] for row in new_mat]

   count = 0
   for rowi in range(len(mat)):
       for coli in range(len(mat[rowi])):
          if mat[rowi][coli] == '#':
             count += 1
   return count

if __name__ == "__main__":
   input_list = open("input.txt", "r").read().splitlines()
   print(find_solution1(input_list))
   print(find_solution2(input_list))
