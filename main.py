from lista import Lista
from auxiliares import get_min


class Node:
    def __init__(self, palavra):
        self.palavra = palavra
        self.esquerda = None
        self.direita = None
        self.contador = 0


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def insere(self, palavra):
        ponteiro = None
        referencia = self.raiz
        while referencia:
            ponteiro = referencia
            if palavra < referencia.palavra:
                referencia = referencia.esquerda
            elif palavra > referencia.palavra:
                referencia = referencia.direita
            else:
                print(f'palavra ja existente: {palavra}')
                return
        if ponteiro is None:
            self.raiz = Node(palavra)
            print(f'palavra inserida: {palavra}')
        elif palavra < ponteiro.palavra:
            ponteiro.esquerda = Node(palavra)
            print(f'palavra inserida: {palavra}')
        else:
            ponteiro.direita = Node(palavra)
            print(f'palavra inserida: {palavra}')

    def consulta_palavra(self, palavra):
        return self._consulta(self.raiz, palavra)

    def _consulta(self, no, palavra):
        if no is None:
            print(f'palavra inexistente: {palavra}')
            return
        if palavra == no.palavra:
            no.contador += 1
            print(f'palavra existente: {palavra} {no.contador}')
            return
        elif palavra < no.palavra:
            return self._consulta(no.esquerda, palavra)
        else:
            return self._consulta(no.direita, palavra)

    def mais_consultadas(self):
        if self.raiz is None:
            print('arvore vazia')
            return
        palavras_mais_consultadas = Lista()
        maior_contador = [0]
        self._encontra_maior_contador(self.raiz, maior_contador)
        self._encontra_palavras(
            self.raiz, maior_contador[0], palavras_mais_consultadas)
        if palavras_mais_consultadas.head is None:
            print('arvore vazia')
        else:
            print('palavras mais consultadas:')
            palavras_mais_consultadas.ordenar()
            palavras_mais_consultadas.imprimir()
            print(f'numero de acessos: {maior_contador[0]}')

    def _encontra_maior_contador(self, node, maior_contador):
        if node is not None:
            if node.contador > maior_contador[0]:
                maior_contador[0] = node.contador
            self._encontra_maior_contador(node.esquerda, maior_contador)
            self._encontra_maior_contador(node.direita, maior_contador)

    def _encontra_palavras(self, node, maior_contador, lista):
        if node is not None:
            if node.contador == maior_contador:
                lista.add(node.palavra)
            self._encontra_palavras(node.esquerda, maior_contador, lista)
            self._encontra_palavras(node.direita, maior_contador, lista)

    def ordem_alfabetica(self, l1, l2):
        lista_palavras = Lista()
        self._coloque_ordem(self.raiz, l1, l2, lista_palavras)
        if lista_palavras.head:
            print("Palavras em ordem:")
            lista_palavras.ordenar()
            lista_palavras.imprimir()
        else:
            print("Lista vazia")

    def _coloque_ordem(self, no, l1, l2, lista):
        if no is not None:
            if l1 <= no.palavra[0] <= l2:
                lista.add(no.palavra)
            if no.palavra[0] >= l1:
                self._coloque_ordem(no.esquerda, l1, l2, lista)
            if no.palavra[0] <= l2:
                self._coloque_ordem(no.direita, l1, l2, lista)

    def remove_palavra(self, palavra):
        self.raiz, removido = self._remove(self.raiz, palavra)
        if removido:
            print(f'palavra removida: {palavra}')
        else:
            print(f'palavra inexistente: {palavra}')

    def _remove(self, no, palavra):
        if no is None:
            return no, False
        if palavra < no.palavra:
            no.esquerda, removido = self._remove(no.esquerda, palavra)
            return no, removido
        elif palavra > no.palavra:
            no.direita, removido = self._remove(no.direita, palavra)
            return no, removido
        else:
            if no.esquerda is None and no.direita is None:
                return None, True
            elif no.esquerda is None:
                return no.direita, True
            elif no.direita is None:
                return no.esquerda, True
            else:
                substituto = get_min(no.direita)
                no.palavra = substituto.palavra
                no.contador = substituto.contador
                no.direita, _ = self._remove(no.direita, substituto.palavra)
            return no, True

    def nivel(self, level):
        if self.raiz is not None:
            caminho = Lista()
            self._mostre_nivel(self.raiz, 1, level, caminho)
            if caminho.head:
                print(f'palavras no nivel: {level}')
                caminho.ordenar()
                caminho.imprimir()
            else:
                print(f'nao ha nos com nivel: {level}')
        else:
            print(f'nao ha nos com nivel: {level}')

    def _mostre_nivel(self, node, atual, level, caminho):
        if node is not None:
            self._mostre_nivel(node.esquerda, atual + 1, level, caminho)
            if atual == level:
                caminho.add(node.palavra)
            self._mostre_nivel(node.direita, atual + 1, level, caminho)

    def listar_caminho(self, palavra):
        caminho = Lista()
        if self._listar_caminho_para_palavra(self.raiz, palavra, caminho):
            print('palavras no caminho:')
            caminho.ordenar()
            caminho.imprimir()
        else:
            print(f'palavra inexistente: {palavra}')

    def _listar_caminho_para_palavra(self, no, palavra, caminho):
        if no is None:
            return False
        caminho.add(no.palavra)
        if no.palavra == palavra:
            return True
        if palavra < no.palavra:
            if self._listar_caminho_para_palavra(no.esquerda, palavra, caminho):
                return True
        else:
            if self._listar_caminho_para_palavra(no.direita, palavra, caminho):
                return True
        caminho.remove()
        return False

    def _imprime(self, node):
        if node is None:
            return
        if node.esquerda:
            pont_esq = node.esquerda.palavra
        else:
            pont_esq = "nil"
        if node.direita:
            pont_dir = node.direita.palavra
        else:
            pont_dir = "nil"
        print(f'palavra: {node.palavra} freq: {node.contador} fesq: {pont_esq} fdir: {pont_dir}')
        self._imprime(node.esquerda)
        self._imprime(node.direita)

    def impressao_arvore(self):
        if self.raiz is None:
            print("arvore vazia")
        else:
            self._imprime(self.raiz)


