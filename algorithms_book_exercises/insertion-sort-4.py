# Exercise 2.1-4, page 22
# Consider the problem of adding two n-bit binary integers, 
# stored in two n-element arrays A and B. 
# The sum of the two integers should be stored in binary form 
# in an (n+1)-element array C. 
# State the problem formally and write pseudocode for adding the two integers.


def binary_sum (arrA, arrB):
    n = len(arrA)
    arrC = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        arrC[i + 1] += arrA[i] + arrB[i]
        if arrC[i + 1] > 1:
            arrC[i] += 1
            arrC[i + 1] -= 2
    return arrC

print("\nRemember, that arrays must have the same length.")
while True:
    arrA = list(map(int, input("\nEnter the array A (space-separated): ").split()))
    arrB = list(map(int, input("Enter the array B (space-separated): ").split()))
    if (len(arrA) == len(arrB)):
        break
    else:
        print("Arrays must have the same length!")
arrC = binary_sum(arrA, arrB)
print(f"\nRESULT: {arrC}\n")