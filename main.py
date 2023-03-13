# python3

def parallel_processing(n, m, data):
    output = []
    
    for i in range(n):
        output.append((i, 0))

    procNum = n

    while procNum <= m:
        for i in range(n):
            sec = output[procNum-n][1] + int(data[procNum-n])
            output.append(i, sec)
            procNum = procNum + 1

    return output

def main():
    text = input().split()
    n = text[0]
    m = text[1]

    data = []
    data = input().split()

    result = parallel_processing(int(n),int(m),data)
    
    for i,j in result:
        print(i,j)
    
if __name__ == "__main__":
    main()
