nome = str(input('Digite seu nome: ')).strip().capitalize()
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura[m]: '))
peso = float(input('Digite seu peso[kg]: '))
imc = peso / altura ** 2
print(f'\nBem-vindo(a), {nome}!')
print(f'Você tem {altura}m de altura, pesa {peso}kg e tem {idade} anos.')
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Você está abaixo do peso!\n')
elif 18.5 < imc < 24.9:
    print(f'Seu IMC é {imc:.2f}. Você está com o peso ideal!\n')
elif 25 <= imc < 29.9:
    print(f'Seu IMC é {imc:.2f}. Você está com sobrepeso!\n')
elif 30 <= imc < 34.9:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade grau I!\n')
elif 35 <= imc < 39.9:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade grau II!\n')
else:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade grau III\n')