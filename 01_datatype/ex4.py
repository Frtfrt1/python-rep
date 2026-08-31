# 문자열(str)
# "", ''

a = "python"
print(a, type(a))

print("I'll be back")
print("I'll be back")

# 여러줄 문자열 (주석이랑 좀 다름)
a = """
Life is short
You need python
"""
print(a)


# docstring
def func():
    # x = 1 # 이거 쓰면 func.__doc__ 없어짐
    """
    func() 함수에 대한 설명 작성
    """
    pass


print(func.__doc__)  # func 첫번째 줄에 doc str 작성해야함

# 문자열 연결
print("Hello" + " Python")

# 문자열 반복
print("Hello" * 10)
print("-" * 50)

# 문자열 연산시 주의사항 (같은 자료형 끼리만 연산 가능)
print("Hello" + str(3))

print("10" + "2")
print(int("10") + int("2"))

# 문자열 포매팅 (f-string)
name = "pororo"
age = 23

print(f"이름{{}}: {name}, 나이: {age}")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}")

pi = 3.141592

print(f"{pi:.3f}")  # 3.142 (자동 반올림)
print(f"{pi:.0f}")

num = 1234567890
print(f"{num:,}")  # 1,234,567,890

print(f"{num:15d}")  # 15칸 확보 & 오른쪽 정렬
print(f"{num:<15,d}")  # 15칸 확보 & 쉼표 끊기 & 왼쪽 정렬

print(f"{num:015d}")  # 15칸 확보 & 오른쪽 정렬 & 빈 공간 0 채우기
print(f"{num:<015,d}")  # 15칸 확보 & 쉼표 끊기 & 왼쪽 정렬 & 빈 공간 0 채우기
