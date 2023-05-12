#!python3

print("This is a long piece of text that I don't want to have to type out every time.")

a = "This is a long piece of text that I don't want to have to type out every time."
print(a)

a = "This is a long piece of text that I don't want to have to type out every time."
b = a
print(b)

b = a = "This is a long piece of text that I don't want to have to type out every time."
c,d,e,f = "Or even like this",10, 20.0, True

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)