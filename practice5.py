# num = int(input())
#
# i = 0
# while i < num:
#     print('',num)
#     i += 1

#정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, while 문을 사용하세요

# num = int(input())
#
# i=1
# while i <= num:
#     print(i,i*i)
#     i += 1

# 1이 될때까지
# 가능하면 최대한 많이 나누는 작업이 최적의 해를 보장?
### n,k를 공백을 기준으로 구분하여 입력 받기
n, k  = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될대 까지 빼기
    target = (n//k)*k
    result = result + (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n//= k

#마지막으로 남은 수에 대해 1씩 빼기
result += (n - 1)
print(result)