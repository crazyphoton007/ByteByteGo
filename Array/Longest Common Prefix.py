# Longest Common Prefix

def longestCommonPrefix(str):
    res = ""
    for i in range(len(str[1])):
        for s in str:
            if i == len(s) or s[i] != str[1][i]:
                return res
            
        res += str[1][i]

    return res


if __name__ == '__main__':
    str = ["vikas", "vik", "vi"]

    result = longestCommonPrefix(str)
    print(result)
