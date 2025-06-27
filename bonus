import requests

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

def stahni_ciselnik_pravnich_forem():
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat"
    data = {"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        ciselnik = response.json()
        polozky = ciselnik["ciselniky"][0]["polozkyCiselniku"]
        return polozky
    else:
        print("Nepodařilo se načíst číselník právních forem.")
        return []

def find_legal_form(kod, seznam_polozek):
    kod = str(kod) if kod is not None else ""
    for polozka in seznam_polozek:
        if str(polozka.get("kod")) == kod:
            return polozka.get("nazev")
    return "Neznámá právní forma"

dotaz = input("Zadej název nebo část názvu subjektu: ")

pravni_formy = stahni_ciselnik_pravnich_forem()

url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
data = {"obchodniJmeno": dotaz}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    vysledek = response.json()
    subjekty = vysledek.get("ekonomickeSubjekty", [])
    pocet = vysledek.get("pocetCelkem", 0)

    print(f"\nNalezeno subjektů: {pocet}\n")

    for subjekt in subjekty:
        jmeno = subjekt.get("obchodniJmeno", "Neznámé jméno")
        ico = subjekt.get("ico", "Neznámé IČO")

        pravni_forma_info = subjekt.get("pravniForma")
        if isinstance(pravni_forma_info, dict):
            kod_pravni_formy = pravni_forma_info.get("kod")
        else:
            kod_pravni_formy = None

        nazev_pravni_formy = find_legal_form(kod_pravni_formy, pravni_formy)
        print(f"{jmeno}, {ico}, {nazev_pravni_formy}")

else:
    print(f"Chyba při vyhledávání. HTTP kód: {response.status_code}")
