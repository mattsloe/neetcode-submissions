class Solution:

    def encode(self, strs: List[str]) -> str:
        numOfStrings = len(strs)
        # prepend the number of strings as a 3 digit ###
        msg = "{:03}".format(len(strs))
        for str in strs:
            # prepend the length of the string as a 3 digit ###
            encoded_string = "{:03}".format(len(str)) + str
            # add the str into msg
            msg += encoded_string
        return msg

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        # read number of strings
        num_of_strings = int(s[:3])
        s = s[3:] #pop off this
        # iterate 
        for i in range(num_of_strings):
            msg_length = int(s[:3])
            msg = s[3:msg_length + 3]
            decoded_strings.append(msg)
            # Move the pointer forward to the next string segment
            s = s[3 + msg_length:]
        return decoded_strings
