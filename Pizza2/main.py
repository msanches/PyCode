# Importando matplotlib
import matplotlib.pyplot as plt

# Importando numpy
import numpy as np

# Aqui criamos a área que plotamos o gráfico e definimos seu tamanho
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

# Dados para compor o gráfico
recipe = ["Trigo",
          "Arroz",
          "Feijão",
          "Batata",
          "Aipim"]

# Definindo a quantidade de cada dado
data = [100, 250, 200, 120, 80]

# Aqui serão colocados os kg e as porcentagens no gráfico
def func(pct, allvals):
    # calc %
    absolute = int(pct/100.*np.sum(allvals))
    # fazendo legenda do gráfico com % e kg
    return "{:.1f}%\n({:d} kg)".format(pct, absolute)

# Criando o gráfico e colocando a função da legenda interna
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

# Definindo a caixa de legenda externa, título, localização e onde vai 'ancorar o box'
ax.legend(wedges, recipe,
          title="Produtos",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Aqui definimos o tamanho do texto de dentro do gráfico, e o peso da fonte como bold
plt.setp(autotexts, size=8, weight="bold")

# Título do gráfico
ax.set_title("Quantidade de itens do estoque em kg:")

# Mostrando o gráfico
plt.show()