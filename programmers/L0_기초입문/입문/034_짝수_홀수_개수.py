# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 13. 09:34:03

def solution(num_list):
    even = [i for i in num_list if i%2==0]
    odd = [i for i in num_list if i%2!=0]
    return (len(even),len(odd))