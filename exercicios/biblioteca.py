class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
    def emprestar(self):
        if not self.disponivel:
            print("o livro nao esta disponivel")
            return
        self.disponivel = False
        print("livro emprestado")
        return self.disponivel
        

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print("livro devolvido")
            return self.disponivel
        return self.disponivel

    def mostrar_informacoes(self):
        titulo = self.titulo
        autor = self.autor
        disponivel = "disponivel" if self.disponivel else "nao disponivel"
        print(f"informacoes do livro\ntitulo: {titulo}\nautor: {autor}\ndisponibilidade: {disponivel}")
        return 





livro_1 = Livro("Harry Potter", "nao lembro")

livro_1.emprestar()
livro_1.emprestar()
livro_1.mostrar_informacoes()