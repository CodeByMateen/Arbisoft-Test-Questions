def VehiclesUsed(T, S):
    i=-1
    Tcount=0
    
    while(Tcount<=len(S)):
        i=i+1
        if(T[i]<S[i]):
            n=S[i]-T[i]
            T[i+1] = T[i+1]-n
            Tcount+=S[i]
        elif T[i]>S[i]:
            n=T[i]-S[i]
            S[i+1]=S[i+1]+n
            Tcount+=S[i]
        else:
            Tcount+=S[i]
            
    return i
        

T=[4,4,2,4]
S=[5,5,2,5]

T.sort(reverse=True)
S.sort(reverse=True)

print(VehiclesUsed(T, S))