import requests
import json

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

def stahni_ciselnik_pravnich_forem():
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat"
    data = {"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        ciselniky = response.json().get("ciselniky", [])
        if ciselniky:
            polozky = ciselniky[0].get("polozkyCiselniku", [])
            print(f"Načteno {len(polozky)} položek číselníku právních forem.")
            return polozky
    else:
        print("Nepodařilo se načíst číselník právních forem.")
        return []

def find_legal_form(kod, seznam_polozek):
    kod = str(kod).strip()
    for polozka in seznam_polozek:
        if str(polozka.get("kod")).strip() == kod:
            nazev_list = polozka.get("nazev", [])
            for nazev_dict in nazev_list:
                if nazev_dict.get("kodJazyka") == "cs":
                    return nazev_dict.get("nazev", "Neznámá právní forma")
            if nazev_list:
                return nazev_list[0].get("nazev", "Neznámá právní forma")
    return "Neznámá právní forma"

def main():
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
            kod_pravni_formy = str(pravni_forma_info).strip() if pravni_forma_info is not None else ""

            if kod_pravni_formy:
                nazev_pravni_formy = find_legal_form(kod_pravni_formy, pravni_formy)
            else:
                nazev_pravni_formy = "Právní forma není dostupná"

            print(f"{jmeno}, {ico}, {nazev_pravni_formy}")

    else:
        print(f"Chyba při vyhledávání. HTTP kód: {response.status_code}")

if __name__ == "__main__":
    main()
