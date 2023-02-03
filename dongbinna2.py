# 곱하기 혹은 더하기 문제
# 첫째줄에 하나의 문자열 S주어짐 -> 첫쨰줄에 만들어질 수 있는 가장 큰 수 출력
# +보다 *가 큰 수가 됨 ! 그러나 0이나 1인 경우 -> 더하기가 더 효율적
# data = input()
#
# # 첫번째 문자를 숫자로 대입하여 변경
# result = int(data[0])
#
# for i in range(1, len(data)):
#     # 두 수 중에서 하ㄹ나라도 0이나 1인 경우 , 곱하기 보다는 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print((result))

# --------------------------------------------------------------------------------------
# 모험가 길드 문제
# 오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인한다

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# result = 0 # 총 그룹 수
# count = 0 # 현재 그룹에 포함됭 모험가의 수
#
# for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
#     count += 1 # 현재 그룹에 모험가 포함
#     if count >= i:
#         result += 1
#         count = 0
#
# print(result)











