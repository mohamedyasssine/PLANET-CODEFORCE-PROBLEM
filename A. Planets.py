t=int(input())
for i in range(t) :
    n,c=map(int,input().split())
    dict1=dict()
    L=list(map(int,input().split()))
    for j in L :
        if j not in dict1 :
            dict1[j]=1
        else :
            dict1[j]+=1
    resultat=0
    for j in dict1.keys() :
        if(dict1[j]==1):
            resultat+=1
        else:
            if(dict1[j]>c):
                resultat += c
            else:
                resultat+=dict1[j]
    print(resultat)