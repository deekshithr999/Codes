class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        i, j = 0, 0
        sumA, sumB = 0, 0
        while i<m or j<n:
            if i< m and (j == n or A[i]< B[j]):
                sumA += A[i]
                i+=1
            elif j < n and (i==m or A[i]>B[j]):
                sumB += B[j]
                j+=1
            else:
                sumA = sumB = max(sumA, sumB) + A[i]
                i+=1
                j+=1
        return max(sumA, sumB)% (pow(10,9)+7)


def maxSum(self, A, B):
    '''
    Ref from lc solutions
    '''
    i, j, n, m = 0, 0, len(A), len(B)
    a, b, mod = 0, 0, 10**9 + 7
    while i < n or j < m:
        if i < n and (j == m or A[i] < B[j]):
            a += A[i]
            i += 1
        elif j < m and (i == n or A[i] > B[j]):
            b += B[j]
            j += 1
        else:
            a = b = max(a, b) + A[i]
            i += 1
            j += 1
    return max(a, b) % mod