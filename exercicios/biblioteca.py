class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
    def emprestar(self, disponivel):
        if self.disponivel:
            self.disponivel = False
            print("livro emprestado")
        print("livro indisponivel")

    def devolver(self, disponivel):
        
