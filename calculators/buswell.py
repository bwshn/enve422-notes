import re


def count_elements(formula):
    """Written in ChatGPT to count all the elements of a simply expresses molecule"""
    # Define a regular expression pattern to match elements and their counts
    pattern = r'([A-Z][a-z]*)(\d*)'

    # Initialize a dictionary to store the element counts
    element_counts = {}

    # Use re.findall() to find all matches of the pattern in the formula
    matches = re.findall(pattern, formula)

    # Iterate over the matches and update the element counts
    for match in matches:
        element = match[0]
        count = match[1] if match[1] else '1'
        if element in element_counts:
            element_counts[element] += int(count)
        else:
            element_counts[element] = int(count)

    # Return the element counts
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
    print(count_elements(formula))
    modified_Buswell(formula)
