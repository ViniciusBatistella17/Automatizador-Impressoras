import os
import subprocess


def instalar_impressora(fabricante):

    drivers = os.listdir("drivers/" + fabricante)
    print (f"Drivers {fabricante}:")
    drivers_exe = []

    for driver in drivers:
        if driver.endswith(".exe"):
            drivers_exe.append(driver)
    if not drivers_exe:
            print("Não tem drivers aqui")
            return
    for numero, driver in enumerate(drivers_exe, 1):
        print(f"{numero}. {driver}")
     
    while True:
        try:
            impressora_driver = input("Digite o numero do driver que você quer instalar: ")
            if 1 <= int(impressora_driver) <= len(drivers_exe):
                lista_driver = int(impressora_driver) - 1
                break
            else:
                print("Não tem esse numero de driver")
        except:
            print("Digite um numero:")
            continue
    while True:
        subprocess.run(f"drivers/" + fabricante + "/" + drivers_exe[lista_driver])
        while True:
            resposta = input("A impressora foi instalada? ")
            resposta = resposta.lower()
            if resposta == "sim":
                exit()
            elif resposta == "nao":
                return
            else:
                print("Digita sim ou nao")
            
def instalar_por_ip():
    subprocess.run([
        "rundll32",
        "printui.dll,PrintUIEntry",
        "/il",
    ])

while True:
    print ("====================================")
    print ("  AUTOMATIZADOR DE IMPRESSORAS V1")
    print ("====================================")
    print ("")
    print (" 1 - Instalar pelo instalador da impressora")
    print (" 2 - Instalar pelo IP da impressora")
    escolha_modo = input("Escolha o modo de instalação: ")
    if escolha_modo == "1":
        print (" Modelos disponíveis: ")
        print (" 1 - HP")
        print (" 2 - Brother")
        print (" 3 - Epson")
        print (" 4 - Canon")
        print ("")
        
        escolha = input("Escolha o modelo da impressora: ")
        
        if escolha == "1":
            instalar_impressora("HP")

        elif escolha == "2":
            instalar_impressora("Brother")

        elif escolha == "3":
            instalar_impressora("Epson")
   
        elif escolha == "4":    
            instalar_impressora("Canon")

        else:
            print("Esse numero não tem, digita outro.")
    
    elif escolha_modo == "2":
        instalar_por_ip()
