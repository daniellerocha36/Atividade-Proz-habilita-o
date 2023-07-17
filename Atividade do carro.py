#Desenvolva um código que utilize as seguintes características de um veículo:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.

#Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

#algoritmos:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.

#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
#E: Veículos com quatro rodas ou mais e com mais de 6000 kg.




#Var
quantidade_de_rodas = int (input("Digite a quantidade de rodas do seu veículo: "))
peso_do_veiculo = int (input("Digite o peso do seu veículo: "))
quantidade_de_pessoas_acomodam = int (input("Digite a quantidade de pessoas que seu veículo acomoda: "))

#Inicio

if quantidade_de_rodas == 2 or quantidade_de_rodas ==3:
    print("Seu veículo é da categoria:A")

elif quantidade_de_rodas == 4 and quantidade_de_pessoas_acomodam <=8 and peso_do_veiculo <=3500:
    print("Seu veiculo é da categoria:B")

elif quantidade_de_rodas >=4 and peso_do_veiculo >=3500 and peso_do_veiculo <=6000:
    print("Seu veículo é da categosria:C")

elif quantidade_de_rodas >=4 and quantidade_de_pessoas_acomodam >=8:
    print("Seu veículo é da categoria:D")

else:
    print("Seu veículo é da categosria:E")




