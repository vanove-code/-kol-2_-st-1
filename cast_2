import requests

# Zeptej se uživatele na část názvu subjektu
dotaz = input("Zadej název nebo část názvu subjektu: ")

# Nastavení hlaviček pro API
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

# Nastavení dat pro POST požadavek
data = {"obchodniJmeno": dotaz}

# Odeslání požadavku
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
response = requests.post(url, headers=headers, json=data)

# Zpracování odpovědi
if response.status_code == 200:
    vysledek = response.json()
    subjekty = vysledek.get("ekonomickeSubjekty", [])
    pocet = vysledek.get("pocetCelkem", 0)

    print(f"Nalezeno subjektů: {pocet}")

    for subjekt in subjekty:
        jmeno = subjekt.get("obchodniJmeno", "Neznámé jméno")
        ico = subjekt.get("ico", "Neznámé IČO")
        print(f"{jmeno}, {ico}")

else:
    print(f"Chyba při dotazu. HTTP kód: {response.status_code}")
