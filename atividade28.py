# Um sistema de monitoramento deve ler a temperatura de um servidor e classificar assim:
#  até C → “Normal”; entre 61°C e 80°C → “Atenção”; acima de 80°C → “Crítico — risco de superaquecimento!”.


temperatura = float(input("Digite a temperatura do servidor (°C): "))
if temperatura <= 60:
    print("Normal.")
elif 61 <= temperatura <= 80:
    print("Atenção!")
else:
    print("Crítico - risco de superaquecimento!")