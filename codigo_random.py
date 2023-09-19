def voce_E(nome):
    print(f"você {nome} é uma das pessoas ja feitas aqui no tal planeta terra")

print("bem vindo ao teste de git do isaque")
escolha = int(input("digite 1 para olee e 2 para olá: "))
if escolha == 1:
    escolha = "olee"
elif escolha == 2:
    escolha = "ola"
else:
    print("mensagem invalida")
    print('tá errado')
    print("teste_01")
nome = input("agora fala seu nome ai: ")
print(voce_E(nome))
print(f'vc escolheu a opção {escolha + " oi"}')
