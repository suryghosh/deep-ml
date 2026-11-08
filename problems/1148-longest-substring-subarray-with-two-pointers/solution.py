def longest_unique_substring(s):
    # s: a string
    # return an integer length
    seen = set()
    left=0
    right=0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        
        seen.add(s[right])
        curr_length = right-left+1
        max_length = max(curr_length,max_length)
    return max_length
    pass