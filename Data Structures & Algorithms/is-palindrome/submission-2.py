class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_list = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        n=""
        for car in s:
            if car in alphanumeric_list:
                n+=car.lower()
        for i in range(len(n)//2) :
            j=len(n)-i-1
            if n[i]!=n[j] :
                return False
        return True