import json

def calcular_faturamento(fat_diario):
    faturamentos = [dia['faturamento']for dia in fat_diario if dia['faturamento'] > 0 and dia['dia'] not in (6,0)]
    
    menor_fat = min(faturamentos)
    maior_fat = max(faturamentos)
    
    media_fat = int(sum(faturamentos) / len(faturamentos))
    
    acimaMedia = sum(1 for dia in faturamentos if dia > media_fat)
    return menor_fat, maior_fat, acimaMedia, media_fat

import os
with open('c:\\Users\\marci\\OneDrive\\Documentos\\teste_pratico_target\\Faturamento\\faturamento_diario.json', 'r') as file:
    faturamento_diario = json.load(file)

menor, maior, diasAcima, media_fat = calcular_faturamento(faturamento_diario)

print(f'Menor faturamento do mês: {menor}')
print(f'Maior faturamento do mês: {maior}')
print(f'Dias de faturamento acima da média ({media_fat}): {diasAcima}')
    
    
    
    