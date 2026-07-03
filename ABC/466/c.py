import sys

def main():
    inp = sys.stdin
    N = int(inp.readline())

    def ask(i,j):
        print(f"? {i} {j}",flush = True)
        return inp.readline().strip() == "Yes"
    
    count = 0
    r = 1
    for i in range(1,N+1):
        if r < i:
            r = i
        while r < N and ask(i, r+1):
            r += 1
        count += r - i

    print(f"! {count}", flush = True)

main()