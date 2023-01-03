import numpy

def removeduplicates(nums): 
    latnum = None # latest int from nums
    n = 0 # index
    numlen = (len(nums)-1)
    
    while(n <= numlen):
        print(f"numlen is now:{numlen}")
        print(f"index n is: {n}")
        print(f"the complete list i {nums}")
        if nums[n] != latnum: # if unique number
            latnum = nums[n]
            print(f"last unique number is {latnum}")
            n += 1
        else: #if found duplicate
           nums.pop(n)
           numlen -= 1
    print(nums) 

    #print(nums)
    print(f"Amount of unique elements are: {len(nums)}")
    return()


def main(): 
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    removeduplicates(nums)

if __name__ == "__main__":
    main()




