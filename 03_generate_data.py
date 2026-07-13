import pandas as pd
import random

# Nastavíme startovní pozici pro náhodnost, aby data byla pokaždé stejná
random.seed(42)

sektory = ['Bankovní', 'Nebankovní (licence)', 'Predátorský']
bydleni_moznosti = ['Vlastní', 'Nájem']
statusy = ['Splaceno', 'V prodlení', 'Exekuce']

data = []

for i in range(1, 501):
    # Logika hypotézy H1: Lidé v nájmu mají v našem modelu o něco větší šanci na horší úvěr
    typ_bydleni = random.choices(bydleni_moznosti, weights=[0.6, 0.4])[0]
    
    if typ_bydleni == 'Nájem':
        sektor = random.choices(sektory, weights=[0.4, 0.3, 0.3])[0]
    else:
        sektor = random.choices(sektory, weights=[0.7, 0.2, 0.1])[0]
        
    # Logika výše půjčky a RPSN podle sektoru
    if sektor == 'Bankovní':
        vyse = random.randint(50000, 300000)
        rpsn = round(random.uniform(4.5, 8.5), 1)
        status = random.choices(statusy, weights=[0.95, 0.04, 0.01])[0]
    elif sektor == 'Nebankovní (licence)':
        vyse = random.randint(20000, 100000)
        rpsn = round(random.uniform(10.0, 25.0), 1)
        status = random.choices(statusy, weights=[0.80, 0.15, 0.05])[0]
    else: # Predátorský
        vyse = random.randint(5000, 30000)
        rpsn = round(random.uniform(120.0, 300.0), 1)
        status = random.choices(statusy, weights=[0.30, 0.40, 0.30])[0]
        
    data.append([i, sektor, vyse, rpsn, typ_bydleni, status])

# Převedeme na tabulku a uložíme jako CSV se středníkem
df = pd.DataFrame(data, columns=['id_pujcky', 'sektor', 'vyse_pujcky_kc', 'rpsn_procento', 'typ_bydleni', 'status_splaceni'])
df.to_csv('pujcky_500.csv', index=False, sep=';', encoding='utf-8-sig')

print("Úspěch! Soubor 'pujcky_500.csv' byl vytvořen a obsahuje 500 unikátních řádků.")
