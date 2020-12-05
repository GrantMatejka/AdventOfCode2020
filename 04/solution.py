import re

'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''

# first try :)


def find_solution1(arr):
   fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
   valid_count = 0

   for passport in arr:
      i = 0
      valid = True
      while valid and i < len(fields):
         if fields[i] in passport:
            i += 1
         else:
            valid = False

      if valid:
         valid_count += 1
   return valid_count

# super dirty but first try as well
def find_solution2(arr):
   field_conditions = [
       ["byr", 1920, 2002],
       ["iyr", 2010, 2020],
       ["eyr", 2020, 2030],
       ["hgt", ["cm", 150, 193], ["in", 59, 76]],
       ["hcl"],
       ["ecl", ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]],
       ["pid"]]
   valid_count = 0

   potential_passports = []
   for passport in arr:
    if all((element[0] in passport) for element in field_conditions):
        potential_passports.append(re.split(' ', passport.replace('\n', ' ')))

   # so we dont need to worry about validating them
   for passport in potential_passports:
      valid = True
      for field in passport:
         value = field.split(':')
         if len(value) == 2:
            value = value[1]
            for condition in field_conditions:
               if condition[0] in field and condition[0] == "byr":
                  if int(value) < condition[1] or int(value) > condition[2]:
                     valid = False
               elif condition[0] in field and condition[0] == "iyr":
                  if int(value) < condition[1] or int(value) > condition[2]:
                     valid = False
               elif condition[0] in field and condition[0] == "eyr":
                  if int(value) < condition[1] or int(value) > condition[2]:
                     valid = False
               elif condition[0] in field and condition[0] == "hgt":
                  if condition[1][0] in field:
                     value = value.replace(condition[1][0], '')
                     if int(value) < condition[1][1] or int(value) > condition[1][2]:
                        valid = False
                  elif condition[2][0] in field:
                     value = value.replace(condition[2][0], '')
                     if int(value) < condition[2][1] or int(value) > condition[2][2]:
                        valid = False
                  else:
                     valid = False
               elif condition[0] in field and condition[0] == "hcl":
                  if not re.search("^[#][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$", value):
                     valid = False
               elif condition[0] in field and condition[0] == "ecl":
                  if value not in condition[1]:
                     valid = False
               elif condition[0] in field and condition[0] == "pid":
                  if not re.search("^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$", value):
                     valid = False
               #print(condition[0] + " " + field + " " + str(valid))

      if valid:
         valid_count += 1

   return valid_count


if __name__ == "__main__":
   input_list = open("input.txt", "r").read().split("\n\n")
   print(find_solution1(input_list))
   print(find_solution2(input_list))
