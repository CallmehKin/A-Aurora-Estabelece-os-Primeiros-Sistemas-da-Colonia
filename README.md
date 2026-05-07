# Sistema Integrado da Colônia – Aurora Siger

## Integrantes da Equipe

- Samirah Pinotti Deranian – 573375

---

# Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de representar o funcionamento inteligente de uma colônia em Marte.

O sistema organiza dados da colônia, toma decisões automáticas e realiza previsões simples utilizando conceitos de:
- estruturas de dados;
- lógica de programação;
- modelagem matemática;
- programação em Python.

A proposta simula um sistema computacional capaz de auxiliar no gerenciamento energético e operacional da base.

---

# Objetivos do Sistema

O sistema foi desenvolvido para:

- Organizar os dados da colônia;
- Criar regras automáticas de decisão;
- Realizar previsões energéticas simples;
- Analisar geração e consumo de energia;
- Simular comportamento inteligente da colônia.

---

# Organização dos Dados

Os dados foram organizados utilizando:
- listas;
- variáveis;
- estruturas hierárquicas.

## Exemplos:

```python
energia = [20, 25, 30]
vento = [8, 10, 12]
consumo = 60
```

---

# Regras de Decisão

O sistema utiliza lógica condicional para gerar ações automáticas.

## Regra 1

Se:
- energia < 30
- consumo > 50

Então:

```text
ALERTA: reduzir consumo
```

---

## Regra 2

Se:
- geração > consumo

Então:

```text
SUGESTÃO: armazenar energia excedente
```

---

# Modelagem e Previsão

O sistema utiliza regressão simples para prever geração energética com base na velocidade do vento.

## Exemplo:

| Vento | Energia |
|---|---|
| 8 | 20 |
| 10 | 25 |
| 12 | 30 |

### Entrada:

```text
vento = 11
```

### Saída:

```text
energia prevista ≈ 27
```

---

# Análise Energética

O sistema compara:
- geração;
- consumo;
- estabilidade energética.

## Exemplo de risco:

```text
geração = 40
consumo = 70
```

### Resultado:

```text
RISCO: consumo maior que geração
```

---

# Implementação em Python

O projeto foi implementado utilizando Python e funções simples.

## Principais funcionalidades:
- análise energética;
- previsão de energia;
- regras de decisão;
- geração de alertas.

---

# Estrutura do Sistema

```text
Sistema da Colônia
       ↓
Organização de Dados
       ↓
Regras de Decisão
       ↓
Previsão Energética
       ↓
Análise do Sistema
```

---

# Estrutura do Repositório

```text
📁 projeto-colonia
 ┣ 📄 README.md
 ┗ 📄 sistema.py
```

---

# Como Executar

1. Instale o Python
2. Abra o arquivo `sistema.py`
3. Execute o código

---

# Exemplo de Execução

```text
=== SISTEMA DA COLÔNIA ===

Decisão:
Sistema estável

Previsão de energia:
Energia prevista = 27.5

Análise:
RISCO: consumo maior que geração
```

---

# Tecnologias Utilizadas

- Python
- Estruturas de Dados
- Regressão Simples
- Lógica Condicional

---

# Conclusão

O projeto demonstrou como conceitos fundamentais da computação podem ser aplicados em um sistema integrado de gerenciamento energético.

A solução desenvolvida permite automatizar decisões, prever cenários e melhorar a estabilidade operacional da colônia.
