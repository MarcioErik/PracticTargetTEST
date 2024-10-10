faturamento_estado = [
    {"SP": 67836.43},  
    {"RJ": 36678.66},
    {"MG": 29229.88},
    {"ES": 27165.48},
    {'Outros': 19849.53}
]

total_fat = sum(estado[list(estado.keys())[0]] for estado in faturamento_estado)

print(f'Faturamento total: {total_fat:.2f}')

percent_sp = next(estado["SP"] for estado in faturamento_estado if "SP" in estado) / sum(estado[list(estado.keys())[0]] for estado in faturamento_estado)
print(f'Porcentagem de SP:{percent_sp*100:.2f}%')

percent_rj = next(estado["RJ"] for estado in faturamento_estado if "RJ" in estado) / sum(estado[list(estado.keys())[0]] for estado in faturamento_estado)
print(f'Porcentagem de RJ:{percent_rj*100:.2f}%')

percent_mg = next(estado["MG"] for estado in faturamento_estado if "MG" in estado) / sum(estado[list(estado.keys())[0]] for estado in faturamento_estado)
print(f'Porcentagem de MG:{percent_mg*100:.2f}%')

percent_es = next(estado["ES"] for estado in faturamento_estado if "ES" in estado) / sum(estado[list(estado.keys())[0]] for estado in faturamento_estado)
print(f'Porcentagem de ES:{percent_es*100:.2f}%')

percent_others = next(estado["Outros"] for estado in faturamento_estado if "Outros" in estado) / sum(estado[list(estado.keys())[0]] for estado in faturamento_estado)
print(f'Porcentagem de Outros:{percent_others*100:.2f}%')