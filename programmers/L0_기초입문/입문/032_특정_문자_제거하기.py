# 특정 문자 제거하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120826
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 12. 09:57:15

def solution(my_string, letter):
    return ''.join([l for l in my_string if l != letter])