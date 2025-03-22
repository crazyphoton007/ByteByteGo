
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
                    print(triplet)


                    triplets.add(triplet)


    return [list(triplet) for triplet in triplets]



if __name__ == '__main__':
    nums = [0, -1, 2, -3, 1]
    
    result = triplet_sum(nums)
    print(result)


# Triplet Sum
# O(n^3)

def triplet_sum(nums):
    triplets = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        pairs = pair_sum(nums, i+1, -nums[i])

        for pair in pairs:
            triplets.append([nums[i]] + pair)


    return triplets

def pair_sum(nums, start, target):
    pairs = []
    left = start
    right = len(nums)-1
    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            pairs.append([nums[left], nums[right]])
            left +=1

            while left < right and nums[left] == nums[left - 1]:
                left += 1

        elif sum < target:
            left += 1

        else:
            right -= 1

    return pairs



if __name__ == '__main__':
    nums = [-2, -1, -1, 1, 2, 2]
    
    result = triplet_sum(nums)
    print(result)