def processa_comandos(arvore, comandos):
    for comando in comandos:
        if comando[0] == 'i':
            palavra = comando[1]
            arvore.insere(palavra)
        elif comando[0] == 'c':
            palavra = comando[1]
            arvore.consulta_palavra(palavra)
        elif comando[0] == 'f':
            arvore.mais_consultadas()
        elif comando[0] == 'o':
            l1, l2 = comando[1], comando[2]
            arvore.ordem_alfabetica(l1, l2)
        elif comando[0] == 'r':
            palavra = comando[1]
            arvore.remove_palavra(palavra)
        elif comando[0] == 'n':
            nivel = int(comando[1])
            arvore.nivel(nivel)
        elif comando[0] == 't':
            palavra = comando[1]
            arvore.listar_caminho(palavra)
        elif comando[0] == 'p':
            arvore.impressao_arvore()
        elif comando[0] == 'e':
            break


if __name__ == "__main__":
    import sys

    arvore = ArvoreBinariaBusca()
    print("Digite seus comandos. Para finalizar, digite 'e'.")
    while True:
        comando = input().strip()
        if comando == 'e':
            break
        elif comando == 'i':
            palavra = input().strip()
            arvore.insere(palavra)
        elif comando == 'c':
            palavra = input().strip()
            arvore.consulta_palavra(palavra)
        elif comando == 'r':
            palavra = input().strip()
            arvore.remove_palavra(palavra)
        elif comando == 't':
            palavra = input().strip()
            arvore.listar_caminho(palavra)
        elif comando == 'o':
            l1 = input().strip()
            l2 = input().strip()
            arvore.ordem_alfabetica(l1, l2)
        elif comando == 'n':
            nivel = int(input().strip())
            arvore.nivel(nivel)
        elif comando == 'f':
            arvore.mais_consultadas()
        elif comando == 'p':
            arvore.impressao_arvore()

    arvore = ArvoreBinariaBusca()
    processa_comandos(arvore, comando)

# versao: Python 3.12.4
