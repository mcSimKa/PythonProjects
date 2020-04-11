class Pattern:

    def match_string(self, s: str) -> bool:
        len_s = len(s)
        for index_symbol, symbol in enumerate(self.pattern):
            to_be_removed = []
            for index_application, position in enumerate(self.applications):
                if (position + 1 < len_s) and ((self.pattern[index_symbol][0] == '.') or (self.pattern[index_symbol][0] == s[position + 1])):
                #if self.char_matches_symbol(position + 1, index_symbol):
                    if (symbol[1] == '*'):
                        self.applications.append(position+1)
                    else:
                        self.applications[index_application] += 1
                else:
                    if not (symbol[1] == '*'):
                        to_be_removed.append(index_application)
            if len(to_be_removed) > 0:
                to_be_removed.sort(reverse=True)
                for index_removed in to_be_removed:
                    del self.applications[index_removed]
            self.applications = list(set(self.applications))
            self.applications.sort()

        if len(self.applications) >  0:
            self.applications.sort()
            max_reached = self.applications[-1]
            return max_reached == len(s)-1
        else:
            return False

    def __init__(self, p: str):
        pattern = []
        for char in p:
            if char == '*':
                pattern[-1][1] = '*'
                if (len(pattern) > 1) and (pattern[-2][1] == '*') and (pattern[-1][0] == pattern[-2][0]):
                    del pattern[-1]
            else:
                pattern.append([char, ''])
        self.pattern = pattern
        self.applications = [-1]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = Pattern(p)
        return pattern.match_string(s)


def test(s: object, p: object, expected: object) -> object:
    sol = Solution()
    test_result = sol.isMatch(s, p)

    print("Input %r pattern %r expected %r returned %r this is %r" % (
        s, p, expected, test_result, (test_result == expected)))


def test_all():
    test("baab", "ba*ab", True)
    test("baab", "ba*aab", True)
    test("baab", "ba*aaab", False)
    test("a", "ab*", True)
    test("abcd", "d*", False)
    test("mississippi", "mis*is*ip*.", True)
    test("aaa", "a*a", True)
    test("aa", "aa", True)
    test("aaa", "ab*a*c*a", True)
    test("aaa", "aaaa", False)
    test("aaa", "a*a", True)
    test("aa", "a*", True)
    test("aa", "a", False)
    test("ab", ".*", True)
    test('a', "c*a", True)
    test("bab", "ba*ab", True)
    test("bbbba", ".*a*a", True)
    test("ab", ".*..", True)
    test("", ".*", True)
    test("a", ".*..a*", False)
    test("aaabbb", "a*b*....", True)
    test("aaabbb", "a*b*a...", True)
    test("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s", True)
    test("bbba", ".*b", False)
    test("abbcacbbbbbabcbaca", "a*a*.*a*.*a*.b*a*", True)
    test("abbcacbbbbbabcbaca", "a*a*.*a*.*a*.b*a*", True)
    test("", ".", False)


test("a", ".*..a*", False)
test_all()
