class Solution:
    # brainstorm
        # we have to find a way to encode a string in such a way that we don't decode it incorrectly

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += s.encode('utf-8').hex() + "G"
        return new_str

    def decode(self, s: str) -> List[str]:
        strs = s.split("G")
        res = []
        for s in strs:
            res.append(bytes.fromhex(s).decode('utf-8'))
        res.pop()
        return res
