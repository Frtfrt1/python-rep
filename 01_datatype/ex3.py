# 불리언(bool)

a = True
print(a, type(a))

print(2 < 3)
print(2 > 3)
print(2 == 3)
print(2 != 3)

print("뽀로로" > "크롱")

# bool()
print(bool(3))  # T
print(bool(0))  # F
print(bool("hello"))  # T
print(bool(""))  # F
print(bool([10]))  # T
print(bool([]))  # F

# None 자료형
a = None
print(a, type(a))
print(bool(a))

if a is None:
    print("값이 없습니다")
