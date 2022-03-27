def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""

    # Sort str list
    strs.sort(key=len)

    """
    Starting from the first word, we grab the first letter and iterate through each subsequent word and compare the ith
    index letter. If it is the same till the end, we then append, otherwise we return whatever we have currently 
    concatenated.
    """
    current_letter = ""
    previous_letter = ""
    for i in range(len(strs[0])):
        current_letter = strs[0][i]
        previous_letter = current_letter
        for j in range(len(strs)):
            current_letter = strs[j][i]
            if current_letter == previous_letter:
                continue
            else:
                return ans
        ans += current_letter

    return ans


if __name__ == '__main__':
    test_str = ["a"]
    print(longestCommonPrefix(test_str))
    exit()
