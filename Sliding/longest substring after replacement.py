def longest_substring_replacement(s, k):


    freq = {}
    highest_freq = 0
    max_len = 0

    left = 0
    right = 0

    while right < len(s):

        freq[s[right]] = freq.get(s[right], 0) + 1       #   this checks if the character   already  exists in the dictionary freq and if it does not then return 0
        highest_freq = max(highest_freq, freq[s[right]])
        
        num_chars_to_replace = (right - left + 1) - highest_freq

        if num_chars_to_replace > k:

            freq[s[left]] -= 1       
            left += 1                                #shrink  window

        max_len = right- left + 1  #expand window

        right += 1

    return max_len


if __name__ == '__main__':
    s = "caabab"

    result = longest_substring_replacement("aabcdcca", 2)
    print(f"longest substring after replacement", {result})