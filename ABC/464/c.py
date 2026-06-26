import sys

def main():
    lines = sys.stdin.read().split("\n")
    N,M = map(int,lines[0].split())

    cnt = [0] * (N+1)
    events = [[] for _ in range(M+1)]
    for i in range(1,N+1):
        a,d,b = map(int,lines[i].split())
        cnt[a] += 1
        events[d].append([a,b])
    
    distinct = sum(1 for i in cnt if i > 0)
    ans = []
    for i in range(1,M+1):
        for a,b in events[i]:
            cnt[a] -= 1
            if cnt[a] == 0: distinct -= 1
            if cnt[b] == 0: distinct += 1
            cnt[b] += 1
        ans.append(distinct)
    print("\n".join(map(str,ans)))      
main()
