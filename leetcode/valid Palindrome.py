def isPalindrome(s) -> bool:
    strs = []
    for char in s:
        # isalnum() -> 문자열이 영어, 한글, 혹은 숫자로 되어있으면 참 리턴, 아니면 거짓리턴
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True
s = "race a car"
print(isPalindrome(s))
