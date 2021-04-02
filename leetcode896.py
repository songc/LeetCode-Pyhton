class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag = None
        for i in range(1,len(A)):
            if flag is not None:
                if flag:
                    if A[i]<A[i-1]:
                        return False
                else:
                    if A[i]>A[i-1]:
                        return False
            else:
                if A[i]>A[i-1]:
                    flag = True
                if A[i]<A[i-1]:
                    flag = False
        return True