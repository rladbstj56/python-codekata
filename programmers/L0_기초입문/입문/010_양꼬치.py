# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 01. 21. 10:00:05

def solution(n, k):
    service = n//10
    price = 12000*n + 2000*(k-service)
    return price