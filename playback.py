def urlify (s):
    s = s.strip().split(" ")
    return ("...").join(s)
print(urlify("It is test."))
