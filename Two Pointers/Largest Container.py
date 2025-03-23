# O(n^2)

def largest_container(heights):
    n = len(heights)
    max_water = 0
    for i in range(n):
        for j in range(i+1, n):
            water = min(heights[i], heights[j]) * (j - i)
            max_water = max(water, max_water)

    return max_water



# O(n)

def largest_container(heights):
    max_water = 0
    left = 0
    right = len(heights) - 1
    while (left < right):
        water = max(max_water, water)

        if (heights[left] < heights[right]):
            left += 1

        elif heights[left] > heights[right]:
            right -= 1

        else:
            left += 1
            right -= 1
    
    return max_water


