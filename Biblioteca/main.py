from dependencias.biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:
    
    print("-=" * 30)
    print("Menu".center(60, " "))
    print("-=" * 30)
    
    opcao = input('''
[ 1 ] - Cadastrar Livro
[ 2 ] - Buscar Livro
[ 3 ] - Editar Livro
[ 4 ] - Excluir Livro
[ 5 ] - Emprestar Livro
[ 6 ] - Devolver Livro
[ 7 ] - Cadastrar Usuario
[ 8 ] - Buscar Usuario
[ 9 ] - Editar Usuario
[ 10 ] - Excluir Usuario
[ 11 ] - Sair

Escolha uma opção: ''')
    
    try:
        opcao = int(opcao)
    except ValueError:
        print("\n❌ Escolha apenas uma opção valida! Este campo aceita somente numeros inteiros!")
        continue
    
    if opcao == 11:
        print("Saindo...")
        break
        
    elif opcao == 1:
        print()
        print("Cadastro de Livro".center(60, "-"))
        print()
        
        biblioteca.cadastrar_livro()
        
    elif opcao == 2:
        print()
        print("Buscar Livro".center(60, "-"))
        print()
        
        titulo = input("Digite o titulo do livro: ").title().strip()
        resultado = biblioteca.buscar_livro(titulo)
        
        if resultado is None:
            print("\n❌ Livro não encontrado!")
            continue
        
        biblioteca.exibir_livro(resultado.titulo)
        
    elif opcao == 3:
        print()
        print("Editar Livro".center(60, "-"))
        print()
        
        while True:
            titulo = input("Digite o titulo do livro que deseja editar: ").title().strip()
            
            if not titulo:
                print("\n❌ Este campo não pode esta vazio")
                continue
            
            else:
                break
        
        biblioteca.editar_livro(titulo)
        
    elif opcao == 4:
        print()
        print("Excluir Livro".center(60, "-"))
        print()
        
        while True:
            titulo = input("Digite o titulo do livro que deseja excluir: ")

            if not titulo:
                print("\n❌ Este campo não pode estar vazio!")
                continue
            
            else:
                break
            
        biblioteca.excluir_livro(titulo)
        
    elif opcao == 5:
        print()
        print("Emprestar Livro".center(60, "-"))
        print()
        
        while True:
            titulo = input("Digite o titulo do livro a ser emprestado: ")
            
            if not titulo:
                print("\n❌ Este campo não pode estar vazio!")
                continue
            
            else:
                break
            
        while True:
            usuario = input(f"Digite o nome completo do usuario que esta pegando o livro {titulo} emprestado: ")
            
            if not usuario:
                print("\n❌ Este campo não pode estar vazio!")
                continue
            
            if not usuario.replace(" ", "").isalpha():
                print("\n❌ Este campo acenta somente letras!")
                continue
            
            else:
                break
            
        biblioteca.emprestar_livro(titulo, usuario)
        
    elif opcao == 6:
        print()
        print("Devolver Livro".center(60, "-"))
        print()
        
        while True:
            titulo = input("Digite o titulo do livro a ser devolvido: ")
            
            if not titulo:
                print("\n❌ Este campo não pode estar vazio!")
                continue
            
            else:
                break
            
        while True:
            usuario = input(f"Digite o nome completo do usuario que esta devolvendo o livro {titulo}: ")
            
            if not usuario:
                print("\n❌ Este campo não pode estar vazio!")
                continue
            
            if not usuario.replace(" ", "").isalpha():
                print("\n❌ Este campo acenta somente letras!")
                continue
            
            else:
                break
            
        biblioteca.devolver_livro(titulo, usuario)
        
    elif opcao == 7:
        print()
        print("Cadastro de Usuarios".center(60, "-"))
        print()
        
        biblioteca.cadastrar_usuario()
        
    elif opcao == 8:
        print()
        print("Buscar Usuario".center(60, "-"))
        print()
        
        while True:
            nome_usuario = input("Digite o nome do usuario que deseja buscar: ")
            
            if not nome_usuario:
                print("\n❌ Este campo não pode está vazio!")
                continue
            
            if not nome_usuario.replace(" ", "").isalpha():
                print("\n❌ Este campo aceita somente letras!")
                continue
            
            else:
                break
            
        biblioteca.exibir_usuario(nome_usuario)
        
    elif opcao == 9:
        print()
        print("Editar Usuario".center(60, "-"))
        print()
        
        while True:
            nome_usuario = input("Digite o nome do usuario que deseja editar: ")
            
            if not nome_usuario:
                print("\n❌ Este campo não pode está vazio!")
                continue
            
            if not nome_usuario.replace(" ", "").isalpha():
                print("\n❌ Este campo aceita somente letras!")
                continue
            
            else:
                break
            
        biblioteca.editar_usuario(nome_usuario)
        
    elif opcao == 10:
        print()
        print("Excluir Usuario".center(60, "-"))
        print()
        
        while True:
            nome_usuario = input("Digite o nome do usuario que deseja excluir: ")
            
            if not nome_usuario:
                print("\n❌ Este campo não pode está vazio!")
                continue
            
            if not nome_usuario.replace(" ", "").isalpha():
                print("\n❌ Este campo aceita somente letras!")
                continue
            
            else:
                break
        
        biblioteca.excluir_usuario(nome_usuario)            