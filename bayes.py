pa = float(input("Enter P(A): "))
pb = float(input("Enter P(B): "))
pba = float(input("Enter P(B|A): "))
pab = (pba * pa) / pb
print(f"P(A|B) = {pab}")
