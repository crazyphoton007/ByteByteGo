
# Triplet Sum
# O(n^3)

def triplet_sum(nums):
    n = len(nums)
    triplets = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i]+nums[j]+nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))


                    triplets.add(triplet)


    return [list(triplet) for triplet in triplets]



if __name__ == '__main__':
    nums = [0, -1, 2, -3, 1]
    
    result = triplet_sum(nums)
    print(result)
