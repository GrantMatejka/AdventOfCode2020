# first try :)
def find_solution1(arr):
   running_total = 0

   for answer_list in arr:
      dummy_set = []
      for answer in answer_list:
         if answer not in dummy_set:
            dummy_set.append(answer)
      running_total += len(dummy_set)
   return running_total

# third try :( shoulda tested sooner
def find_solution2(arr):
   running_total = 0

   for answer_group_list in arr:
      print(answer_group_list)
      intersec = answer_group_list[0]
      for answer_group in answer_group_list:
         if len(answer_group) > 0:
            intersec = intersec.intersection(answer_group)
      print(intersec)
      print(len(intersec))
      running_total += len(intersec)
   return running_total

if __name__ == "__main__":
   input_list = [x.replace('\n', '') for x  in open("input.txt", "r").read().split("\n\n")]
   print(find_solution1(input_list))
   input_list = [[set(y) for y in x.split('\n')] for x  in open("input.txt", "r").read().split("\n\n")]
   print(find_solution2(input_list))
