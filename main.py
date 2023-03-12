# python3

def parallel_processing(n, m, data):
    output = []
    
    for i in range(n):
        output.append((i, 0))

    procNum = n

    while procNum <= m:
        for i in range(n):
            sec = output[]


    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    text = input().split()
    n = text[0]
    m = text[1]

    data = []
    data = input().split()

    result = parallel_processing(n,m,data)
    
    for i,j in result:
        print(i,j)
    
if __name__ == "__main__":
    main()
