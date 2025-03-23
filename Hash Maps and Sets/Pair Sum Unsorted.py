def pair_sum_unsorted(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [num_map[target-num], i]
        
        num_map[num] = i

    return []





if __name__ == '__main__':
    nums = [-1, 3, 4, 2]
    target = 1

    result = pair_sum_unsorted(nums, target)
    print(result)
