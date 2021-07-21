#
#실습1
# def decorator(func):
#     def decorated(input_text):
#         print('함수 시작!')
#         func(input_text)
#         print('함수 끝!')
#     return decorated
#
# @decorator
# def hello_world(input_text):
#     print(input_text)
#
#
# hello_world('Hello World!')

# 실습2
def decorator2(func):
    def inner_decorator(width, height):
        if width <= 0 or height <= 0:
            raise ValueError('Input value must be positive value')
        else:
            func(width, height)
    return inner_decorator

@decorator2
def tri(width, height):
    print(width * height * 1/2)

@decorator2
def squ(width, height):
    print(width * height)

tri(2, 4)

squ(4, 3)