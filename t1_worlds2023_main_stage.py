from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://lol.fandom.com/wiki/Special:RunQuery/PickBanHistory?PBH%5Bpage%5D=Worlds+2023+Main+Event&PBH%5Bteam%5D=T1&PBH%5Btextonly%5D%5Bis_checkbox%5D=true&PBH%5Btextonly%5D%5Bvalue%5D=&_run=&pfRunQueryFormName=PickBanHistory&wpRunQuery=&pf_free_text=")
soup = BeautifulSoup(html.read(), "html.parser")

#Encontrando a tabela
t1_pb_worlds2023_table = soup.find("table", {"class": "wikitable plainlinks hoverable-rows column-show-hide-1"})

#Encontrando todas as linhas da tabela, a partir da linha número 2 (tr = table row)
table_rows = t1_pb_worlds2023_table.tbody.findAll('tr')[2:]

blueban1 = []
blueban2 = []
blueban3 = []
bluepick1 = []
bluepick2 = []
bluepick3 = []
blueban4 = []
blueban5 = []
bluepick4 = []
bluepick5 = []
redban1 = []
redban2 = []
redban3 = []
redpick1 = []
redpick2 = []
redpick3 = []
redban4 = []
redban5 = []
redpick4 = []
redpick5 = []
bluepick1_role = []
bluepick2_role = []
bluepick3_role = []
bluepick4_role = []
bluepick5_role = []
redpick1_role = []
redpick2_role = []
redpick3_role = []
redpick4_role = []
redpick5_role = []

for rows in table_rows:
    table_columns = rows.findAll('td')[:33]

    blueban1.append(table_columns[6].get_text())
    blueban2.append(table_columns[8].get_text())
    blueban3.append(table_columns[10].get_text())
    bluepick1.append(table_columns[12].get_text())
    bluepick2.append(table_columns[14].get_text().split(", ")[0])
    bluepick3.append(table_columns[14].get_text().split(", ")[1])
    blueban4.append(table_columns[17].get_text())
    blueban5.append(table_columns[19].get_text())
    bluepick4.append(table_columns[21].get_text().split(", ")[0])
    bluepick5.append(table_columns[21].get_text().split(", ")[1])
    redban1.append(table_columns[7].get_text())
    redban2.append(table_columns[9].get_text())
    redban3.append(table_columns[11].get_text())
    redpick1.append(table_columns[13].get_text().split(", ")[0])
    redpick2.append(table_columns[13].get_text().split(", ")[1])
    redpick3.append(table_columns[15].get_text())
    redban4.append(table_columns[16].get_text())
    redban5.append(table_columns[18].get_text())
    redpick4.append(table_columns[20].get_text())
    redpick5.append(table_columns[22].get_text())
    bluepick1_role.append(table_columns[23].get_text())
    bluepick2_role.append(table_columns[24].get_text())
    bluepick3_role.append(table_columns[25].get_text())
    bluepick4_role.append(table_columns[26].get_text())
    bluepick5_role.append(table_columns[27].get_text())
    redpick1_role.append(table_columns[28].get_text())
    redpick2_role.append(table_columns[29].get_text())
    redpick3_role.append(table_columns[30].get_text())
    redpick4_role.append(table_columns[31].get_text())
    redpick5_role.append(table_columns[32].get_text())

data = {
    'BB1': blueban1,
    'BB2': blueban2,
    'BB3': blueban3,
    'RB1': redban1,
    'RB2': redban2,
    'RB3': redban3,
    'BP1': bluepick1,
    'RP1': redpick1,
    'RP2': redpick2,
    'BP2': bluepick2,
    'BP3': bluepick3,
    'RP3': redpick3,
    'BB4': blueban4,
    'BB5': blueban5,
    'RB4': redban4,
    'RB5': redban5,
    'RP4': redpick4,
    'BP4': bluepick4,
    'BP5': bluepick5,
    'RP5': redpick5,
    'BR1': bluepick1_role,
    'BR2': bluepick2_role,
    'BR3': bluepick3_role,
    'BR4': bluepick4_role,
    'BR5': bluepick5_role,
    'RR1': redpick1_role,
    'RR2': redpick2_role,
    'RR3': redpick3_role,
    'RR4': redpick4_role,
    'RR5': redpick5_role
}

df_t1_pb_worlds2023 = pd.DataFrame(data)
print(df_t1_pb_worlds2023)

df_t1_pb_worlds2023.to_excel('C:/Users\henri\OneDrive\Área de Trabalho\Excel\SKT T1 Drafts - Worlds 2023.xlsx')