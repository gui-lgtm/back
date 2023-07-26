import math

def calcular_latas_tinta(area):
    litros_tinta = area / 3

    latas_tinta = math.ceil(litros_tinta / 18)
    return latas_tinta

def calcular_preco_total(latas):
    preco_lata = 80
    return latas * preco_lata

def main():
    try:
        area_pintar = float(input("Digite o tamanho de metros quadrados da area a ser pintada: "))
        if area_pintar <= 0:
            print("Por Favor, digite o valor para a area.")
            return


        latas_necessarias = calcular_latas_tinta(area_pintar)
        preco_total = calcular_preco_total(latas_necessarias)

        print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
        print(f"Preço total: R$ {preco_total:.2f}")
        
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido para a área.")

if __name__ == "__main__":
    main()