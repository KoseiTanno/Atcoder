# 私の回答
# 正解

A,B,X = map(int,input().split())

# 条件を満たすとわかっている端
# 0ならば必ず買える
ok = 0
# 条件を満たさないとわかっている端
# Nは10**9以下しか売っていない
ng = 10**9+1
while abs(ng-ok) > 1:
    mid = (ng+ok) // 2
    if (A*mid + B*len(str(mid))) <= X:
        ok = mid
    else:
        ng = mid
print(ok)