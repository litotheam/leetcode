class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        left = 0
        right = 0

        output_length = 10e5+1

        dict_s = {}
        dict_t = {}
        for c in t:
            if c not in dict_t:
                dict_t[c] = 1
            else:
                dict_t[c] += 1

        if m < n:
            output = ""
        else:
            for right in range(m):
                if s[right] not in dict_s: 
                    dict_s[s[right]] = 1
                else:
                    dict_s[s[right]] += 1

                while(True):
                    is_included = True
                    for key, value in dict_t.items():
                        if key not in dict_s or value > dict_s[key]:
                            is_included = False
                            break

                    if is_included == False:
                        break
                    else:
                        if len(s[left:right+1]) < output_length:
                            output = s[left:right+1]
                            output_length = len(output)
                        dict_s[s[left]] -= 1
                        if dict_s[s[left]] == 0:
                            dict_s.pop(s[left])
                        left += 1

        if output_length == 10e5+1:
            output = ""

        return output