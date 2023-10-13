#!/usr/bin/env python3

class Solution:
    def longestCommonPrefix(self, v):
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

#         wrong solution
#         strs_len = []
#         for str in strs:
#             strs_len.append(len(str))
# 
#         smallest_string = min(strs_len)
#         print(smallest_string)
# 
#         prefix = ""
#         for i in range(smallest_string):
# 
#             current_char = ""
#             prefix_done = False
#             for str in strs:
#                 if current_char == "":
#                     current_char = str[i]
#                     continue
#                 elif str[i] != current_char:
#                     prefix_done = True
#                     break
# 
#             if prefix_done:
#                 prefix += current_char
#                 prefix_done = False
#                 break
# 
#         return prefix


if __name__ == "__main__":
    substirng = Solution().longestCommonPrefix(["flower","flow","flight"])
    print(substirng)
