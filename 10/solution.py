
def find_solution1(arr):
   arr.sort()
   highest = max(arr) + 3
   idx = 0
   jolt_arr = [0]

   while idx < len(arr):
      if arr[idx] - jolt_arr[len(jolt_arr)-1] <= 3:
         jolt_arr.append(arr[idx])

      idx += 1
   
   jolt_arr.append(highest)

   one_jump = 0
   three_jump = 0
   for i in range(len(jolt_arr)-1):
      if jolt_arr[i+1] - jolt_arr[i] == 1:
         one_jump += 1
      elif jolt_arr[i+1] - jolt_arr[i] == 3:
         three_jump += 1

   return one_jump * three_jump


# dynamic programming ftw, this was a doozy and no good recursively
def find_solution2(arr):
   sol = {0: 1}
   arr.sort()
   for num in arr:
      sol[num] = 0
      if num - 1 in sol:
         sol[num] += sol[num-1]
      if num - 2 in sol:
         sol[num] += sol[num-2]
      if num - 3 in sol:
         sol[num] += sol[num-3]
   return(sol[max(arr)])

if __name__ == "__main__":
   input_list = [int(x) for x in open("input.txt", "r").read().splitlines()]
   print(find_solution1(input_list))
   print(find_solution2(input_list))
