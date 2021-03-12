"""Split sorted modely_02."""

import pandas as pd

url = "https://onemocneni-aktualne.mzcr.cz/api/account/mifLSHU2re3GAmiotOkdYExeoQ/file/modely%252Fmodely_02_efektivita_testovani.csv"

df = pd.read_csv(url, delimiter=';')

df = df.sort_values(['datum_hlaseni', 'datum_prvniho_priznaku', 'orp', 'vek_kat', 'pohlavi'])

df[df['datum_hlaseni'] < '2021'].to_csv('modely_02_efektivita_testovani_sorted_2020_v1.csv')

df.loc[(df['datum_hlaseni'] >= '2021') & (df['datum_hlaseni'] < '2021-07')].to_csv('modely_02_efektivita_testovani_sorted_2021_1_v1.csv')

df.loc[(df['datum_hlaseni'] >= '2021') & (df['datum_hlaseni'] >= '2021-07')].to_csv('modely_02_efektivita_testovani_sorted_2021_2_v1.csv')

df.loc[(df['datum_hlaseni'] >= '2022')].to_csv('modely_02_efektivita_testovani_sorted_2022_v1.csv')

df[(df['datum_hlaseni'] >= '2023') | df['datum_hlaseni'].isnull()].to_csv('modely_02_efektivita_testovani_sorted_null_v1.csv')