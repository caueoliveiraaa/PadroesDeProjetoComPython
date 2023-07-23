import os 
import random

class Programa:
    def __init__(self, nome, ano):
        self._nome: str = nome.title()
        self.ano: int = ano
        self._likes = 0
        
    @property
    def likes(self) -> int:
        return self._likes
        
    def dar_like(self) -> None:
        self._likes += 1
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome) -> None:
        self._nome = novo_nome
        
    def __str__(self) -> None:
        return f'{self.nome}, {self.ano}, {self.likes} Likes'
        
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao: int = duracao
        
    def __str__(self) -> None:
        return f'{self.nome}, {self.ano}, {self.duracao} min, {self.likes} Likes'
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas: int = temporadas
        
    def __str__(self) -> None:
        return f'{self.nome}, {self.ano}, {self.temporadas} temporadas, {self.likes} Likes'
        
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Possibilitando iteracao
    def __getitem__(self, item):
        self._programas[item]

    # Getter para todos os programas
    @property
    def listagem(self):
        return self._programas
    
    # Possibilitanto retornar len dos _programas
    def __len__(self):
        return len(self._programas)
    

if __name__ == '__main__':
    os.system("cls")
    
    # Instanciando objetos
    matrix = Filme("The matrix", 2000, 160)
    her = Filme("Her", 2012, 180)
    mr_robot = Serie("Mr. Robot", 2018, 5)
    black_mirror = Serie("Black Mirror", 2015, 6)
    
    # Adicionando likes aos filmes e séries
    filmes_e_series = [matrix, mr_robot, her, black_mirror]
    for programa in filmes_e_series:
        random_number = random.randint(150, 999)
        for _ in range(random_number):
            programa.dar_like()
    
    # Tornando os objetos iteráveis com classe Playlist do tipo list
    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)
    print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")
    
    # Usando __str__ para print representando o objeto da classe
    for programa in playlist_fim_de_semana.listagem:
        print(programa)
        