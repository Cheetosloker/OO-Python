class Programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Duracação: {self.duracao} - Likes: {self.likes}')

class Serie(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self.likes}')

class playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._Programas = programas

    def __getitem__(self, item):
        return self._Programas[item]

    @property
    def listagem(self):
        return self._Programas

    def __len__(self):
        return len(self._Programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2019, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

tmep.dar_like()
demolidor.dar_like()
vingadores.dar_like()
atlanta.dar_like()

filmes_e_serie = [vingadores, atlanta, tmep, demolidor]
playslist_fim_de_semana = playlist('fim de semana', filmes_e_serie)

print(f'Tamanho da playlist: {len(playslist_fim_de_semana.listagem)}')
len(playslist_fim_de_semana)
for Programas in playslist_fim_de_semana.listagem:
    print(Programas)
