class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_s = []
        for elem in strs:
            ret_s.append(elem)
            ret_s.append('😊')
        return ''.join(ret_s)

    def decode(self, s: str) -> List[str]:
        ret_s = []
        acc = []
        for char in s:
            if char != '😊':
                acc.append(char)
            else:
                acc = ''.join(acc)
                ret_s.append(acc)
                acc = []

        return ret_s
