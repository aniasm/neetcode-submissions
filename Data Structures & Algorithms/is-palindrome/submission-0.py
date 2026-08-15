class Solution:
    def isPalindrome(self, s: str) -> bool:
        j=len(s)-1
        for i in range(j):
            if s[i].isalnum():
                while s[j].isalnum()==False:
                    j-=1
                else:
                    if s[i].lower() != s[j].lower():
                        return False
                    j-=1
            else:
                break
        return True
        