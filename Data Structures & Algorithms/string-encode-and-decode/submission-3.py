class Solution:

    def encode(self, strs: List[str]) -> str:
        str_lengths = ""
        all_strs = ""
        for s in strs:
            str_lengths += str(len(s)) + ","
            all_strs += s
        final_encode = str_lengths + "#" + all_strs
        print(final_encode)
        return final_encode

    def decode(self, s: str) -> List[str]:        
        i = 0
        seen_delimeter = False
        
        lens = []
        curr_len = ''

        res = []
        curr_word = ''
        curr_word_ix = 0

        # Phase 1: parse lengths
        while not seen_delimeter:
            if s[i] == "#":
                seen_delimeter = True
            elif s[i] != ',':
                curr_len += s[i]
            else:
                lens.append(int(curr_len))
                curr_len = ''
            i += 1

        # Phase 2: extract words based on lens
        while curr_word_ix < len(lens):
            end_i = i + lens[curr_word_ix]
            res.append(s[i:end_i])
            i = end_i
            curr_word_ix += 1

        return res
