import re
from collections import defaultdict
from typing import Dict

# Define the formula pattern as a constant variable
FORMULA_PATTERN = r'([A-Z][a-z]*)(\d*)'

def count_elements(formula: str) -> Dict[str, int]:
    """
    Count the elements in a chemical formula.

    Args:
        formula (str): The chemical formula.

    Returns:
        dict: A dictionary with element counts.
    """
    # Initialize a defaultdict to store the element counts
    element_counts = defaultdict(int)

    # Use re.findall() to find all matches of the pattern in the formula
    matches = re.findall(FORMULA_PATTERN, formula)

    # Iterate over the matches and update the element counts
    for element, count in matches:
        count = count if count else '1'
        element_counts[element] += int(count)

    # Convert the defaultdict to a regular dictionary
    element_counts = dict(element_counts)

    # Return the element counts
    return element_counts

def calculate_compounds(elements: Dict[str, int]) -> Dict[str, float]:
    """
    Calculate the compounds based on the element counts.

    Args:
        elements (dict): A dictionary with element counts.

    Returns:
        dict: A dictionary with compound values.
    """
    carbon = elements.get('C', 0)
    hydrogen = elements.get('H', 0)
    oxygen = elements.get('O', 0)
    nitrogen = elements.get('N', 0)
    sulfur = elements.get('S', 0)

    # Calculate the compound values
    water = (4 * carbon - hydrogen - 2 * oxygen + 3 * nitrogen + 2 * sulfur) / 4
    methane = (4 * carbon + hydrogen - 2 * oxygen - 3 * nitrogen - 2 * sulfur) / 8
    carbon_dioxide = (4 * carbon - hydrogen + 2 * oxygen + 3 * nitrogen + 2 * sulfur) / 8
    ammonia = nitrogen
    hydrogen_sulfide = sulfur

    # Create a dictionary with the compound values
    compounds = {
        'H₂O': water,
        'CH₄': methane,
        'CO₂': carbon_dioxide,
        'NH₃': ammonia,
        'H₂S': hydrogen_sulfide
    }

    return compounds

def dulong_formula(elements: Dict[str, int]) -> float:
    """
    Calculate the Higher Calorific Value (HCV) using the Dulong formula.

    Args:
        elements (dict): A dictionary with element counts.

    Returns:
        float: The calculated Higher Calorific Value (HCV).
    """
    carbon = elements.get('C', 0)
    hydrogen = elements.get('H', 0)
    oxygen = elements.get('O', 0)
    nitrogen = elements.get('N', 0)
    sulfur = elements.get('S', 0)

    # Calculate the weight ratios
    total_weight = carbon * 12.011 + hydrogen * 1.00784 + oxygen * 15.999 + nitrogen * 14.0067 + sulfur * 32.065
    c_ratio = carbon * 12.011 / total_weight
    h_ratio = hydrogen * 1.00784 / total_weight
    o_ratio = oxygen * 15.999 / total_weight
    n_ratio = nitrogen * 14.0067 / total_weight
    s_ratio = sulfur * 32.065 / total_weight

    HCV = 33800 * c_ratio + 144000 * (h_ratio - o_ratio / 8) + 9270 * s_ratio

    return HCV

def process_formula(formula: str) -> None:
    """
    Process the chemical formula and print the elemental composition, compound values, and HCV.

    Args:
        formula (str): The chemical formula.
    """
    element_counts = count_elements(formula)

    if not element_counts:
        print("Invalid chemical formula.")
        return

    print("\nElemental Composition:")
    print(element_counts)

    compounds = calculate_compounds(element_counts)
    print("\nBuswell Equation:")
    for compound, value in compounds.items():
        print(f"{compound}: {value:.2f}")

    hcv = dulong_formula(element_counts)
    print("\nHigher Calorific Value (HCV or HHV):")
    print(f"{hcv:.2f} kJ/kg\n")

while True:
    formula = input("Enter the chemical formula (or press Enter to exit): ")
    if formula == "":
        break

    process_formula(formula)
