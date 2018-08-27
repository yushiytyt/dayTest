f = open("test5.txt", "w", encoding="utf-8")
f.write("hello world1\nhello world2\nhello world3\nhello world4")
f.close()
f = open("test5.txt", "r", encoding="utf-8")
neiRong = f.read()
print(neiRong)

