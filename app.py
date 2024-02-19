import pyautogui
from time import sleep

# - Passos manuais para realização desse processo:

# - Registrar novo usuário:
    # 1- Clicar em "Cadastrar novo usuário"
pyautogui.click(995,679,duration=0.001)

    # 2- Clicar e cadastrar usuário
pyautogui.click(971,604, duration=.001)
pyautogui.write('Otavio')

    # 3- Clicar e cadastra senha
pyautogui.click(970,639, duration=0.001)
pyautogui.write('otavvioo')

    # 4- Clicar em "Registrar novo funcionário"
pyautogui.click(951,677, duration=0.001)


# 1- Clicar e digitar o usuário
pyautogui.click(986,602, duration=0.001)
pyautogui.write('Otavio')

# 2- Clicar e digitar a senha
pyautogui.click(978,640, duration=0.001)
pyautogui.write('otavvioo')

# 3- Clicar no botão "Entrar"
pyautogui.click(818,680, duration=0.001)

# 4- Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

# 	1- Clicar e digitar produtol
        pyautogui.click(578,582, duration=0.001)
        pyautogui.write(produto)

# 	2- Clicar e digitar quantidade	
        pyautogui.click(633,622, duration=0.001)
        pyautogui.write(quantidade)

# 	3- Clicar e digitar preçoProduto 4
        pyautogui.click(610,660, duration=0.001)
        pyautogui.write(preco)

# 	4- Clicar em "Registrar"
        pyautogui.click(417,897, duration=0.001)

        sleep(0.5)