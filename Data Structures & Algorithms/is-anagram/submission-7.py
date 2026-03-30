class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)

        def build_dict(text):
            text_dict = {}
            for ch in text:
                if ch not in text_dict:
                    text_dict[ch] = 1
                else:
                    text_dict[ch] += 1
            return text_dict
        
        s_dict = build_dict(s)
        t_dict = build_dict(t)

        return s_dict == t_dict