class Solution:
    def isMatch_new(self, s: str, p: str) -> bool:
        def get_next_p(p_position: int):
            if p_position < 0:
                return False,'', False, -1
            if p_position == 0:
                return True, p[p_position], -1
            if p[p_position] == '*':#getting the lenghts of the same characters in the * pattern
                return True, p[p_position-1], True, p_position-2
            else:
                return True, p[p_position], False, p_position-1

        s_position = len(s)-1
        next_pattern_exist, pattern, is_star, next_p = get_next_p(len(p)-1)

        while next_pattern_exist:
            if s[s_position] == pattern or pattern == '.':
                s_position -= 1
                if s_position == 0:
                    if next_p == -1 or next_p == 0:
                        return True
                    else:
                        return False
                if not is_star:
                    next_pattern_exist, pattern, is_star, next_p = get_next_p(next_p)
            else:
                if is_star:
                    next_pattern_exist, pattern, is_star, next_p = get_next_p(next_p)
                else:
                    return False
        return False

    def isMatch_old(self, s: str, p: str) -> bool:
        def get_next_p(position_p : int):
            if position_p+1 < len(p):
                return p[position_p+1]
            else:
                return p[position_p]

        position_p = 0
        position_s = 0
        length_p = len(p)
        length_s = len(s)
        while position_p < length_p and position_s < length_s:
            #point to the next symbol in the s string to check, if that is a beginning then position_s=0
            if s[position_s] == p[position_p] or p[position_p] == '.':
                if get_next_p(position_p) != '*':
                    position_p += 1
            else:
                if get_next_p(position_p) == '*':
                    #move to the next pattern after * but return back in one position in the string because the symbol in s does not matches
                    if position_p + 2 < length_p and p[position_p] != p[position_p+2]:
                        position_p += 2
                    else:
                        position_p += 3
                    continue
                    #we do not move to the next s symbol but checking
                else:
                    return False
            position_s += 1

        if position_p + 2 == length_p and get_next_p(position_p) == '*':
            position_p += 2

        if position_p + 2 < length_p and p[position_p] == p[position_p + 2]:
            position_p += 3

        if position_s == length_s and position_p == length_p:
            return True
        else:
            return False

    def isMatch3(self, s: str, p: str) -> bool:
        def get_next_p(p_position : int):
            pattern_checked = 0
            if p_position == len(p):# there is no pattern left
                return False, '', False, len(p), pattern_checked
            if p_position + 1 == len(p):# only last symbol in the pattern
                return True, p[p_position], False, len(p), pattern_checked
            if p[p_position + 1] == '*':#getting the lenghts of the same characters in the * pattern
                for i in range(p_position+2,len(p)):
                    if p[i] == p[p_position]:
                        pattern_checked -= 1
                    else:
                        break
                return True, p[p_position], True, p_position + 2, pattern_checked
            else:
                return True, p[p_position], False, p_position + 1, pattern_checked

        s_position = 0
        next_pattern_exist, pattern, is_star, next_p, pattern_checked = get_next_p(0)

        while next_pattern_exist:
            if s[s_position] == pattern or pattern == '.':
                pattern_checked += 1
                s_position += 1
                if s_position == len(s):
                    if next_p>= len(p):
                        return True
                    else:
                        #there are still patter left. Shall we go through it?
                        if is_star:
                            s_position -= 1
                            next_pattern_exist, pattern, is_star, next_p, pattern_checked = get_next_p(next_p)
                            continue
                        else:
                            #try to eat it until the end
                            next_pattern_exist, pattern, is_star, next_p, pattern_checked = get_next_p(next_p)
                            while next_p < len(p):
                                next_pattern_exist, pattern, is_star, next_p, pattern_checked = get_next_p(next_p)
                            if is_star:
                                return True
                            else:
                                return False
                if not is_star:
                    next_pattern_exist, pattern, is_star, next_p, pattern_checked = get_next_p(next_p)
            else:
                if pattern_checked > 0 or is_star:
                    old_pattern = pattern
                    while old_pattern == pattern:
                        next_pattern_exist, pattern, is_star, next_p, pattern_checked = get_next_p(next_p)
                else:
                    return False
        return False

    def isMatch(self, s: str, p: str) -> bool:
        def get_next_p(p_position : int):
            if p_position == len(p):# there is no pattern left
                return False, '', False, len(p)
            if p_position + 1 == len(p):# only last symbol in the pattern
                return True, p[p_position], False, len(p)
            if p[p_position + 1] == '*':#getting the lenghts of the same characters in the * pattern
                return True, p[p_position:p_position+1], True, p_position + 2
            else:
                return True, p[p_position], False, p_position + 1
        s_position = 0
        next_pattern_exist, pattern, is_star, next_p = get_next_p(0)
        result = []
        p_result = -1
        if s_position == len(s):
            p_result = len(result) - 1
            while next_p < len(p):
                # evaluate the rest of pattern vs the last coverage
                # skip all the patterns that fits to the last one applied? But move backwords for those that had been used for match
                next_pattern_exist, pattern, is_star, next_p = get_next_p(next_p)
                # skip all stars because they have no value
                if is_star:
                    continue
                if result[p_result][0] != pattern and pattern != '.':
                    if is_star:
                        continue
                    else:
                        return False
                # move back in result list if star was used for the symbol to match the pattern
                if (result[p_result][0] == pattern or pattern == '.') and result[p_result][2]:
                    p_result -= 1
                    if p_result < -1:
                        return False
                else:
                    return False
            return True
        while next_pattern_exist:
            if s[s_position] == pattern or pattern == '.':
                result.append([s[s_position],pattern,is_star])
                p_result = -1
                s_position += 1
                if s_position == len(s):
                    p_result = len(result) - 1
                    while next_p < len(p):
                        # evaluate the rest of pattern vs the last coverage
                        # skip all the patterns that fits to the last one applied? But move backwords for those that had been used for match
                        next_pattern_exist, pattern, is_star, next_p = get_next_p(next_p)
                        #skip all stars because they have no value
                        if is_star:
                            continue
                        if result[p_result][0] != pattern and pattern != '.':
                            if is_star:
                                continue
                            else:
                                return False
                        #move back in result list if star was used for the symbol to match the pattern
                        if (result[p_result][0] == pattern or pattern == '.') and result[p_result][2]:
                            p_result -= 1
                            if p_result<-1:
                                return False
                        else:
                            return False
                    return True
                if not is_star:
                    next_pattern_exist, pattern, is_star, next_p = get_next_p(next_p)
            else:
                if is_star:
                    next_pattern_exist, pattern, is_star, next_p = get_next_p(next_p)
                else:
                    if len(result)>0:
                        if (result[p_result][0] == pattern or pattern == '.') and result[p_result][2]:
                            p_result -= 1
                            next_pattern_exist, pattern, is_star, next_p = get_next_p(next_p)
                            continue
                    return False
        return False

def test(s: object, p: object, expected: object) -> object:
    sol = Solution()
    test_result = sol.isMatch(s, p)

    print("Input %r pattern %r expected %r returned %r this is %r" % (s, p, expected, test_result, (test_result == expected)))

def test_all():
    test("aaa","ab*a*c*a", True)
    test("a","ab*", True)
    test("abcd","d*",False)
    test("mississippi","mis*is*ip*.",True)
    test("aa","aa", True)
    test("aaa","aaaa", False)
    test("aaa","a*a", True)
    test("aa","a*", True)
    test("aa","a", False)
    test("ab",".*", True)
    test('a',"c*a",True)
    test("baab","ba*ab",True)
    test("baab","ba*aab",True)
    test("baab","ba*aaab",False)
    test("bab","ba*ab",True)
    test("a",".*..a*",False)
    test("bbbba",".*a*a",True)
    test("ab", ".*..", True)

test_all()
#test("a", ".*..a*", False)
test("", ".*", True)