vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def halvesAreAlike(s: str):
    half = int(len(s) / 2)
    a = s[:half]
    b = s[half::]
    # print(f"part 1 -> {s[:half]}, part 2 -> {s[half::]}")
    c1, c2 = (0, 0)
    for vowel in vowels:
        c1 += a.count(vowel)
        c2 += b.count(vowel)
    # print(f"count -> a = {c1} and b = {c2}")
    return True if c1 == c2 else False


s1 = "book"
s2 = "textbook"
s3 = "MerryChristmas"
s4 = "AbCdEfGh"
print(halvesAreAlike(s4))

# idea regex remove everything besides the wolves.
