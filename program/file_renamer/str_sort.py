def contains_special_chars(s):
    special_chars = ['?', '/', '\\', '<', '>', '*', '|', ':']

    for char in special_chars:
        if char in s:
            return True

    return False


s1 = "This is a test string."
print(contains_special_chars(s1))  # 输出: False

s2 = "Hello, world!"
print(contains_special_chars(s2))  # 输出: False

s3 = "Check this string with ? and :"
print(contains_special_chars(s3))  # 输出: True

s4 = "Some <random> *string* |with\\ special characters."
print(contains_special_chars(s4))  # 输出: True
