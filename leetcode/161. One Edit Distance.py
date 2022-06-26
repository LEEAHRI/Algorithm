def isOneEditDistance(self, s: str, t: str) -> bool:
    s_size = len(s)
    t_size = len(t)
    count = 0
    if s == t or abs(s_size - t_size) > 1: return False
    if s_size == t_size:
        for i in range(s_size):
            if s[i] != t[i]:
                count += 1
            if count > 1: return False
        return True
    elif s_size > t_size:
        for i in range(t_size):
            if t[i] != s[i] and t[i] != s[i + 1]:
                return False
    else:
        for i in range(s_size):
            if s[i] != t[i] and s[i] != t[i + 1]:
                return False
    return True