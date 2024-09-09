import json

with open('faturamento.json') as f:
    data = json.load(f)

valores_faturamento = [item['valor'] for item in data['faturamento'] if item['valor'] > 0]

media_faturamento = sum(valores_faturamento) / len(valores_faturamento)
min_faturamento = min(valores_faturamento)
max_faturamento = max(valores_faturamento)
dias_acima_media = sum(1 for valor in valores_faturamento if valor > media_faturamento)

print("Menor valor de faturamento:", min_faturamento)
print("Maior valor de faturamento:", max_faturamento)
print("Número de dias acima da média:", dias_acima_media)