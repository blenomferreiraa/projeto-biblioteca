import itertools

class Livro:
    id_livro = itertools.count(start=1)
    
    def __init__(self, titulo, autor, categoria, faixa_etaria):
        self._id = next(Livro.id_livro)
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria
        self._faixa_etaria = faixa_etaria
        self._disponivel = True
    
    @property
    def id(self):
        return self._id
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def faixa_etaria(self):
        return self._faixa_etaria
    
    @property
    def disponivel(self):
        return self._disponivel
    
    def editar_titulo(self, titulo):
        self._titulo = titulo
        
    def editar_autor(self, novo_autor):
        self._autor = novo_autor
        
    def editar_categoria(self, nova_categoria):
        self._categoria = nova_categoria
        
    def editar_faixa_etaria(self, nova_faixa_etaria):
        self._faixa_etaria = nova_faixa_etaria
        
    def emprestar(self):
        if not self.disponivel:
            print("\n❌ O livro não está disponivel!")
            return
        
        self._disponivel = False
        
        print(f"\n✅ Livro {self.titulo} emprestado com sucesso!")
        
    def devolver(self):
        if self._disponivel:
            print("\n❌ O livro não está emprestado!")
            return
        
        self._disponivel = True
        print(f"\n✅ Livro {self.titulo} devolvido com sucesso!")
        
    
        
        
    