# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 05. 00:21:39

def solution(array, height):
    array.append(height)
    array.sort(reverse=True) # inplace 메서드
    a = array.index(height)
    return a