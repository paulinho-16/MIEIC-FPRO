def palindrome_index (s):
    def palindrome(s):
        s_reversed = s[::-1]
        if s == s_reversed:
            return True
        else:
            return False
    if palindrome(s) == True:
        return -1
    for i in range(len(s)):
        palavra = s[:i] + s[i+1:]
        if palindrome(palavra) == True:
            return i
    return -1           