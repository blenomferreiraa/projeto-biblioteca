from .livro import Livro
from .usuario import Usuario

class Biblioteca:
    
    def __init__(self):
        
        self.livros = []
        self.usuarios = []
        
    def cadastrar_livro(self):
        
        while True:
            titulo = input("Titulo: ").title().strip()
            
            if self.buscar_livro(titulo):
                print(f"\n❌ O livro {titulo} já existe")
                continue
            
            if not titulo:
                print("\n❌ O titulo do livro não pode está vazio!")
                continue
            
            if not titulo.replace(" ", "").isalnum():
                print("\n❌ O titulo do livro não pode conter caracteres especiais!")
                continue
            
            else:
                break
            
        while True:
            autor = input("Digite o nome do autor: ")
            
            if not autor:
                print("\n❌ O nome do autor não pode está vazio!")
                continue
            
            if not autor.replace(" ", "").isalpha():
                print("\n❌ O nome do autor deve conter somente letras!")
                continue
            
            if len(autor) <= 1:
                print("\n❌ O nome do autor deve conter mais que um caracter!")
                continue
            
            else:
                break
        
        while True:
            categoria = input("Digite a categoria do livro: ")
            
            if not categoria:
                print("\n❌ O campo categoria não pode está vazio!")
                continue
            
            if not categoria.replace(" ", "").isalpha():
                print("\n❌ O nome da categoria deve conter apenas letras!")
                continue
            
            if len(categoria) <= 3:
                print("\n❌ O campo categoria deve conter mais que 3 caracteres!")
                continue
            else:
                break
            
        while True:
            faixa_etaria = input("Digite a faixa etaria do livro: ").title().strip()
            
            if not faixa_etaria:
                print("\n❌ A faixa etaria não deve está vazia!")
                continue
            
            if not faixa_etaria.replace(" ", "").isalpha():
                print("\n❌ A faixa etaria deve conter apenas letras!")
                continue
            
            if len(faixa_etaria) <= 1:
                print("\n❌ A faixa etaria deve conter mais que um caracter!")
                continue
            
            else:
                break
            
        livro = Livro(titulo, autor, categoria, faixa_etaria)
        self.livros.append(livro)
        
        print(f"\n✅ O livro {livro.titulo} foi cadastrado com sucesso!\n")
            
    def buscar_livro(self, titulo):
        for livro in self.livros:
            if titulo.lower().strip() == livro.titulo.lower().strip():
                return livro
        return None
    
    def listar_livro(self):
        
        if not self.livros:
            print("\n❌ Nenhum livro cadastrado!")
            return
        
        for livro in self.livros:
            status = "✅ Disponivel" if livro.disponivel else "❌ Emprestado"
            
            print(f"\nId: {livro.id:<5} Titulo: {livro.titulo:<30} Autor: {livro.autor:<30} Categoria: {livro.categoria:<10} Faixa Etaria: {livro.faixa_etaria:<10} Status: {status:<10}")
    
    def editar_livro(self, titulo):
        
        livro = self.buscar_livro(titulo)
        
        if livro is None:
            print("\n❌ Livro não encontrado!")
            return
        
        while True:
            novo_titulo = input("Digite o novo titulo do livro: ").title().strip()
            
            if self.buscar_livro(novo_titulo):
                print("\n❌ Já existe um livro com esse titulo!")
                continue
            
            if not novo_titulo:
                print("\n❌ O novo titulo do livro não deve está vazio!")
                continue
            
            if not novo_titulo.replace(" ", "").isalnum():
                print("\n❌ O novo titulo não pode conter caracter especial!")
                continue
            
            else:
                break
            
        while True:
            
            novo_autor = input("Digite o nome do novo autor: ").title().strip()
            
            if not novo_autor:
                print("\n❌ O novo nome do autor não pode está vazio!")
                continue
            
            if len(novo_autor) <= 1:
                print("\n❌ O novo nome do autor deve ser maior que um caracter!")
                continue
            
            if not novo_autor.replace(" ", "").isalpha():
                print("\n❌ O novo nome do autor deve conter apenas letras!")
                continue
            
            else:
                break
            
        while True:
            nova_categoria = input("Digite a nova categoria do livro: ").title().strip()
            
            if not nova_categoria:
                print("\n❌ O campo nova categoria não pode está vazio!")
                continue
            
            if len(nova_categoria) <= 3:
                print("\n❌ A nova catgeoria não pode ser menor que quatro caracteres!")
                continue
            
            if not nova_categoria.replace(" ", "").isalpha():
                print("\n❌ A nova categoria não pode conter caracteres especiais!")
                continue
            
            else:
                break
        while True:
            nova_faixa_etaria = input("Digite a nova faixa etaria do livro: ").title().strip()
            
            if not nova_faixa_etaria:
                print("\n❌ A nova faixa etaria do livro não pode está vazia!")
                continue
            
            if not nova_faixa_etaria.replace(" ", "").isalpha():
                print("\n❌ A nova faixa etaria do livro deve conter apenas letras!")
                continue
            
            if len(nova_faixa_etaria) <= 1:
                print("\n❌ A nova faixa etaria do livro deve conter mais que um caracter!")
                continue
            
            else:
                break
            
        livro.editar_titulo(novo_titulo)
        livro.editar_autor(novo_autor)
        livro.editar_categoria(nova_categoria)
        livro.editar_faixa_etaria(nova_faixa_etaria)
        
        print(f"✅ O livro {titulo}, foi atualizado com sucesso!")
        
    def exibir_livro(self, titulo):
        livro = self.buscar_livro(titulo)
        
        if livro is None:
            print("\n❌ Livro não encontrado!")
            return
        
        status = "Disponivel" if livro._disponivel else "Emprestado"
        
        print(f"\nTitulo: {livro.titulo:<25} Autor: {livro.autor:<25} Categoria: {livro.categoria:<20} Faixa Etaria: {livro._faixa_etaria:<10} Status: {status}")
        
    def excluir_livro(self, titulo):
        livro = self.buscar_livro(titulo)
        
        if livro is None:
            print("\n❌ Livro não encontrado!")
            return
        
        if not livro._disponivel:
            print("\n❌ Impossivel excluir um livro que está emprestado!")
            return
        
        self.livros.remove(livro)
        print("\n✅ Livro excluido com sucesso!")
            
    
    def emprestar_livro(self, titulo, nome_usuario):
        livro = self.buscar_livro(titulo)
        
        if livro is None:
            print("\n❌ Livro não encontrado!")
            return
        
        usuario = self.buscar_usuario(nome_usuario)
        
        if usuario is None:
            print("\n❌ Usuario não encontrado!")
            return
        
        if livro._faixa_etaria == "Adulto" and usuario.idade < 18:
            print("\n❌ Emprestimo indisponivel! A idade não corresponde a Faixa Etaria permitada para este livro!")
            return
        
        if livro._faixa_etaria == "Jovem" and usuario.idade <= 15:
            print("\n❌ Emprestimo indisponivel! A idade não corresponde a Faixa Etaria permitada para este livro!")
            return
        
        livro.emprestar()
        usuario.pegar(livro)
        
    def devolver_livro(self, titulo, nome_usuario):
        livro = self.buscar_livro(titulo)
        
        if livro is None:
            print("\n❌ Livro não encontrado!")
            return
        
        usuario = self.buscar_usuario(nome_usuario)
        
        if usuario is None:
            print("\n❌ Usuario não encontrado!")
            return
        
        livro.devolver()
        usuario.entregar(livro)
                
    def cadastrar_usuario(self):
        
        while True:
            nome = input("Digite o nome do usuario: ").title().strip()
            
            if not nome:
                print("\n❌ O campo nome não pode está vazio!")
                continue
            
            if len(nome) <= 1:
                print("\n❌ O nome deve conter mais que 1 caracter!")
                continue
            
            if not nome.replace(" ", "").isalpha():
                print("\n❌ O campo nome não pode conter nenhum caracter especial!")
                continue
            
            else:
                break
            
        while True:
            idade = input("Digite a idade do usuario!").title().strip()
            
            try:
                idade = int(idade)
            except ValueError:
                print("\n❌ A idade do usuario deve conter apenas numeros inteiros!")
                continue
            
            if not idade:
                print("\n❌ A idade do usuario não pode está vazia!")
                continue
            
            if idade <= 0:
                print("\n❌ A idade do usuario deve ser maior quue ZERO!")
                continue
            
            if idade > 125:
                print("\n❌ A idade do usuario deve ser menor que 125 anos!")
                continue
            
            else:
                break
            
        usuario = Usuario(nome, idade)
        self.usuarios.append(usuario)
        
        print("✅ Usuario cadastrado com sucesso!")
        
    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if nome.title().strip() == usuario.nome.title().strip():
                return usuario
            
        return None
    
    def exibir_usuario(self, nome_usuario):
        usuario = self.buscar_usuario(nome_usuario)
        
        if usuario is None:
            print("\n❌ Usuario não encontrado!")
            return
        
        print(f"Nome: {usuario.nome:<25} Idade: {usuario.idade:<10} Livros emprestados: {len(usuario._lista_emprestimo):<10}")
    
    def editar_usuario(self, nome):
        usuario = self.buscar_usuario(nome)
        
        if usuario is None:
            print("\n❌ Usuario não encontrado!")
            return
        
        while True:
            novo_nome = input("Digite o novo nome do usuario: ").title().strip()
            
            if not novo_nome:
                print("\n❌ O novo nome do usuario não pode está vazio!")
                continue
            
            if not novo_nome.replace(" ", "").isalpha():
                print("\n❌ O novo nome do usuario deve conter apenas letras!")
                continue
            
            if len(novo_nome) <= 1:
                print("\n❌ O novo nome do usuario deve conter dois ou mais caracteres!")
                continue
            
            else:
                break
        
        while True:
            nova_idade = input("Digite a nova idade no usuario: ")
            
            try:
                nova_idade = int(nova_idade)
            except ValueError:
                print("\n❌ A nova idade do usuario deve conter somente numeros inteiros!")
                continue
            
            if nova_idade <= 0:
                print("\n❌ A nova idade do uzuario deve ser maior que ZERO!")
                continue
            
            if nova_idade > 125:
                print("\n❌ A nova idade do usuario deve ser menor que 125 anos!")
                continue
            
            else:
                break
        
        usuario.editar_nome(novo_nome)
        usuario.editar_idade(nova_idade)
        
        print("\n✅ Usuario atualizado com sucesso!")
            
    
    def listar_usuarios(self):
        if not self.usuarios:
            print("\n❌ Nenhum usuario cadastrado!")
            return
        
        for usuario in self.usuarios:
            print(f"Nome: {usuario.nome:<25} Idade: {usuario.idade:<10} Livros emprestados: {len(usuario._lista_emprestimo):<10}")
            
    def excluir_usuario(self, nome_usuario):
        usuario = self.buscar_usuario(nome_usuario)
        
        if usuario is None:
            print("\n❌ Usuario não encontrado!")
            return
        
        if usuario._lista_emprestimo:
            print("\n❌ Não é possivel excluir um usuario que esteja com um livro emprestado!")
            return
        
        self.usuarios.remove(usuario)
        print(f"✅ Usuario {nome_usuario} excluido com sucesso!")
        
        
        