# PR 04
# Volume Of Sphere - 4/3PIr^3

r = 4.5
PI = 3.14
vol = 4/3*PI*r*r*r

# vol = 4/3*3.14*r*r*r -> Avoid using new variable, since all the variable will be object which will consume more memory
print(f"Volume of Sphere of radius {r} = {vol}")