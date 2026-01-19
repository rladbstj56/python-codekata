# 두 수의 나눗셈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120806
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 01. 19. 12:09:00

def solution(num1, num2):
    import math
    answer = math.trunc(1000*num1/num2)
    return answer
