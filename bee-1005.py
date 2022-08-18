#media 1

A = float(input())
Af = float("{:.2f}".format(A))
B = float(input())
Bf = float("{:.2f}".format(B))


media = ((Af*3.5) + (Bf*7.5))/11

print(f"MEDIA = {media:.5f}")
