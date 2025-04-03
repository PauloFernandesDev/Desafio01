hora1 = int (input("Informe a primeira hora: "))
min1 = int(input("Informe o(s) primeiro(s) minuto(s): "))
hora2 = int (input("Informe a segunda hora : "))
min2 = int(input("Informe o(s) segundo(s) minuto(s): "))
resultado = 0
min = 0
if hora1 > 12:
    hora1 = hora1 - 12
if hora2 > 12:
    hora2 = hora2 -12

resultado = hora1 + hora2
min = min1 + min2
if min >= 60:
    resultado = resultado + 1
    min = min - 60

if resultado > 12:
    resultado = resultado - 12

print(f"Hora saida: {resultado}:{min}")