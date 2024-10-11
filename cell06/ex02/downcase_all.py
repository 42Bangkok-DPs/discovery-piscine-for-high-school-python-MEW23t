def downcase(string=None):
    if string is None:
        return "none"
    return string.lower()

param = downcase("HELLO")
print(param)

without = downcase()
print(without)
