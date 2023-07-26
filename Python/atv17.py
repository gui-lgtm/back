def calcular_tempo_download(tamanho_arquivo_mb, velocidade_link_mbps):
    tamanho_arquivo_bits = tamanho_arquivo_mb * 8 * 1024 * 1024
    velocidade_link_bps = velocidade_link_mbps * 1024 * 1024
    tempo_segundos = tamanho_arquivo_bits / velocidade_link_bps
    tempo_minutos = tempo_segundos / 60
    return tempo_minutos

def main():
    try:
        tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo em MB: "))
        velocidade_link_mbps = float(input("Digite a velocidade do link de internet em Mbps: "))

        if tamanho_arquivo_mb <= 0 or velocidade_link_mbps <= 0:
            print("Por favor, digite valores válidos maiores que zero.")
            return

        tempo_aproximado_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_link_mbps)

        print(f"O tempo aproximado de download será de {tempo_aproximado_minutos:.2f} minutos.")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar valores numéricos válidos.")

if __name__ == "__main__":
    main()