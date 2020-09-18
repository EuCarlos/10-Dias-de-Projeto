import matplotlib.pyplot as plt
import requests
from datetime import date

date_today = date.today()
date = '{}/{}/{}'.format(date_today.day, date_today.month,
date_today.year)

plt.rcParams["figure.figsize"] = (10,5)
print('Carregando Grafico...')
Url = 'https://corona-api.com/countries'
Paises = []
Casos_Confirmados = []
Tot_Mortes = []

Data = requests.get(Url).json()

try:
    Paises.append(Data["data"][213]["name"]) #Estados Unidos
    Casos_Confirmados.append(Data["data"][213]["latest_data"]["confirmed"])
    Tot_Mortes.append(Data["data"][213]["latest_data"]["deaths"])

    Paises.append(Data["data"][96]["name"]) #India
    Casos_Confirmados.append(Data["data"][96]["latest_data"]["confirmed"])
    Tot_Mortes.append(Data["data"][96]["latest_data"]["deaths"])

    Paises.append(Data["data"][38]["name"]) #Brasil
    Casos_Confirmados.append(Data["data"][38]["latest_data"]["confirmed"])
    Tot_Mortes.append(Data["data"][38]["latest_data"]["deaths"])

    Paises.append(Data["data"][159]["name"]) #Russia
    Casos_Confirmados.append(Data["data"][159]["latest_data"]["confirmed"])
    Tot_Mortes.append(Data["data"][159]["latest_data"]["deaths"])

    Paises.append(Data["data"][164]["name"]) #Peru
    Casos_Confirmados.append(Data["data"][164]["latest_data"]["confirmed"])
    Tot_Mortes.append(Data["data"][164]["latest_data"]["deaths"])
except IndexError:
    print('\033[33m'+'\033[41m'+"OCORREU UM ERRO: TENTANDO ALCANÇAR UM ÍNDICE QUE NÃO EXISTE NA API."+'\033[0;0m')

plt.title('Numero de casos COVID-19')
plt.xlabel('Paises')
plt.ylabel('N° de Casos')
plt.bar(Paises, Casos_Confirmados, color='#14213d', label='Confirmados')
plt.bar(Paises, Tot_Mortes, color='#fca311', label='Mortes')
plt.legend()

plt.grid(True)
plt.show()
for i in range(len(Paises)):
    print('País: {}\nCasos Confirmados: {}\nTotal de Mortes: {}\n'.format(Paises[i], Casos_Confirmados[i], Tot_Mortes[i]))
print('='*70)
print('Grafico criado em: {}(Hoje)\nAutor: Carlos Alves\nGitHub.com/EuCarlos'.format(date))
