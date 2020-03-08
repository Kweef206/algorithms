"""
Given a string, find the length of the longest substring
without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""


def longest_non_repeat(string):
    substrings = []
    ongoing = []
    for i in range(len(string)):
        for j in range(len(substrings)):
            if j not in ongoing:
                continue
            if string[i] in substrings[j]:
                ongoing.remove(j)
            else:
                substrings[j] += string[i]
        substrings.append(string[i])
        ongoing.append(len(substrings) - 1)
    index = max([(i, len(s)) for i, s in enumerate(substrings)], key=lambda x: x[1])[0]
    substring = substrings[index]
    return substring, len(substring)


def main():
    print(longest_non_repeat("abcabcbb"))
    print(longest_non_repeat("bbbbb"))
    print(longest_non_repeat("pwwkew"))


if __name__ == "__main__":
    main()