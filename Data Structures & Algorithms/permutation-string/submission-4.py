class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        st1=[0]*26
        st2=[0]*26
        for i in s1:
            st1[ord(i)-ord('a')]+=1

        for i in range(0,len(s2)):
            st2[ord(s2[i])-ord('a')]+=1
            if i>len(s1)-1:
                st2[ord(s2[i-len(s1)])-ord('a')]-=1
            if st1==st2:
                return True

        return False