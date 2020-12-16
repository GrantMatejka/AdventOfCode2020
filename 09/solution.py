
def find_solution1(arr, preamble):
   idx = 0

   while idx + preamble < len(arr):
      valid_pair = False
      end = idx + preamble
      for i in range(idx, end):
         for j in range(i + 1, end):
            if arr[i] != arr[j] and arr[i] + arr[j] == arr[end]:
               valid_pair = True
      if valid_pair != True:
         return arr[end]
      idx += 1

   return -1


def find_solution2(arr):
   goal_sum = 530627549

   for idx in range(len(arr)):
      i = 0
      ret_arr = []
      while sum(ret_arr) < 530627549:
         ret_arr.append(arr[i + idx])
         i += 1

      if sum(ret_arr) == 530627549:
         return min(ret_arr) + max(ret_arr)

   return 0

if __name__ == "__main__":
   input_list = [int(x) for x in open("input.txt", "r").read().splitlines()]
   preamble = 25
   print(find_solution1(input_list, preamble))
   print(find_solution2(input_list))
