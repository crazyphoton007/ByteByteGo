def longest_substring_with_unique_chars(s):

    max_len = 0
    hash_set = set()

    left = 0
    right = 0

    while right < len(s):
        
        while s[right] in hash_set:
            hash_set.remove(s[left])
            left += 1

        max_len = max(max_len, right - left + 1)


        hash_set.add(s[right])
        right += 1

    return max_len


if __name__ == '__main__':
    s = "caabab"

    result = longest_substring_with_unique_chars(s)
    print(f"longest substring: {result}")

    # print(f"Last word: {last}, count: {count}")