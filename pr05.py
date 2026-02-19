# PR 05
# Find value of expr: 4a^3+3b^2

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
# value = 4*(a*a*a)+3*(b*b)
# value = 4*(a*a*a)+3*(b*b) -> This can be rewritten as value = 4*(a**3)+3*(b*b)
value = 4*(a**3)+3*(b*b)
print(f"Find value of expr: 4a^3+3b^2, where a={a}, b={b}, value={value}")
