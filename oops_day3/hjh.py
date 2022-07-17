
def lenghtOfLongestAP(set, n):
    if (n <= 2):
        return n

    L = [[0 for x in range(n)]
         for y in range(n)]
    llap = 2  # Initialize the result
    for i in range(n):
        L[i][n - 1] = 2

    for j in range(n - 2, 0, -1):
        i = j - 1
        k = j + 1
        while (i >= 0 and k <= n - 1):

            if (set[i] + set[k] < 2 * set[j]):
                k += 1

            elif (set[i] + set[k] > 2 * set[j]):
                L[i][j] = 2
                i -= 1

            else:

                L[i][j] = L[j][k] + 1

                # Update overall LLAP, if needed
                llap = max(llap, L[i][j])

                i -= 1
                k += 1
                while (i >= 0):
                    L[i][j] = 2
                    i -= 1
    return llap


# Driver Code
if __name__ == "__main__":
    t = int(input())
    # Below line read inputs from user using map() function
    set1 = list(map(int, input().strip().split()))[:t]

    n1 = len(set1)
    if(n1==0):
        print("-1")
    print(lenghtOfLongestAP(set1, t))



# This code is contributed by ita_c
