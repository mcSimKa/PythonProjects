class Pattern:
    def match_string(self, s: str):
        for symbol in self.pattern:
            if not self.apply_pattern(symbol, s):
                return False
        return self.application_covers_all(s)

    def application_covers_all(self, s: str):
        return self.max_reached == len(s) - 1

    def list_covered_by_previous_symbol(self) -> list:
        return self.applications[-2]

    def apply_pattern(self, symbol: list, s: str):
        def single_symbol():
            return (symbol[1] != '*')

        if single_symbol():
            self.applications.append([])
        else:
            self.applications.append([self.applications[-1][0]])

        matched = False

        for start_from in self.list_covered_by_previous_symbol():
            shift = 1
            while start_from + shift < len(s):
                if (s[start_from+shift] == symbol[0]) or (symbol[0] == '.'):
                    self.applications[-1].append(start_from+shift)
                    matched = True
                if single_symbol() or not matched:
                    break
                shift += 1

        if not matched:
            if single_symbol():
                return False
            else:
                self.applications.remove(self.applications[-1])

        self.fix_max_reached()
        return True

    def fix_max_reached(self):
        self.max_reached = max(self.max_reached, self.applications[-1][-1])


    def parse(self, p: str) -> list:
        result = []
        for char in p:
            if char == '*':
                result[-1][1] = '*'
            else:
                result.append([char, ''])
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
    test("a", ".*..a*", False)
    test("bbbba", ".*a*a", True)
    test("ab", ".*..", True)
    test("", ".*", True)
    test("a", ".*..a*", False)
    test("aaabbb", "a*b*....", True)
    test("aaabbb", "a*b*a...", True)
    test("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s", True)


test("abcd", "d*", False)
test("bbbba", ".*a*a", True)
test_all()
# test("a", ".*..a*", False)
