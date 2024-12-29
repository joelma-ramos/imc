print('Digite a sua altura: ')
altura = float(input())
print('Digite o seu peso: ')
peso = float(input())

resultado_imc = peso / (altura * altura)

if resultado_imc < 18.5:
    print('Você está com baixo peso')
elif resultado_imc >= 18.5 and resultado_imc < 25:
    print('Você está no peso adequado')
elif resultado_imc >= 25 and resultado_imc < 30:
    print('Você está em sobrepeso')
elif resultado_imc >= 30 and resultado_imc < 35:
    print('Você está em obesidade grau I')
elif resultado_imc >= 35 and resultado_imc < 40:
    print('Você está em obesidade grau II')
elif resultado_imc >= 40:
    print('Você está em obesidade grau III')

