class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        # print(countT)
        
        res, resLen, curLen = [-1, -1], float("infinity"), 0

        l = 0
        for r in range(len(s)):
            cur = s[r]
            window[cur] = 1 + window.get(cur, 0)
            # print(window)
            if cur in countT and window[cur] == countT[cur]:
                curLen += 1
            # print(curLen, len(countT))
            while curLen == len(countT):
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                # print(s[l], window)
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    curLen -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

