def calculate_svi():
    """Calculates the SVI value based on 30 min compaction of sludge in 1L cylinder and MLSS content"""
    print("SVI Calculator\n")
    while True:
        try:
            volume = float(input("Volume (mL): "))
            mlss = float(input("MLSS (mg/L): "))

            # Check if inputs are valid
            if volume <= 0 or mlss <= 0:
                print("Volume and MLSS values must be greater than zero.\n")
                break

            svi = 1000 * volume / mlss
            print("SVI (mL/g):", svi, "\n")
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            break
        except KeyboardInterrupt:
            print("\nCalculation interrupted. Exiting...")
            break


calculate_svi()
