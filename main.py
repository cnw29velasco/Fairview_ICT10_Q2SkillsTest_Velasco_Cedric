from pyscript import document, display
#Dictionary containing planets information

nonmetals= {
    "H": ("H", "Hydrogen", 1, 1.008),
    "C": ("C", "Carbon", 6, 12.011),
    "N": ("N", "Nitrogen", 7, 14.007),
    "O": ("O", "Oxygen", 8, 15.999),
    "F": ("F", "Fluorine", 9, 18.998),
    "P": ("P", "Phosphorus", 15, 30.974),
    "S": ("S", "Sulfur", 16, 32.06),
    "Se": ("Se", "Selenium", 34, 78.971),
    "Cl": ("Cl", "Chlorine", 17, 35.45),
    "Br": ("Br", "Bromine", 35, 79.904),
    "I": ("I", "Iodine", 53, 126.904),
    "He": ("He", "Helium", 2, 4.003),
    "Ne": ("Ne", "Neon", 10, 20.180),
    "Ar": ("Ar", "Argon", 18, 39.948),
    "Kr": ("Kr", "Krypton", 36, 83.798),
    "Xe": ("Xe", "Xenon", 54, 131.293),
    "Rn": ("Rn", "Radon", 86, 222)
}
# Values, Non metal code, Non metal symbol, Name, Atomic Number, Atomic Mass

#function to search for a planet
def find_nonmetal(e):

    #Get the input FROM HTML
    nonmetal = document.getElementById("nonmetal").value

    lookup = nonmetals.get(nonmetal, ("Nonmetal cannot be found", "-", "-", "-"))

    #display the propertiest
    
    document.getElementById("nonmetalcode").innerText = nonmetal
    document.getElementById("symbol").innerText = lookup[0]
    document.getElementById("element").innerText = lookup[1]
    document.getElementById("atomic number").innerText = lookup[2]
    document.getElementById("atomic mass").innerText = lookup[3]


