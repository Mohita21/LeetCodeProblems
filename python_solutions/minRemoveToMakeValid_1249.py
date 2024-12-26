class Solution():
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        st = ""
        c = 0
        c2 = 0
        stack = []
        for idx,i in enumerate(s):
            if i == '(': 
                stack.append(idx)
                c += 1
            elif i == ')':
                if len(stack) > 0:
                    k = stack.pop()
                    b = st[k-c +1+c2:]
                    st = st[:k-c+1+c2] + '(' + b
                    st = st + i
                    c2 += 1
                else:
                    c += 1
                
            elif i != ')' :
                st = st + i
        return st


if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    print(Solution().minRemoveToMakeValid(s))
    s = "a)b(c)d"
    print(Solution().minRemoveToMakeValid(s))
    s = "))(("
    print(Solution().minRemoveToMakeValid(s))
    s = "(a(b(c)d)"
    print(Solution().minRemoveToMakeValid(s))
