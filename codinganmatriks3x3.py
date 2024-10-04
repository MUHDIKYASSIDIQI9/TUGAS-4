a = [[4, 3, 1],
     [2, 1, 5],
     [1, 2, 2]]

b = [[1, 2, 4],
     [2, 3, 1],
     [4, 1, 2]]

c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
baris_a = len(a)
kolom_a = len(a[0])

baris_b = len(b)
kolom_b = len(b[0])

print(a)
print("Baris matriks a adalah: ", baris_a)
print("Kolom matriks a adalah: ", kolom_a)
print()
print(b)
print("Baris matriks b adalah: ", baris_b)
print("Kolom matriks b adalah: ", kolom_b) 

if (kolom_a == baris_b):
    print("matriks a dan b dapat di kalikan")
else:
    print("matriks a dan b tidak dapat di kalikan")

print("Hasil perkalian matriks a dengan b:")
c = (a[0][0]*b[0][0])+(a[0][1]*b[1][0])+(a[0][2]*b[2][0])
d = (a[0][0]*b[0][1])+(a[0][1]*b[1][1])+(a[0][2]*b[2][1])
e = (a[0][0]*b[0][2])+(a[0][1]*b[1][2])+(a[0][2]*b[2][2])
print(f"[{c},{d},{e}]")
f = (a[1][0]*b[0][0])+(a[1][1]*b[1][0])+(a[1][2]*b[2][0])
g = (a[1][0]*b[0][1])+(a[1][1]*b[1][1])+(a[1][2]*b[2][1])
h = (a[1][0]*b[0][2])+(a[1][1]*b[1][2])+(a[1][2]*b[2][2])
print(f"[{f},{g},{h}]")
i = (a[2][0]*b[0][0])+(a[2][1]*b[1][0])+(a[2][2]*b[2][0])
j = (a[2][0]*b[0][1])+(a[2][1]*b[1][1])+(a[2][2]*b[2][1])
k = (a[2][0]*b[0][2])+(a[2][1]*b[1][2])+(a[2][2]*b[2][2])
print(f"[{i},{j},{k}]")


PS C:\Users\MyBook Hype> python.exe '.\TUGAS 4 MENGHITUNG MATRIKS 3X3.py'
[[4, 3, 1], [2, 1, 5], [1, 2, 2]]
Baris matriks a adalah:  3
Kolom matriks a adalah:  3

[[1, 2, 4], [2, 3, 1], [4, 1, 2]]
Baris matriks b adalah:  3
Kolom matriks b adalah:  3
matriks a dan b dapat di kalikan
Hasil perkalian matriks a dengan b:
[14,18,21]
[24,12,19]
[13,10,10]

