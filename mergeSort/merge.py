import sys

def main():
    global counter
    if len(sys.argv) == 1:
        print "You can also give filename as a command line argument"
        filename = raw_input("Enter Filename: ")
    else:
        filename = sys.argv[1]

    counter = 0
    inp_list = file_to_list(filename)
    #print("Original: %s\n" % inp_list)
    merge(inp_list)
    print("Merged in %s operations\n" % (counter))

# merge sort
def merge(inp_list):
    global counter
    length = len(inp_list)
    if length > 1:
        # set middle and split array
        mid = length / 2
        left = inp_list[:mid]
        right = inp_list[mid:]

        # recursive calls
        merge(left)
        merge(right)

        # pointers
        i = 0
        j = 0
        k = 0

        # main loop
        #print(">  Splitting: %s" % inp_list)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                inp_list[k] = left[i]
                i += 1
                counter += 1
            else:
                inp_list[k] = right[j]
                j = j + 1
                counter += 1
            k += 1

        # clean up
        while i < len(left):
            inp_list[k] = left[i]
            i += 1
            k += 1
            counter += 1

        while j < len(right):
            inp_list[k] = right[j]
            j += 1
            k += 1
            counter += 1
        #print(counter)
    #print(">    Merging: %s" % inp_list)

def file_to_list(path):
    list = []
    with open(path, 'r') as f:
        for line in f:
            list.append(int(line))
    return list

counter = 0
if __name__ == "__main__":
    main()
