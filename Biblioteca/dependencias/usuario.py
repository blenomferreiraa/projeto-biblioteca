import itertools

class Usuario:
    
    id_livro = itertools.count(start=1)
    
    def __init__(self, nome, idade):
        
        self._id = next(Usuario.id_livro)
        
        self._nome = nome
        
        self._idade = idade
        
        self._lista_emprestimo = []
        
    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    def editar_nome(self, nome):
        self._nome = nome
        
    def editar_idade(self, idade):
        self._idade = idade
    
    def pegar(self, livro):
        if livro in self._lista_emprestimo:
            print("\n❌ O livro já está emprestado!")
            return
        
        self._lista_emprestimo.append(livro) 
        
    def entregar(self, livro):
        if not livro in self._lista_emprestimo:
            print("\n❌ O livro não está emprestado!")
            return
            
        self._lista_emprestimo.remove(livro)
    
    