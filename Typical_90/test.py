N = int(input())
s = "()"
def kakko(n):
    if n % 2 != 0:
        exit()
    elif n == 2:
        return ["()"]
    else:
        res = []
        for s in kakko(n-2):
            res += [s[:i] +"()" + s[i:] for i in range(N)]
            
        return sorted(list(set(res)))

print("\n".join(kakko(N)))