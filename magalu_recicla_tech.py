# Programa: Magalu Recicla Tech
# Objetivo: simular o registro de descarte de lixo eletrônico
# e calcular pontos conforme o peso do material descartado.
def calcular_pontos(peso):
    """
    Função simples para calcular a pontuação do usuário.
    Para esta simulação, cada quilo descartado corretamente gera 10 pontos.
    """
    pontos = peso * 10
    return pontos
def classificar_material(material):
    """
    Função simples para classificar o tipo de resíduo eletrônico informado.
    """
    material = material.lower()
    if material in ["celular", "tablet", "notebook", "computador"]:
        return "Equipamento eletrônico"
    elif material in ["carregador", "cabo", "fone", "controle"]:
        return "Acessório eletrônico"
    elif material in ["pilha", "bateria"]:
        return "Resíduo com cuidado especial"
    else:
        return "Outro tipo de resíduo eletrônico"
# Início do programa
print("=== MAGALU RECICLA TECH ===")
print("Sistema de registro de descarte de lixo eletrônico")
nome_usuario = input("Digite o nome do usuário: ")
total_pontos = 0
total_peso = 0
continuar = "sim"
while continuar == "sim":
    material = input("\nInforme o material que será descartado: ")
    peso = float(input("Informe o peso do material em kg: "))
    if peso > 0:
        categoria = classificar_material(material)
        pontos = calcular_pontos(peso)
        total_pontos = total_pontos + pontos
        total_peso = total_peso + peso
        print("\nRegistro realizado com sucesso!")
        print("Material descartado:", material)
        print("Classificação:", categoria)
        print("Peso registrado:", peso, "kg")
        print("Pontos gerados:", pontos)
        if categoria == "Resíduo com cuidado especial":
            print("Atenção: pilhas e baterias precisam de coleta e destinação específicas.")
        else:
            print("Material registrado para encaminhamento à logística reversa.")
    else:
        print("Peso inválido. O peso deve ser maior que zero.")
    continuar = input("\nDeseja registrar outro descarte? Digite sim ou não: ").lower()
print("\n=== RESUMO DO USUÁRIO ===")
print("Usuário:", nome_usuario)
print("Peso total descartado:", total_peso, "kg")
print("Total de pontos acumulados:", total_pontos)
print("Obrigado por contribuir com o descarte correto de lixo eletrônico!")

