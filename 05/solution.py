# first try once again 
def find_solution1(arr):
   seat_id_list = []

   for asgn in arr:
      row = [0, 127]
      col = [0, 7]
      for lett in asgn[:7]:
         if lett == 'F':
            row[1] = ((row[1] - row[0]) // 2) + row[0]
         else:
            row[0] = (row[1] // 2) + (row[0] // 2) + 1
      for lett in asgn[7:]:
         if lett == 'L':
            col[1] = ((col[1] - col[0]) // 2) + col[0]
         else:
            col[0] = (col[1] // 2) + (col[0] // 2) + 1

      seat_id_list.append((row[0] * 8) + col[0])
            
   return max(seat_id_list)

'''
The seats at the very front and back of the plane don't exist on this aircraft, 
so they'll be missing from your list as well.
Your seat wasn't at the very front or back, though; 
the seats with IDs +1 and -1 from yours will be in your list.
'''
# first try, I should go through and clean up all these solutions but oh well
def find_solution2(arr):
   seat_id_list = []

   for asgn in arr:
      row = [0, 127]
      col = [0, 7]
      for lett in asgn[:7]:
         if lett == 'F':
            row[1] = ((row[1] - row[0]) // 2) + row[0]
         else:
            row[0] = (row[1] // 2) + (row[0] // 2) + 1
      for lett in asgn[7:]:
         if lett == 'L':
            col[1] = ((col[1] - col[0]) // 2) + col[0]
         else:
            col[0] = (col[1] // 2) + (col[0] // 2) + 1

      seat_id_list.append((row[0] * 8) + col[0])
            
   seat_id_list.sort()

   for seat_idx in range(1, len(seat_id_list) - 1):
      if seat_id_list[seat_idx - 1] + 1 != seat_id_list[seat_idx]:
         return seat_id_list[seat_idx - 1] + 1
      if seat_id_list[seat_idx + 1] - 1 != seat_id_list[seat_idx]:
         return seat_id_list[seat_idx + 1] - 1

if __name__ == "__main__":
   input_list = open("input.txt", "r").read().splitlines()
   print(find_solution1(input_list))
   print(find_solution2(input_list))