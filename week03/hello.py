def add(a, b):
    return a + b


print(add(1, 2))


def is_even(num):  # is_even 이라는 이름의 함수를 정의한다. num을 변수로 받는다.
    if num % 2 == 0:  # num을 2로 나눈 나머지가 0이면
        return True  # True (참)을 반환한다.
    else:  # 아니면,
        return False  # False (거짓)을 반환한다.


result = is_even(20)

# print 로 값 확인해보기
# result의 값은 무엇일까요?

fruits = ['사과', '배', '감', '귤']

for fruit in fruits:  # fruit 은 우리가 임의로 지어준 이름입니다.
    print(fruit)  # 사과, 배, 감, 귤 하나씩 꺼내어 출력합니다.
