class Pattern:
    def match_string(self, s: str):
        for symbol_pos in range(len(self.pattern)):
            if not self.apply_pattern(symbol_pos, s):
                return False
        return self.application_covers_all(s)

    def application_covers_all(self, s: str):
        return self.max_reached == len(s) - 1

    def single_symbol(self, position: int) -> bool:
        return self.pattern[position][1] != '*'

    def list_covered_by_previous_symbol(self, symbol_pos) -> list:
        result = self.applications[symbol_pos]
        while symbol_pos > 0 and not self.single_symbol(symbol_pos-1):
            symbol_pos -= 1
            result = self.applications[symbol_pos] + result
        return list(set(result))

    def build_single_path(self, symbol_pos: int, s: str):
        def append_application():
            self.applications[-1].append(start_from + shift)
            return True

        def compare():
            return (s[start_from+shift] == self.pattern[symbol_pos][0]) or (self.pattern[symbol_pos][0] == '.')

        matched = False
        previous_symbol_matches = self.list_covered_by_previous_symbol(symbol_pos)
        for start_from in previous_symbol_matches:
            shift = 1
            while start_from + shift < len(s):
                if compare():
                    matched = append_application()
                    if self.single_symbol(symbol_pos):
                        break
                else:
                    break
                shift += 1
        return matched

    def apply_pattern(self, symbol_pos: int, s: str):
        self.applications.append([])
        if not self.build_single_path(symbol_pos, s):
            if self.single_symbol(symbol_pos):
                return False

        if len(self.applications[-1]) > 0:
            if self.single_symbol(symbol_pos) and self.pattern[symbol_pos][0] != '.':
                self.applications[-1].sort()
                self.max_reached = self.applications[-1][-1]
            else:
                self.applications[-1].sort()
                self.max_reached = max(self.max_reached, self.applications[-1][-1])
        return True



    def parse(self, p: str) -> list:
        result = []
        for char in p:
            if char == '*':
                result[-1][1] = '*'
            else:
                result.append([char, ''])
        i = 0
        while i < len(result)-1:
            if result[i][0] == result[i+1][0] and result[i][1] == result[i+1][1] == '*':
                del result[i+1]
            i += 1

        return result

    def __str__(self):
        return self.pattern

    def __init__(self, p: str):
        self.pattern = self.parse(p)
        self.applications = [[-1]]
        self.max_reached = -1


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
    test("bbba",".*b", False)
    test("abbcacbbbbbabcbaca","a*a*.*a*.*a*.b*a*",True)
    test("abbcacbbbbbabcbaca","a*a*.*a*.*a*.b*a*",True)

test("bcbabcaacacbcabac","a*c*a*b*.*aa*c*a*a*", True)
test_all()
