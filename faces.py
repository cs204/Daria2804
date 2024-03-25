def convert(s):
    s = s.replace(":)", "\N{Slightly Smiling Face}")
    s = s.replace(":(", "\N{Slightly Frowning Face}")
    return(s)
def replace():
    a = input()
    b = convert(a)
    print(b)
replace()
