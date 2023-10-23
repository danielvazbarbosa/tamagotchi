class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax
        self.energiaAtual = energiaMax
        self.saciedadeAtual = saciedadeMax
        self.limpezaAtual = limpezaMax
        self.idadeAtual = 0
        self.diamantes = 0
        self.vida = True

    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energiaAtual

    def getSaciedadeAtual(self):
        return self.saciedadeAtual

    def getLimpezaAtual(self):
        return self.limpezaAtual

    def getIdadeAtual(self):
        return self.idadeAtual

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        if self.energiaAtual > 0 and self.saciedadeAtual > 0 and self.limpezaAtual > 0 and self.idadeAtual <= self.idadeMax:
            self.vida = True
            return self.vida
        else:
            self.vida = False
            return 

    def brincar(self):
        if self.vida == True:
            self.energiaAtual -= 2
            self.saciedadeAtual -= 1
            self.limpezaAtual -= 3
            self.diamantes += 1
            self.idadeAtual += 1
            if self.energiaAtual >= self.energiaMax:
                self.energiaAtual = self.energiaMax
            if self.limpezaAtual >= self.limpezaMax:
                self.limpezaAtual = self.limpezaMax 
            if self.saciedadeAtual >= self.saciedadeMax:
                self.saciedadeAtual = self.saciedadeMax
            if self.idadeAtual >= self.idadeMax:
                self.idadeAtual = self.idadeMax
            return True
        else:
            return False

    def comer(self):
        if self.vida == True:
            self.energiaAtual -= 1
            self.saciedadeAtual += 4
            self.limpezaAtual -= 2
            self.idadeAtual += 1
            if self.energiaAtual >= self.energiaMax:
                self.energiaAtual = self.energiaMax
            if self.limpezaAtual >= self.limpezaMax:
                self.limpezaAtual = self.limpezaMax 
            if self.saciedadeAtual >= self.saciedadeMax:
                self.saciedadeAtual = self.saciedadeMax
            if self.idadeAtual >= self.idadeMax:
                self.idadeAtual = self.idadeMax
            return True
        else:
            return False

    def dormir(self):
        if self.vida == True:
            if self.energiaAtual <= self.energiaMax - 5:
                self.energiaAtual = self.energiaMax
                self.saciedadeAtual -= 2
                self.idadeAtual += 1
                if self.energiaAtual >= self.energiaMax:
                    self.energiaAtual = self.energiaMax
                if self.limpezaAtual >= self.limpezaMax:
                    self.limpezaAtual = self.limpezaMax 
                if self.saciedadeAtual >= self.saciedadeMax:
                    self.saciedadeAtual = self.saciedadeMax
                if self.idadeAtual >= self.idadeMax:
                    self.idadeAtual = self.idadeMax
                return True
            else: 
                return False
        else:
            return False

    def banhar(self):
        if self.vida == True:
            self.energiaAtual -= 3
            self.saciedadeAtual -= 1
            self.limpezaAtual = self.limpezaMax
            self.idadeAtual += 2
            if self.energiaAtual >= self.energiaMax:
                self.energiaAtual = self.energiaMax
            if self.limpezaAtual >= self.limpezaMax:
                self.limpezaAtual = self.limpezaMax 
            if self.saciedadeAtual >= self.saciedadeMax:
                self.saciedadeAtual = self.saciedadeMax
            if self.idadeAtual >= self.idadeMax:
                self.idadeAtual = self.idadeMax
            return True
        else:
            return False