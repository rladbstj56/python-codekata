# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 03. 16. 11:26:25

def solution(hp):
    answer = 0
    ants = [5, 3, 1]
    
    for ant in ants:
        count, hp = divmod(hp, ant)
        answer += count
        
    return answer