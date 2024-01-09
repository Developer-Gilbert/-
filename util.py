# 함수명 : total
# 매개변수1 : start, 시작값
# 매개변수2 : end, 종료값
# start부터 end까지의 총합을 구해서 리턴

def total(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum


def calc(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2
