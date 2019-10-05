from tkinter import *
import math
import random
 
class No(object):
    def __init__(self, val, esquerdo=None, direito=None):
        self.val = val
        self.esquerdo = esquerdo
        self.direito = direito
 
class Arvore(object):
    def __init__(self):
        self.raiz = None
 
    def set_raiz(self, raiz):
        self.raiz = Arvore()
        self.raiz = No(raiz)
         
    def add(self, x):
        if(self.raiz == None):
            self.set_raiz(x)
            return self
        elif(x > self.raiz.val):
            if( (self.raiz.direito) is None ):
                self.raiz.direito = Arvore()
                self.raiz.direito.set_raiz(x)
                return self.raiz.direito
            else:
                (self.raiz.direito).add(x)
        elif(x < self.raiz.val):
            if( (self.raiz.esquerdo) is None):
                self.raiz.esquerdo = Arvore()
                self.raiz.esquerdo.set_raiz(x)
                return self.raiz.esquerdo
            else:
                (self.raiz.esquerdo).add(x)
 
    def niveis(self):
        e=0
        if self.raiz.esquerdo:
            e = self.raiz.esquerdo.niveis()
        d=0
        if self.raiz.direito:
            d = self.raiz.direito.niveis()
        return 1+max(e,d)
 
 
    def fator(self):
        e=0
        if self.raiz.esquerdo:
            e = self.raiz.esquerdo.niveis()
        d=0
        if self.raiz.direito:
            d = self.raiz.direito.niveis()
        return e-d
 
    def set_filhos(self, e, d):
        self.raiz.esquerdo = e
        self.raiz.direito = d
 
    def rotacao_esq(self):
        self.raiz.val, self.raiz.direito.raiz.val = self.raiz.direito.raiz.val, self.raiz.val
        aux = self.raiz.esquerdo
        self.set_filhos(self.raiz.direito, self.raiz.direito.raiz.direito)
        self.raiz.esquerdo.set_filhos(aux, self.raiz.esquerdo.raiz.esquerdo)
 
    def rotacao_dir(self):
        self.raiz.val, self.raiz.esquerdo.raiz.val = self.raiz.esquerdo.raiz.val, self.raiz.val
        aux = self.raiz.direito
        self.set_filhos(self.raiz.esquerdo.raiz.esquerdo, self.raiz.esquerdo)
        self.raiz.direito.set_filhos(self.raiz.direito.raiz.direito, aux)
 
         
    def rotacao_esq_dir(self):
        self.raiz.esquerdo.rotacao_esq()
        self.rotacao_dir()
 
    def rotacao_dir_esq(self):
        self.raiz.direito.rotacao_dir()
        self.raiz.rotacao_esq()
 
    def balancear(self):
        fat = self.fator()
        if fat > 1:
            if self.raiz.esquerdo.fator() > 0:
                self.rotacao_dir()
            else:
                self.rotacao_esq_dir()
        elif fat < -1:
            if self.raiz.direito.fator() < 0:
                self.rotacao_esq()
            else:
                self.rotacao_dir_esq()
 
    def profundidade(self):
        e=0
        d=0
        if self.raiz.esquerdo: e=self.raiz.esquerdo.niveis()
        if self.raiz.direito: d=self.raiz.direito.niveis()
        return 1+max(e,d)
   
class Aplicacao:
    def __init__(self, pai):
        self.arvoreBinaria = None
        self.t1 = Entry(pai)
        self.t1.bind("<Return>", self.constroiArvore)
        self.t1.pack()
        self.b1 = Button(pai)
        self.b1.bind("<Button-1>", self.constroiArvore)
        self.b1["text"] = "ENTRE COM VALOR"
        self.b1.pack()
        self.c1 = Canvas(pai, width=1024, height=650)
        self.c1.pack()
 
    def constroiArvore(self, *args):
        try:
            valor = int(self.t1.get())
        except Exception:
            return
        print(valor)
        if self.arvoreBinaria == None:
            print("Criando")
            self.arvoreBinaria = Arvore()
            self.raiz = self.arvoreBinaria.add(valor)
        else:
            print("Inserindo")
            self.arvoreBinaria.add(valor)
        self.desenhaArvore()
 
    def desenhaArvore(self):
        self.HORIZONTAL = 1024
        self.VERTICAL = 750
        self.tamanho = 30
        self.c1.delete(ALL)
        self.c1.create_rectangle(
            0, 0, self.HORIZONTAL, self.VERTICAL, fill="red")
        self.xmax = self.c1.winfo_width() - 40  # margem de 40
        self.ymax = self.c1.winfo_height()
        self.numero_linhas = self.arvoreBinaria.profundidade()
        x1 = int(self.xmax / 2 + 20)
        y1 = int(self.ymax / (self.numero_linhas + 1))
        self.arvoreBinaria.balancear()
        self.desenhaNoh(self.raiz, x1, y1, x1, y1, 1)
 
    def desenhaNoh(self, noh, posAX, posAY, posX, posY, linha):
        if noh == None:
            return
        numero_colunas = 2**(linha + 1)
        x1 = int(posX - self.tamanho / 2)
        y1 = int(posY - self.tamanho / 2)
        x2 = int(posX + self.tamanho / 2)
        y2 = int(posY + self.tamanho / 2)
        self.c1.create_line(posAX, posAY, posX, posY, fill="white")
        self.c1.create_oval(x1, y1, x2, y2, fill="white")
        self.c1.create_text(posX, posY, text=str(noh.raiz.val))
        posAX, posAY = posX, posY
        dx = self.xmax / numero_colunas
        dy = self.ymax / (self.numero_linhas + 1)
        posX = posAX + dx
        posY = posAY + dy
        self.desenhaNoh(noh.raiz.direito, posAX, posAY, posX, posY, linha + 1)
        posX = posAX - dx
        self.desenhaNoh(noh.raiz.esquerdo, posAX, posAY, posX, posY, linha + 1)
     
 
if __name__ == "__main__":
    root = Tk(None, None, "Desenhando Uma Árvore Binária")
    root.geometry("1024x750")
    ap = Aplicacao(root)
    root.mainloop()