
def find_solution1(arr):
   accumulator = 0
   idx = 0

   while (True):
      if arr[idx][2] == True:
         break;

      if arr[idx][0] == "nop":
         idx += 1
      elif arr[idx][0] == "acc":
         accumulator += arr[idx][1]
         idx += 1
      elif arr[idx][0] == "jmp":
         idx += arr[idx][1]
      
      arr[idx-1][2] = True

   return accumulator


def find_solution2(arr):
   accumulator = 0
   idx = 0

   while idx < len(arr):
      tested = 0
      if arr[idx][0] == "nop":
         arr[idx][0] = "jmp"
         tested = test_solution(arr)
         arr[idx][0] = "nop"
      elif arr[idx][0] == "jmp":
         arr[idx][0] = "nop"
         tested = test_solution(arr)
         arr[idx][0] = "jmp"

      arr = [[x[0],x[1], False] for x in arr]
      if tested > 0:
         return tested
      idx += 1
      

def test_solution(arr):
   accumulator = 0
   idx = 0
   
   while (idx < len(arr)):
      if arr[idx][2] == True:
         break

      if arr[idx][0] == "nop":
         idx += 1
      elif arr[idx][0] == "acc":
         accumulator += arr[idx][1]
         idx += 1
      elif arr[idx][0] == "jmp":
         idx += arr[idx][1]

      arr[idx-1][2] = True
   
   if idx == len(arr):
      return accumulator
   else:
      return 0

if __name__ == "__main__":
   input_list = [[x.split()[0], int(x.split()[1]), False]
                 for x in open("input.txt", "r").read().splitlines()]

   print(find_solution1(input_list))
   print(find_solution2(input_list))
