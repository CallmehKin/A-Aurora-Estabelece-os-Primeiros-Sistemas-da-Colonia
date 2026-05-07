```python
# ==========================
# SISTEMA INTEGRADO - MARTE
# ==========================

energia = [20, 25, 30]
vento = [8, 10, 12]
consumo = 60

# --------------------------
# REGRA DE DECISÃO
# --------------------------

def decidir_acao(energia_atual, consumo_atual):

    if energia_atual < 30 and consumo_atual > 50:
        return "ALERTA: reduzir consumo"

    elif energia_atual > consumo_atual:
        return "SUGESTÃO: armazenar energia"

    else:
        return "Sistema estável"

# --------------------------
# PREVISÃO DE ENERGIA
# --------------------------

def prever_energia(vento_dados, energia_dados, novo_vento):

    relacoes = []

    for i in range(len(vento_dados)):
        relacoes.append(energia_dados[i] / vento_dados[i])

    media = sum(relacoes) / len(relacoes)

    return media * novo_vento

# --------------------------
# ANÁLISE ENERGÉTICA
# --------------------------

def analisar_energia(geracao, consumo):

    if consumo > geracao:
        return "RISCO: consumo maior que geração"

    else:
        return "OK: energia suficiente"

# --------------------------
# EXECUÇÃO
# --------------------------

energia_atual = energia[-1]

print("=== SISTEMA DA COLÔNIA ===")

print("\nDecisão:")
print(decidir_acao(energia_atual, consumo))

vento_novo = 11

energia_prevista = prever_energia(
    vento,
    energia,
    vento_novo
)

print("\nPrevisão de energia:")
print(f"Energia prevista = {round(energia_prevista, 2)}")

print("\nAnálise:")
print(analisar_energia(energia_atual, consumo))
```
