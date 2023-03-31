def solid():
    """Solid percent to mg/L conversion function, assuming water density is 1kg/L"""
    val = float(input("Enter solid (%) content: "))
    s_gravity = float(input("Enter specific gravity: "))
    mgL = val*s_gravity*10**6/100.0
    print("\n{0:.0f} mg/L\n".format(mgL))


def mg_L():
    """mg/L to solid % conversion function, assuming water density is 1kg/L"""
    mgL = float(input("Enter mg/L: "))
    s_gravity = float(input("Enter specific gravity: "))
    val = mgL*100.0/(s_gravity*10**6)
    print("\n{0:.0f} %\n".format(val))


while (1):
    print("1. Solid % to mg/L || 2. mg/L to Solid %")
    fun = int(input("What conversion do you want to use? (Enter 1 or 2)\n"))
    if fun == 1:
        solid()
    elif fun == 2:
        mg_L()
    else:
        print("Invalid input!")
