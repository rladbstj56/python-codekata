# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 13. 09:39:13

def solution(num_list):
    odd = [n for n in num_list if n%2]
    return [len(num_list)-len(odd),len(odd)]