if __name__ == '__main__':
    records=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score,name])
        scores.append(score)
sec_score=sorted(set(scores))[1]
lst=[]
for i in range(len(records)):
    if(sec_score==records[i][0]):
        lst.append(records[i][1])
lst.sort()
for i in range(len(lst)):
    print(lst[i])
