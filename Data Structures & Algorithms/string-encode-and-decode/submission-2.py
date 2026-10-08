class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + "#" + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 

            str_length = int(s[i:j])

            start = j + 1 
            word = s[start: start+str_length]
            result.append(word)

            i = start + str_length
        
        return result

