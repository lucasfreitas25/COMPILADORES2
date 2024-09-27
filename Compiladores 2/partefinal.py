class MaqHipo:
    def __init__(self):
        self.codigos = []
        self.dados = []
        self.escopoMain = {}
        self.escopoMetodo = {}
        self.posicao = 0
        self.isMetodo = False

    def adicionar_codigo(self, instrucao, argumento):
        self.codigos.append((instrucao, argumento))
    
    def empilhar_dado(self, dado):
        self.dados.append(dado)
    
    def desempilhar_dado(self):
        if self.dados:
            return self.dados.pop()
        else:
            raise IndexError("A pilha está vazia")

    def topo(self):
        if self.dados:
            return self.dados[-1]
        else:
            raise IndexError("A pilha está vazia")


maq = MaqHipo()


try:
    with open("output.j", "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                chave, valor = parts
                maq.adicionar_codigo(chave, valor)  
            else:
                chave = parts[0]
                maq.adicionar_codigo(chave, None)  
except Exception as e:
    print(f"Ocorreu um erro: {e}")
while int(maq.posicao) < len(maq.codigos):
    print(maq.posicao)  
 
    instrucao, argumento = maq.codigos[maq.posicao]


    if instrucao == "PARA":
        break
    
    elif instrucao == "INPP":
        pass
    
    elif instrucao == "CRCT":
        
        valor = float(argumento)
        maq.empilhar_dado(valor)
    
    elif instrucao == "CRVL":
        if maq.isMetodo:
            valor = maq.escopoMetodo.get(argumento, 0)
        else:
            valor = maq.escopoMain.get(argumento, 0)
        maq.empilhar_dado(valor)
        
    elif instrucao == "SOMA":
        valor1 = maq.desempilhar_dado()
        valor2 = maq.desempilhar_dado()
        maq.empilhar_dado(valor1 + valor2)
        
    elif instrucao == "SUBT":
        valor1 = maq.desempilhar_dado()
        valor2 = maq.desempilhar_dado()
        maq.empilhar_dado(valor2 - valor1)
        
    elif instrucao == "MULT":
        valor1 = maq.desempilhar_dado()
        valor2 = maq.desempilhar_dado()
        maq.empilhar_dado(valor1 * valor2)
        
    elif instrucao == "DIVI":
        valor1 = maq.desempilhar_dado()
        valor2 = maq.desempilhar_dado()
        maq.empilhar_dado(valor2 / valor1)
        
    elif instrucao == "INVE":
        valor1 = maq.desempilhar_dado()
        maq.empilhar_dado(-valor1)
        
    elif instrucao == "CPME":
        valor1 = maq.desempilhar_dado()
        valor2 = maq.desempilhar_dado()
        maq.empilhar_dado(valor2 < valor1)
        
    elif instrucao == "CPIG":
        valor1 = maq.desempilhar_dado()
        valor2 = maq.desempilhar_dado()
        maq.empilhar_dado(valor1 == valor2)
        
    elif instrucao == "CDES":
        valor1 = maq.desempilhar_dado()
        valor2 = maq.desempilhar_dado()
        maq.empilhar_dado(valor1 != valor2)
        
    elif instrucao == "CPMI":
        valor1 = maq.desempilhar_dado()
        valor2 = maq.desempilhar_dado()
        maq.empilhar_dado(valor2 <= valor1)
        
    elif instrucao == "CPMA":
        valor1 = maq.desempilhar_dado()
        valor2 = maq.desempilhar_dado()
        maq.empilhar_dado(valor2 >= valor1)
        
    elif instrucao == "ARMZ":
        valor1 = maq.desempilhar_dado()
        if maq.isMetodo:
            maq.escopoMetodo[argumento] = valor1
        else:
            maq.escopoMain[argumento] = valor1
            
    elif instrucao == "DSVI":
        maq.posicao = int(argumento)
        continue  
    
    elif instrucao == "DSVF":
        valor1 = maq.desempilhar_dado()
        if not valor1:
            maq.posicao = int(argumento)
            continue
    
    elif instrucao == "LEIT":
        valor = float(input())
        maq.empilhar_dado(valor)
    
    elif instrucao == "IMPR":
        valor = maq.desempilhar_dado()
        print(valor)
    
    elif instrucao == "CHPR":
        maq.posicao += 1
        maq.isMetodo = True
        maq.escopoMetodo.clear()
        
        continue

    
    elif instrucao == "PSHR":
        valor = int(argumento)
        maq.empilhar_dado(valor)
    
    elif instrucao == "RTPR":
        valor1 = maq.desempilhar_dado()
        maq.posicao = valor1
        maq.isMetodo = False
        continue
    
    else:
        print(f"Instrução desconhecida: {instrucao}")
        
    maq.posicao += 1
