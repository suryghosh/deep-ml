def valid_palindrome(s):
    # s: a string of lowercase letters
    # return True or False
    counter = 0
    left = 0
    right = len(s)-1
    if right==0:
        return True
    elif right>=1:
        while(left<right):
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                counter +=1
                if counter>1:
                    return False
                left = left+1
                if s[left]==s[right]:
                    continue
                left = left-1
                right = right-1
                if s[left]==s[right]:
                    continue
                return False
    if counter<=1:
        return True
    else:
        return False

    pass