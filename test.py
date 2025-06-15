from collections import defaultdict

def majorityElement(nums):


        n = len(nums)
        m = defaultdict(int)
        
        for num in nums:
            m[num] += 1
        print("vikas", m)
        
        n = n // 2
        for key, value in m.items():
            if value > n:
                return key
        
        return 0


if __name__ == '__main__':
    nums = [2, 2, 4, 2]

    result = majorityElement(nums)
    print(result)


