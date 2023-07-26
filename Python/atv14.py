hora = float(input("Digite quanto você ganha por hora: "))

trabalho = float(input("Digite as horas trabalhadas no mês: "))

resultado = hora * trabalho   

print("Salario Bruto", resultado)

result2 = resultado *11
result3 = result2 / 100

print("Você pagou", result3, "de ir")

result4 = resultado * 8
result5 = result4 / 100

print("Você pagou:", result5, "de INSS")

result6 = resultado * 5 
result7 = resultado / 100

print("Você pagou:", result7, "de Sindicato")

salario = resultado - result3 - result5 - result7
print("Salario liquido é: ", salario)