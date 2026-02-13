# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 13. 09:17:10

import re
def solution(my_string):
    answer = re.sub('a|e|i|o|u','',my_string)
    return answer