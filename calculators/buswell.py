def count_elements(formula):
    # Initialize a dictionary to store the element counts
    element_counts = {}
    
    # Loop through the characters in the formula
    i = 0
    while i < len(formula):
        # If the character is an uppercase letter, it starts a new element
        if formula[i].isupper():
            element = formula[i]
            count = 1
            
            # Check if there is a lowercase letter following the uppercase letter
            if i+1 < len(formula) and formula[i+1].islower():
                element += formula[i+1]
                i += 1
                
            # Check if there is a number following the element
            if i+1 < len(formula) and formula[i+1].isdigit():
                count = int(formula[i+1])
                i += 1
                
            # Add the element and count to the dictionary
            if element in element_counts:
                element_counts[element] += count
            else:
                element_counts[element] = count
        
        # Move on to the next character
        i += 1
    
    # Return the dictionary of element counts
    return element_counts


def modified_Buswell(formula):
    numbers = count_elements(formula)
    a = numbers.get('C', 0)
    b = numbers.get('H', 0)
    c = numbers.get('O', 0)
    d = numbers.get('N', 0)
    e = numbers.get('S', 0)
    Water = (4*a - b - 2*c + 3*d + 2*e)/4
    Methane = (4*a + b - 2*c - 3*d - 2*e)/8
    Carbondio = (4*a - b + 2*c + 3*d + 2*e)/8
    Ammonia = d
    HydrogenSulf = e
    print(
        f"H₂O: {Water} || CH₄: {Methane} || CO₂: {Carbondio} || NH₃: {Ammonia} || H₂S: {HydrogenSulf}")


while (1):
    formula = input("Enter the chemical formula: ")
    modified_Buswell(formula)
