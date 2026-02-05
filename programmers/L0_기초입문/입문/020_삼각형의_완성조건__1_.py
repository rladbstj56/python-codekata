# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 05. 09:30:59

def solution(sides):
    if max(sides) < sum(sides)-max(sides):
        return 1
    else:
        return 2