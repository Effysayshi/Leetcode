#A sequence (an) is increasing if an ≤ an+1 for all n ∈ N and decreasing if an ≥ an+1 for all n ∈ N.
# A sequence is monotone if it is either increasing or decreasing

class Sulotion:
    def monotonic_array(self,array):
        return (all(array[i] <= array[i+1] for i in range(len(array) - 1))) or (all(array[i] >= array[i+1] for i in range(len(array) - 1)))

A = [6, 5, 4, 4]
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

test = Sulotion()
print(test.monotonic_array(A))
print(test.monotonic_array(B))
print(test.monotonic_array(C))