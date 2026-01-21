# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 01. 21. 10:11:01

def solution(n):
    return sum(i for i in range(2,n+1,2))