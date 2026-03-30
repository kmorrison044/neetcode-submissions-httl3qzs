class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "Empty List"
        else:
            return "*&^".join(strs)

    def decode(self, s: str) -> List[str]:
        if s != "Empty List":
            return s.split("*&^")
        else:
            return []
