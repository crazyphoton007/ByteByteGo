# Sliding window
# O()

def first(haystack, needle):
    m = len(needle)
    n = len(haystack)

    for window in range(n - m + 1):
        for i in range(m):
            if needle[i] != haystack[window + i]:
                break

            if i == m - 1:
                return window
    return -1



if __name__ == '__main__':
    haystack = "leetcode"
    needle = "et"

    result = first(haystack, needle)
    print(result)