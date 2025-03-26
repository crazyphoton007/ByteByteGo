# dark moon

from operator import __not__


def lastWord(s):
    i = len(s)-1
    count = 0
    last =  ""

    while i >= 0 and s[i] == " ":
        i -= 1

    while i >= 0 and s[i] != " ":
        last = s[i] + last
        count += 1

        i -= 1
    return count, last


if __name__ == '__main__':
    s = "vikas is great"
    last, count = lastWord(s)

    print(f"Last word: {last}, count: {count}")












