marka = input("Kérem adjon meg egy autó márkát!: ")
evszam = int(input("Kérem adjon meg egy évszámot 1800-2021 között!: "))
def automarkak():
    if evszam < 1981:
        print("\tA(z)", marka, " veterán autó.")
    else:
        print("\tA(z)", marka, " nem veteran auto.")
#b
def veteranvizsgalat():
    eldontes = bool(marka) and marka[-1].isdigit()
    if eldontes:
        print("\tMuzealis")