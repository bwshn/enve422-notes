import math


def specific_gravity_to_density():
    """
    Convert specific gravity to density.
    """
    specific_gravity = float(input("Enter the specific gravity: "))
    density_water = 1000  # Density of water in kg/m³ at 4°C
    density = specific_gravity * density_water
    print(f"\nDensity: {density} kg/m³\n")


def density_to_specific_gravity():
    """
    Convert density to specific gravity.
    """
    density = float(input("Enter the density (kg/m³): "))
    density_water = 1000  # Density of water in kg/m³ at 4°C
    specific_gravity = density / density_water
    print(f"\nSpecific gravity: {specific_gravity}\n")


def solid():
    """
    Solid percent to mg/L conversion function, assuming water density is 1kg/L.
    """
    val = float(input("Enter solid (%) content: "))
    s_gravity = float(input("Enter specific gravity: "))
    mgL = val * s_gravity * 10000
    print(f"\n{mgL:.0f} mg/L\n")


def mg_L():
    """Converts mg/L to solid %, assuming water density is 1 kg/L"""
    mgL = float(input("Enter mg/L: "))
    s_gravity = float(input("Enter specific gravity: "))
    val = mgL * 100.0 / (s_gravity * 10 ** 6)
    print(f"\n{val:.2f}%\n")


def log_to_percent():
    """
    Converts log removal to percent removal.
    """
    log_removal = float(input("Enter the log removal: "))
    percent_removal = (1 - 10 ** (-log_removal)) * 100
    print("\n{0:.{1}f}%\n".format(percent_removal, int(log_removal)))


def percent_to_log():
    """Converts percent removal to log removal"""
    percent_removal = float(input("Enter the percent removal: "))
    log_removal = math.log10(100.0 / (100.0-percent_removal))
    print("\n{:.2f} log removal\n".format(log_removal))


def initial_and_final():
    """Converts initial and final values into log and percent removal"""
    initial = int(float(input("Enter the initial value: ")))
    final = int(float(input("Enter the final value: ")))
    removed = initial - final
    percent_removal = (removed / initial) * 100
    log_removal = math.log10(100.0 / (100.0-percent_removal))
    print("\n{0:.2f} log removal\n{1:.{2}f}%\n".format(
        log_removal, percent_removal, int(log_removal)))


ans = True
while (ans):
    print("1. SG to kg/m³ || 2. kg/m³ to SG")
    print("3. Solid % to mg/L || 4. mg/L to Solid %")
    print("5. Log removal to % || 6. Removed % to log || 7. Initial and final values to removed log and %")
    fun = input(
        "Conversion function: ")
    if fun == "1":
        specific_gravity_to_density()
    elif fun == "2":
        density_to_specific_gravity()
    elif fun == "3":
        solid()
    elif fun == "4":
        mg_L()
    elif fun == "5":
        log_to_percent()
    elif fun == "6":
        percent_to_log()
    elif fun == "7":
        initial_and_final()
    else:
        ans = False
        print("Invalid input!")
        input("Press Enter to leave...")
