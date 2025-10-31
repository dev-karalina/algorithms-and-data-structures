# Exercise 2.1-3, page 22
# Consider the searching problem:
# Input: A sequence of n numbers A = [a1, a2, ..., an] and a value v.
# Output: An index i such that v = A[i] or 
# the special value NIL if v does not appear in A.
# Write code for linear search, which scans through the sequence, 
# looking for v. Using a loop invariant, prove that your algorithm is correct. 
# Make sure that your loop invariant fulfills the three necessary properties


def linear_search (arr, v):
    n = len(arr)
    for i in range(n):
        if (arr[i] == v): 
            return i
    return None


arr = list(map(int, input("\nEnter the array (space-separated): ").split()))
v = int(input("Enter the value to search for: "))
index = linear_search(arr, v)
if index is None:
    print("\nRESULT: NIL\n")
else:
    print(f"\nRESULT: {index}\n")