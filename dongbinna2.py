# 곱하기 혹은 더하기 문제
# 첫째줄에 하나의 문자열 S주어짐 -> 첫쨰줄에 만들어질 수 있는 가장 큰 수 출력
# +보다 *가 큰 수가 됨 ! 그러나 0이나 1인 경우 -> 더하기가 더 효율적
data = input()

# 첫번째 문자를 숫자로 대입하여 변경
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하ㄹ나라도 0이나 1인 경우 , 곱하기 보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print((result))