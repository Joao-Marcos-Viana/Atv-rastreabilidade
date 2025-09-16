import random
num = random.randint(1,10)
tentativa = 0
while tentativa < 3:
    print('='*30)
    print('Tente acertar o numero da sorte!')
    print('Você tem 3 tentativas')
    print('='*30)
    
    chute = int(input('Tentativa: '))
    print('='*30)
    tentativa += 1
    if chute > num:
        print("Muito alto")
        print('='*30)
    elif chute < num:
        print("Muito baixo")
        print('='*30)
    elif chute == num:
        print("Acertou")
        print('='*30)
        break
