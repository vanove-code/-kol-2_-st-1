import requests

# Zeptej se uživatele na IČO
ico = input("Zadej IČO subjektu: ")

# Sestavení URL s daným IČO
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

# Odeslání GET požadavku
response = requests.get(url)

# Zkontroluj, zda požadavek proběhl v pořádku
if response.status_code == 200:
    data = response.json()  # převedení odpovědi na JSON

    # Získání obchodního jména a adresy
    obchodni_jmeno = data.get("obchodniJmeno", "Neznámé jméno")
    adresa = data.get("sidlo", {}).get("textovaAdresa", "Adresa není k dispozici")

    # Výpis informací
    print(obchodni_jmeno)
    print(adresa)

else:
    print(f"Nepodařilo se získat data. HTTP kód: {response.status_code}")
