produtos = []

quantidade = int(input("Quantos produtos deseja cadastrar? "))

# Cadastro
for i in range(quantidade):
    print(f"\nProduto {i + 1}")

    nome = input("Nome: ")
    preco = float(input("Preço: R$ "))
    categoria = input("Categoria: ")

    produtos.append([nome, preco, categoria])


# Filtragem
valor_filtro = float(input("\nDigite um valor para filtrar: "))

print(f"\nProdutos acima de R$ {valor_filtro:.2f}:")

for produto in produtos:
    if produto[1] > valor_filtro:
        print(f"{produto[0]} - R$ {produto[1]:.2f} - {produto[2]}")


# Ordenação crescente
produtos_crescente = produtos.copy()

produtos_crescente.sort(key=lambda produto: produto[1])

print("\nProdutos em ordem crescente:")

for produto in produtos_crescente:
    print(f"{produto[0]} - R$ {produto[1]:.2f} - {produto[2]}")


# Ordenação decrescente
produtos_decrescente = sorted(
    produtos,
    key=lambda produto: produto[1],
    reverse=True
)

print("\nProdutos em ordem decrescente:")

for produto in produtos_decrescente:
    print(f"{produto[0]} - R$ {produto[1]:.2f} - {produto[2]}")


# Categorias únicas
categorias = set()

for produto in produtos:
    categorias.add(produto[2])

print("\nCategorias únicas:")

for categoria in categorias:
    print(f"- {categoria}")


# Estatísticas
precos = []

for produto in produtos:
    precos.append(produto[1])

menor_preco = min(precos)
maior_preco = max(precos)
media_precos = sum(precos) / len(precos)

estatisticas = (menor_preco, maior_preco, media_precos)


# Relatório final
print("\n================================")
print("       RELATÓRIO FINAL")
print("================================")

print(f"Quantidade de produtos: {len(produtos)}")
print(f"Menor preço: R$ {estatisticas[0]:.2f}")
print(f"Maior preço: R$ {estatisticas[1]:.2f}")
print(f"Média dos preços: R$ {estatisticas[2]:.2f}")

print("\nCategorias:")

for categoria in categorias:
    print(f"- {categoria}")


# ==========================================
# VERSÃO EM PORTUGAL - LÓGICA
# ==========================================

# Cadastro:
# vetor_produtos = vetor de tamanho fixo
#
# para cada posição:
#     ler nome
#     ler preço
#     ler categoria
#     armazenar os dados


# Filtragem:
# para cada produto no vetor:
#     se preço > valor_filtro:
#         mostrar produto


# Bubble Sort crescente:
# para i:
#     para j:
#         se preço[j] > preço[j + 1]:
#             trocar os produtos


# Bubble Sort decrescente:
# para i:
#     para j:
#         se preço[j] < preço[j + 1]:
#             trocar os produtos


# Conjunto manual:
# categorias_unicas = vetor vazio
#
# para cada categoria:
#     verificar se já existe
#     se não existir:
#         adicionar ao vetor


# Estatísticas:
# menor = menor preço
# maior = maior preço
# soma = soma dos preços
# média = soma / quantidade
#
# estatisticas = (menor, maior, média)