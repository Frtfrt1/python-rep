# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    # if i == 5:
    #     break
else:
    print("End")  # break 발생X면 출력

nums = [1, 3, 5, 7, 9]
target = 2
i = 0
# found = 0

while i < len(nums):
    if nums[i] == target:
        print(f"{target} found, index: {i}")
        # found = 1
        break
    i += 1
else:
    print(f"{target} not found")

# if not found:
#     print(f"{target} not found")

# 1 ~ 10까지의 합
# sum = 55
i = 0
tot = 0

while i < 11:
    i += 1
    if i & 1:
        continue
    tot += i

print(f"sum = {tot}")
