# (accomplished first try)
def find_solution1(arr):
    total = 0

    for elem in arr:
        low = elem[0]
        high = elem[1]
        letter = elem[2]
        count = 0
        for lett in elem[3]:
            if lett == letter:
                count += 1
        if count >= low and count <= high:
            total += 1
    return total

# (accomplished first try)
def find_solution2(arr):
    total = 0

    for elem in arr:
        low = elem[0]
        high = elem[1]
        letter = elem[2]
        count = 0

        if elem[3][low-1] == letter and elem[3][high-1] != letter:
            total += 1
        elif elem[3][low-1] != letter and elem[3][high-1] == letter:
            total += 1
        
    return total

if __name__ == "__main__":
   input_list = [ [ int(x.split('-')[0]), 
                    int(x.split('-')[1].split(' ')[0]), 
                    x.split('-')[1].split(' ')[1][0], 
                    x.split('-')[1].split(' ')[2]] for x in open("input.txt", "r").read().splitlines()]
   print(find_solution1(input_list))
   print(find_solution2(input_list))
