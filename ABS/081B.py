# 私の回答
# N = int(input())
# A = list(map(int,input().split()))
# even_count = 0
# divide_count = 0
# def judge_even_list(num_list):
#     count = 0
#     for num in num_list:
#         if num % 2 == 0:
#             count += 1
#     if count == len(num_list):
#         return True
#     else:
#         return False
    
# while(judge_even_list(A)):
#     if even_count == len(A):
#         divide_count += 1
#         A = [x/2 for x in A]
#     even_count = 0
#     for j in A:
#         if j % 2 == 0:
#             even_count += 1
# print(divide_count)

# 模範回答
# all関数は与えられたリスト内のすべての要素がTrueである場合にTrueを返す
# それを知っていればかなりコードが短くなった
n = int(input())
a = list(map(int, input().split()))

count = 0

while all(x % 2 == 0 for x in a):
  a = [x // 2 for x in a]
  count += 1
  
print(count)