# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 12. 09:51:58


def solution(n):
    r = n**(0.5)
    return 1 if r % 1 == 0 else 2