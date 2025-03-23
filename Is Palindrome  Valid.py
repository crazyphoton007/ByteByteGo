def is_palindrome(s):
    left = 0
    right = len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():

            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False
        
        left  += 1
        right -= 1

    return True


if __name__ == '__main__':
    s = "nitin"
    result = is_palindrome(s)
    print(result)


# Time Complexity:  O(n)
