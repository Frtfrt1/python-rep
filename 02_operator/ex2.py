# 비트 연산자
a = 5  # 0000 0101
b = 3  # 0000 0011
print(a & b)  # 0000 0001, 1
print(a | b)  # 0000 0111, 7
print(a ^ b)  # 0000 0110, 6
print(a << b)  # 0010 1000, 40 = 5*2^3 (5 -> 10 -> 20 -> 40)
print(40 >> b)  # 5
print(~a)  # 1111 1010 -> 0000 0110, -6

# 멤버쉽 연산자
print("a" in "apple")
print(3 in [1, 2, 3])

# 삼항 연산자
# int max = a > b ? a : b;

a, b = 2, 3
max = a if a > b else b

print("홀수" if a & 1 else "짝수")

score = 85
# 90점 이상이면 "A"
# 80점 이상이면 "B"
# 70점 이상이면 "C"
# 70점 미만이면 "D"
print("ABCD"[0 if score >= 90 else (1 if score >= 80 else (2 if score >= 70 else 3))])
