# 여러 함수들의 시작, 종료에 공통적으로 사용되는 코드가 있는 경우 decorator 를 만들어서 사용하면 매우 유용
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('===== before =====')
        func(*args, **kwargs)         # introduce 실행
        print('===== after  =====')
    return wrapper


@decorator
def introduce(name):
    print(f'My name is {name}!')


introduce('sparta')