# Importando matplolib
import matplotlib.pyplot as plt

#Criando nosso conjunto de dados
labels = 'carros', 'motos', 'ônibus', 'caminhões'
sizes = [40, 30, 15, 20]

#Cira a representação e área de plotagem
figl, axl = plt.subplots()

#Criando o gráfico
axl.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

#Essa opção define o gráfico em circulo
axl.axis('equal')

#Finalmente mostramos o gráfico
plt.show()