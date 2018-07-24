def submask(f):
    print("subnetting now...")
    return f

def calcsubmask(f):
    print("calculating now...")
    if f == 24:
        sm = "255.255.255.0"
    elif f == 25:
        sm = "255.255.255.128"
    elif f==26:
        sm = "255.255.255.192"
    elif f==27:
        sm = "255.255.255.224"
    return sm

#subnetmask = submask(int(input("here:" )))
calsubnetmask = calcsubmask((int(input("cidr: "))))

#print(f"this is {subnetmask}")

print(f"this is the actual sm: {calsubnetmask}")