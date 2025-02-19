userInput = input("Digite o seu nome")

if len(userInput) > 12:
    print("O nome é muito grande!")
elif userInput.count(" ") > 0:
    print("O nome não pode conter espaços!")
elif not userInput.isalpha():
    print("O nome não pode conter digitos!")
else :
    print("Nome validado com sucesso!")
