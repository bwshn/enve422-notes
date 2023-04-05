import math


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def solid():
    """Solid percent to mg/L conversion function, assuming water density is 1kg/L"""
    val = float(input("Enter solid (%) content: "))
    s_gravity = float(input("Enter specific gravity: "))
    mgL = val*s_gravity*10**6/100.0
    print("\n{0:.0f} mg/L\n{1:.2f}‰ || {2:.0f} ppm || {3:.0f} ppb\n".format(mgL,
          val * 10.0, val * 10000.0, val * 10000000.0))


def mg_L():
    """mg/L to solid % conversion function, assuming water density is 1kg/L"""
    mgL = float(input("Enter mg/L: "))
    s_gravity = float(input("Enter specific gravity: "))
    val = mgL*100.0/(s_gravity*10**6)
    print("\n{0:.2f}% || {1:.2f}‰ || {2:.0f} ppm || {3:.0f} ppb\n".format(
        val, val * 10.0, val * 10000.0, val * 10000000.0))


def log_to_percent():
    """Converts log removal to percent removal"""
    log_removal = float(input("Enter the log removal: "))
    percent_removal = (1 - 10 ** (-log_removal)) * 100
    numerator = percent_removal
    denominator = 100
    while numerator % 1 != 0 or denominator % 1 != 0:
        numerator *= 10
        denominator *= 10
    gcd_val = gcd(int(numerator), int(denominator))
    print("\n{0:.2f}%\nEach {1:.2f} reduced to 1\nInitial: {2:.2e} || Final: {3:.2e}\n".format(percent_removal, denominator /
          gcd_val/(denominator/gcd_val - numerator/gcd_val), denominator/gcd_val, denominator/gcd_val - numerator/gcd_val))


def percent_to_log():
    """Converts percent removal to log removal"""
    percent_removal = float(input("Enter the percent removal: "))
    log_removal = math.log10(100.0 / (100.0-percent_removal))
    numerator = percent_removal
    denominator = 100
    while numerator % 1 != 0 or denominator % 1 != 0:
        numerator *= 10
        denominator *= 10
    gcd_val = gcd(int(numerator), int(denominator))
    print("\n{0:.2f} log removal\nEach {1:.2f} reduced to 1\nInitial: {2:.2e} || Final: {3:.2e}\n".format(log_removal, denominator /
          gcd_val/(denominator/gcd_val - numerator/gcd_val), denominator/gcd_val, denominator/gcd_val - numerator/gcd_val))


def initial_and_final():
    """Converts initial and final values into log and percent removal"""
    initial = int(input("Enter the initial value: "))
    final = int(input("Enter the final value: "))
    removed = initial - final
    percent_removal = (removed / initial) * 100
    log_removal = math.log10(100.0 / (100.0-percent_removal))
    numerator = percent_removal
    denominator = 100
    while numerator % 1 != 0 or denominator % 1 != 0:
        numerator *= 10
        denominator *= 10
    gcd_val = gcd(int(numerator), int(denominator))
    print("\n{0:.2f} log removal\n{1:.2f}%\nEach {2:.2f} reduced to 1\n".format(log_removal, percent_removal, denominator /
          gcd_val/(denominator/gcd_val - numerator/gcd_val)))


ans = True
while (ans):
    print("1. Solid % to mg/L || 2. mg/L to Solid %")
    print("3. Log removal to % || 4. Removal % to log || 5. Initial and final to log and %")
    fun = input("What conversion do you want to use? (Enter an appropriate number)\n")
    if fun == "1":
        solid()
    elif fun == "2":
        mg_L()
    elif fun == "3":
        log_to_percent()
    elif fun == "4":
        percent_to_log()
    elif fun == "5":
        initial_and_final()
    else:
        ans = False
        print("Invalid input!")
        input("Press Enter to leave...")
