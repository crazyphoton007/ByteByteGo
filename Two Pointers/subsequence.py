def subsequence(s, t):
    left = 0
    right = 0

    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1

        right += 1

    return True if left == len(s) else False



if __name__ == '__main__':
    s = "vik"
    t = "dkkdvik"
    result = subsequence(s, t)
    print(result)

    