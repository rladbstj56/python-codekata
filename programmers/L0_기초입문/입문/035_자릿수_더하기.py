# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 15. 00:49:30

def solution(n):
    answer = 0
    n = str(n)
    nums = [i for i in n]
    for i in range(len(nums)):
        num = nums.pop()
        answer += int(num)
    return answer