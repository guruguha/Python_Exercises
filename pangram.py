str = str(input().strip())
char_set = set()

for char in str:
    if char.isalpha():
        char = char.upper()
        char_set.add(char)
if len(char_set) == 26:
    print("pangram")
else:
    print("not pangram")
