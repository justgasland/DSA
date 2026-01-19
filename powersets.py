def allPossibleSets(n):
    s= len(n)
    results=[]

    for i in range(1 << s):
        subset=""
        for j in range(s):
            if (i & (1 << j)) > 0:
                subset+=n[j]
        results.append(subset)
    return results

if __name__ == "__main__":
    n = "abc"
    subsets = allPossibleSets(n)
 
    for subset in subsets:
        print(subset)