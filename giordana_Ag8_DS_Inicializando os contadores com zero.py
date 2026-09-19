# Inicializando os contadores com zero
qtd_excelente = 0
qtd_ruim = 0

# Definimos 10 para o teste (conforme solicitado). 
# Dica: Quando for rodar para 50, basta trocar o 10 por 50 aqui embaixo!
total_entrevistados = 10

print("=== SISTEMA DE PESQUISA DE SATISFAÇÃO - TUDOWEB ===")

# Estrutura de repetição para coletar os dados dos entrevistados
for i in range(total_entrevistados):
  print(f"\n--- Entrevistado {i + 1} de {total_entrevistados} ---")
  
  # Coletando nome e idade
  nome = input("Digite o nome do entrevistado: ")
  idade = int(input("Digite a idade do entrevistado: "))
  
  # Coletando a opinião
  print("Opções de avaliação:")
  print("1 - EXCELENTE")
  print("2 - BOM")
  print("3 - RUIM")
  
  opiniao = int(input("Digite o número da sua opinião (1, 2 ou 3): "))
  
  # Estrutura de decisão para contabilizar as respostas
  if opiniao == 1:
    qtd_excelente += 1  # Adiciona 1 ao contador de excelente
  elif opiniao == 3:
    qtd_ruim += 1      # Adiciona 1 ao contador de ruim
  else:
    print("Opção 'BOM' registrada (não altera os totais de excelente/ruim).")

# Exibindo os resultados finais solicitados pela empresa
print("\n========================================")
print("       RELATÓRIO FINAL - TUDOWEB        ")
print("========================================")
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print("========================================")