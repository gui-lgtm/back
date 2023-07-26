import math

def calcular_latas_tinta(area):
    # Cada litro de tinta cobre 6 metros quadrados
    litros_tinta = area / 6
    # Uma lata de tinta possui 18 litros
    latas_tinta = math.ceil(litros_tinta / 18)
    return latas_tinta

def calcular_galoes_tinta(area):
    # Cada litro de tinta cobre 6 metros quadrados
    litros_tinta = area / 6
    # Um galão de tinta possui 3,6 litros
    galoes_tinta = math.ceil(litros_tinta / 3.6)
    return galoes_tinta

def calcular_latas_e_galoes_tinta(area):
    # Acrescente 10% de folga na quantidade de tinta necessária
    litros_tinta_com_folga = area / 6 * 1.1

    # Cálculo da quantidade de latas e galões
    latas_tinta = int(litros_tinta_com_folga / 18)
    litros_restantes = litros_tinta_com_folga % 18
    galoes_tinta = math.ceil(litros_restantes / 3.6)

    return latas_tinta, galoes_tinta

def calcular_preco_latas(latas):
    preco_lata = 80  # Preço de cada lata de tinta (R$ 80,00)
    return latas * preco_lata

def calcular_preco_galoes(galoes):
    preco_galao = 25  # Preço de cada galão de tinta (R$ 25,00)
    return galoes * preco_galao

def calcular_preco_latas_e_galoes(latas, galoes):
    preco_lata = 80  # Preço de cada lata de tinta (R$ 80,00)
    preco_galao = 25  # Preço de cada galão de tinta (R$ 25,00)
    preco_total = latas * preco_lata + galoes * preco_galao
    return preco_total

def main():
    try:
        area_pintar = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
        if area_pintar <= 0:
            print("Por favor, digite um valor válido para a área.")
            return

        latas_necessarias = calcular_latas_tinta(area_pintar)
        preco_latas = calcular_preco_latas(latas_necessarias)

        galoes_necessarios = calcular_galoes_tinta(area_pintar)
        preco_galoes = calcular_preco_galoes(galoes_necessarios)

        latas, galoes = calcular_latas_e_galoes_tinta(area_pintar)
        preco_latas_e_galoes = calcular_preco_latas_e_galoes(latas, galoes)

        print(f"Situação 1: Comprar apenas latas de 18 litros")
        print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
        print(f"Preço total: R$ {preco_latas:.2f}\n")

        print(f"Situação 2: Comprar apenas galões de 3,6 litros")
        print(f"Quantidade de galões de tinta necessários: {galoes_necessarios}")
        print(f"Preço total: R$ {preco_galoes:.2f}\n")

        print(f"Situação 3: Misturar latas e galões")
        print(f"Quantidade de latas de tinta necessárias: {latas}")
        print(f"Quantidade de galões de tinta necessários: {galoes}")
        print(f"Preço total: R$ {preco_latas_e_galoes:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido para a área.")

if __name__ == "__main__":
    main()