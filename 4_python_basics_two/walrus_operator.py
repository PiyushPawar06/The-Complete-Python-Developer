# walrus operator is used to define a large expression so that the code becomes more clean and less complicated. denoted by :=
a = "abcdefghijk"
while (n := len(a)) > 2:
    print(n)
    a = a[:-1]
print(a)