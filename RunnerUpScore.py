if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res=[]
    [res.append(x) for x in arr if x not in res]#removing the duplicates 
    res.sort()#sorting in ascending so that -2 element will be runner up
    print(res[-2])#print the result
