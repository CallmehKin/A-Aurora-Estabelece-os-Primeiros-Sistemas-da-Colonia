# ==========================
# SISTEMA DE POUSO - MARTE
# ==========================

modulos = []

# quantidade de módulos
quantidade = int(input("Quantos módulos deseja cadastrar? "))

# cadastro dos módulos
for i in range(quantidade):

    print(f"\nCadastro do módulo {i+1}")

    nome = input("Nome do módulo: ")
    combustivel = int(input("Combustível (%): "))
    prioridade = input("Prioridade (alta/media/baixa): ")

    modulo = {
        "nome": nome,
        "combustivel": combustivel,
        "prioridade": prioridade
    }

    modulos.append(modulo)

# listas auxiliares
pousados = []
alerta = []

# clima
clima = input("\nClima favorável? (sim/nao): ")

# verificação
for modulo in modulos:

    if modulo["combustivel"] > 25 and clima == "sim":

        print(f"\n{modulo['nome']} → POUSO AUTORIZADO")
        pousados.append(modulo)

    else:

        print(f"\n{modulo['nome']} → DECOLAGEM ABORTADA")
        alerta.append(modulo)

# resumo
print("\n========== RESUMO ==========")

print("\nMódulos pousados:")
for p in pousados:
    print("-", p["nome"])

print("\nMódulos em alerta:")
for a in alerta:
    print("-", a["nome"])
