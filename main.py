class Patterns:
    def __init__(self):
        self.my_patterns = []

    def __init__(self, given_pattern: str):
        self.my_patterns = []
        self.parse_string(given_pattern)

    def add_pattern(self, given_char):
        self.my_patterns.append(given_char)

    def parse_string(self, given_string: str):
        for i in range(len(given_string)):
            if given_string[i] == '*':
                self.my_patterns[-1] += '*'
            else:
                self.add_pattern(given_string[i])

    def list_single(self):
        return [single_pattern for single_pattern in self.my_patterns if len(single_pattern) == 1]

    def list_asterisk(self):
        return [single_pattern for single_pattern in self.my_patterns if len(single_pattern) > 1]

    def __str__(self):
        return ",".join([str(element) for element in self.my_patterns])


class Solution:

    def isMatch(self, s: str, з: str) -> bool:
        def reached_end():
            return position_in_pattern == len(pattern) - 1

        def pattern_was_single_char():
            return (len(processed_p) > 0 and len(processed_p[-1][0]) == 1)

        def attempt_to_takefirst():
            return (position_in_pattern < 0)

        def get_last_processed_char():
            return processed_p[-1][0][0]

        def get_count_asterisks_used():
            return processed_p[-1][1]

        def is_last_asterisk_applied():
            return len(processed_p[-1][0])>1

        def covered_by_previouse_pattern_asterisked_char():
            return get_last_processed_char() == pattern[position_in_pattern] and get_count_asterisks_used() > 0

        def decrement_pattern_asterisked_char():
            processed_p[-1][1] -= 1
            return processed_p[-1][1] > 0

        def asterisk_pattern_nolonger_matches():
            return len(processed_p)>0 and pattern[position_in_pattern] == processed_p[-1][0]

        def is_pattern_char_checked_asterisk():
            return len(pattern[position_in_pattern])>1

        def get_next_pattern_symbol():
            nonlocal position_in_pattern
            if not reached_end():
                if pattern_was_single_char() or attempt_to_takefirst():
                    position_in_pattern += 1
                    return True
                else:
                    if is_matched:
                        return True
                    else:
                        if (is_ptrn_an_asterisk()) and (len(processed_p) == 0):
                            position_in_pattern += 1
                            return True
                        if is_pattern_char_checked_asterisk() and asterisk_pattern_nolonger_matches():
                            position_in_pattern += 1
                            return True
                        if covered_by_previouse_pattern_asterisked_char():
                            if decrement_pattern_asterisked_char():
                                position_in_pattern += 1
                                return True

            return False

        def store_processed_string():
            nonlocal processed_s
            processed_s.append([string[position_in_string], position_in_pattern])

        def store_processed_pattern():
            nonlocal processed_p
            if (len(processed_p) > 0) and (get_last_processed_char() == pattern[position_in_pattern][0]) and (is_last_asterisk_applied()):
                processed_p[-1][1] += 1
            else:
                processed_p.append([pattern[position_in_pattern], 1])

        def next_character() -> bool:
            nonlocal position_in_string
            if position_in_string < len(string) - 1:
                position_in_string += 1
                return True
            else:
                return False

        def is_ptrn_an_asterisk():
            return len(pattern[position_in_pattern]) == 2

        def match(char_exist, char_pattern):
            return char_exist == char_pattern or char_pattern == '.'

        def get_next_string_symbol():
            nonlocal position_in_string

            def found_unprocessed_char_in_string():
                return len(processed_s) < len(s)

            if found_unprocessed_char_in_string():
                if is_matched:
                    position_in_string += 1
                return True
            else:
                return False

        def store_matched():
            store_processed_string()
            store_processed_pattern()

        def ready_to_continue():
            if is_matched:
                return True
            else:
                if len(processed_p) > 0 and len(processed_p[-1]) > 1:
                    return True
                else:
                    return False

        def check_completed():
            if (position_in_pattern == len(pattern) - 1 and len(processed_s) == len(s)) or (
                    len(pattern) == len(string) == 0):
                return True
            else:
                return False

        position_in_string = -1
        position_in_pattern = -1
        #last_checked_p = 0
        processed_s = []
        processed_p = []
        pattern = Patterns(з).my_patterns
        string = list(s)
        is_matched = True
        while True:
            if get_next_pattern_symbol():
                if get_next_string_symbol():
                    is_matched = False
                    if match(string[position_in_string], pattern[position_in_pattern][0]):
                        store_matched()
                        is_matched = True
                else:
                    is_matched = False
            else:
                break
        return check_completed()



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


test('a', "c*a", True)
test_all()
# test("a", ".*..a*", False)
