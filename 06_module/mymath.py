# 사용자 정의 모듈
print("start:", __name__)   # 모듈 이름을 가져오는 내장 변수 (직접 실행하면 __main__, 호출해서 실행하면 mymath)
PI = 3.14
TAU = 6.28
SPACECONSTANT = 15578884884

def add(a, b):
    return a + b
if __name__ == "__main__":  # 모듈 import시 출력되는 거 방지
    print(PI)
    print(add(10, 20))