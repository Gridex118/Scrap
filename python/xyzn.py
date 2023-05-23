import sys

x: int = int(sys.argv[1])
y: int = int(sys.argv[2])
z: int = int(sys.argv[3])
n: int = int(sys.argv[4])

all_triplets: list[tuple] = [
    (i,j,k)
    for i in range(x+1) 
    for j in range(y+1)
    for k in range(z+1)
]

not_n_sums: list[tuple] = [ a for a in all_triplets if sum(a) != n ]

print("All triplets")
print(all_triplets)

print("triplets that do not sum to n")
print(not_n_sums)
