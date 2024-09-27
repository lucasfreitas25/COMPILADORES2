import ply.yacc as yacc
import ply.lex as lex
from lexico import myLexer

#PROBLEMAS: 
# LOOPING

tokens = myLexer.tokens

precedencia = (
    ('left', 'SUM', 'MENOS'),
    ('left', 'MUL', 'DIVI'),
)

metodos = []
tabela_simbolos = {}  
escopo_atual = [{}]  
lista_printar = []
erros = 0

def inserir_variavel(nome, tipo):
    if nome in escopo_atual[-1]:
        print(f"Erro semântico: variável '{nome}' já declarada no escopo atual.")
    else:
        escopo_atual[-1][nome] = tipo
        tabela_simbolos[nome] = {'tipo': tipo, 'valor': None}
    

def verificar_variavel(nome):
    for escopo in reversed(escopo_atual):
        if nome in escopo:
            return escopo[nome]  
    print(f"Erro semântico: variável '{nome}' não declarada.")
    return None

def atribuir_valor(nome, valor):
    if nome in tabela_simbolos:  
        tabela_simbolos[nome]['valor'] = valor
    else:
        raise Exception(f"Tipo incompatível para a variável '{nome}'.")
    

def obter_valor(termo):
    try:
        if termo in tabela_simbolos:
            return tabela_simbolos[termo]['valor']
        else:
            return float(termo)
    except ValueError:
        print(f"Erro: termo {termo} não é um número ou variável válida")
        return None


def entrar_escopo():
    escopo_atual.append({})


def sair_escopo():
    escopo_atual.pop()


def p_prog(p):
    'PROG : PUBLIC CLASS ID LCBRA PUBLIC STATIC VOID MAIN LPAR STRING LSBRA RSBRA ID RPAR LCBRA CMDS RCBRA METODO RCBRA'
    p[0] = ("PROG", p[3], p[16], p[18])
    


def p_metodo(p):
    """METODO : PUBLIC STATIC TIPO ID LPAR PARAMS RPAR LCBRA CMDS RETURN EXPRESSAO SEMICOLON RCBRA
              | empty"""
    
    global metodos
    metodos.append(p[4])  
    codegen.emit('PARA')
    codegen.incrementar_posicao()
    retorno_metodo = codegen.retorno_metodo() 
    retorno_metodo += codegen.retorno_posicao()+1

    entrar_escopo()
    if len(p) == 14:
        p[0] = ("METODO", p[3], p[4], p[6], p[9], p[10], p[12])
      
        
        codegen.emit("RTPR ")
        codegen.incrementar_posicao()
    sair_escopo()  


def p_params(p):
    """PARAMS : TIPO ID MAIS_PARAMS
              | empty"""
    if len(p) == 4:
        p[0] = ("PARAMS", p[1], p[2], p[3])
    else:
        p[0] = None


def p_mais_params(p):
    """MAIS_PARAMS : VIRGU PARAMS
                   | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None


def p_dc(p):
    """DC : VAR MAIS_CMDS
          """
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = None


def p_var(p):
    'VAR : TIPO VARS'
    p[0] = (p[1], p[2])

    tipo = p[1]  
    for var in p[2]:
        inserir_variavel(var, tipo)

    
def p_vars(p):
    'VARS : ID MAIS_VAR'
    p[0] = [p[1]] + (p[2] if p[2] else [])
    


def p_mais_var(p):
    """MAIS_VAR : VIRGU VARS
                | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []
   
        
def p_tipo(p): #CONCLUIDO
    """TIPO : DOUBLE"""
            
    p[0] = "DOUBLE" 


def p_cmds(p):
    """CMDS : CMD MAIS_CMDS
            | CMD_COND CMDS
            | DC
            | empty"""
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    elif p[1] is not None:
        p[0] = [p[1]]  
    else:
        p[0] = [] 



def p_mais_cmds(p):
    """MAIS_CMDS : SEMICOLON CMDS
                 """
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []


def p_cmd_cond(p):
    """CMD_COND : IF LPAR CONDICAO RPAR LCBRA CMDS RCBRA PFALSA
                | WHILE LPAR CONDICAO RPAR LCBRA CMDS RCBRA
    """
    if p[1] == 'if':
        # Gerar código para a condição
        condicao = p[3]  # Avaliar a condição
        codegen.emit(condicao)  # Gerar o código que avalia a condição
        posicao_falsa = codegen.retorno_posicao()  # Posição onde a execução irá pular se a condição for falsa
        codegen.emit(f"DSVF FIM_IF_{posicao_falsa}")  # Se a condição for falsa, salta para o fim do if

        # Gerar código para os comandos dentro do bloco 'if'
        p[0] = ("if", p[3], p[6], p[8])
        codegen.emit(p[6])  # Gera os comandos do bloco 'if'

        # Se houver um bloco 'else', tratar o desvio
        if p[8] is not None:
            posicao_fim_else = codegen.retorno_posicao() + 1  # Posição após o bloco 'if'
            codegen.emit(f"DSVS FIM_ELSE_{posicao_fim_else}")  # Pular o 'else' se o 'if' foi executado
             # Label do fim do bloco 'if'

            # Gerar o código para o bloco 'else'
            codegen.emit(p[8])  # Emitir o código do bloco 'else'
             # Label do fim do bloco 'else'

            

    elif p[1] == 'while':
        # Gerar código para o while
        inicio_while = codegen.retorno_posicao()
        

        # Avaliar a condição do while
        condicao = p[3]  # Avaliar a condição
        codegen.emit(condicao)  # Gerar o código que avalia a condição
        posicao_fim_while = codegen.retorno_posicao() + 1
        codegen.emit(f"DSVF FIM_WHILE_{posicao_fim_while}")  # Se a condição for falsa, sair do loop

        # Gerar o código para os comandos dentro do while
        p[0] = ("while", p[3], p[6])
        codegen.emit(p[6])  # Gera os comandos do bloco 'while'

        # Voltar para o início do while
        codegen.emit(f"DSVS INICIO_WHILE_{inicio_while}")
    

      
def p_cmd(p):
    """CMD : PRINT LPAR EXPRESSAO RPAR
           | ID RESTO_IDENT"""

    if p[2][0] == "ASSIGMENT":           
        p[0] = (p[1], p[2])
        codegen.incrementar_posicao()
    elif p[1] == 'System.out.println':
        p[0] = ("println", p[3])
        codegen.emit(f"IMPR, {p[3]}")  
        codegen.incrementar_posicao()
    else:
        p[0] = ("assign_or_call", p[1], p[2])
        

def p_pfalsa(p):
    """PFALSA : ELSE LCBRA CMDS RCBRA 
              | empty"""
    if len(p) == 5:
        p[0] = ("else", p[3])
        posicao_else = codegen.retorno_posicao()
        codegen.emit(f'DSVI {posicao_else}')
        codegen.incrementar_posicao()
    else:
        p[0] = None


def p_resto_ident(p):
    """RESTO_IDENT : ASSIGMENT EXP_IDENT
                   | LPAR LISTA_ARG RPAR"""
    if p[1] == '=':
        p[0] = ("ASSIGMENT", p[2])
        codegen.emit(f"ARMZ {p[-1]}")  
        codegen.incrementar_posicao()
    else:
        p[0] = ("call", p[2])
        codegen.incrementar_posicao()  
        codegen.emit(F"PSHR {str(codegen.retorno_posicao())}") 
        codegen.emit(f"CHPR {p[-1]}")  
        codegen.emit("PARA")
        codegen.incrementar_posicao() 

def p_condicao(p):
    """CONDICAO : EXPRESSAO RELACAO EXPRESSAO"""
    p[0] = (p[2], p[1], p[3]) 
    if p[2] == "<":
        codegen.emit(f"CPME")
        codegen.incrementar_posicao()
    elif p[2] == ">":
        codegen.emit(f"CPMA")
        codegen.incrementar_posicao()
    elif p[2] == "==":
        codegen.emit(f"CPIG")
        codegen.incrementar_posicao()
    elif p[2] == "!=":
        codegen.emit(f"CPES")
        codegen.incrementar_posicao()
    elif p[2] == ">=":
        codegen.emit(f"CPMI")
        codegen.incrementar_posicao()
    elif p[2] == "<=":
        codegen.emit(f"CPAI")
        codegen.incrementar_posicao()

def p_relacao(p):
    """RELACAO : IGUAL
               | DIF
               | MAI
               | MEN
               | MAI_IGUAL
               | MEN_IGUAL"""
    p[0] = p[1]  
    

    
def p_lista_arg(p):
    """LISTA_ARG : ARGUMENTOS
                 | empty"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = None
        
def p_argumentos(p):
    """ARGUMENTOS : ID MAIS_IDENT"""
    p[0] = ("ARGUMENTOS", p[1], p[2])
 
    
def p_mais_ident(p):
    """MAIS_IDENT : VIRGU ARGUMENTOS 
                  | empty"""
    p[0] = p[2] if len(p) > 1 else []


def p_exp_ident(p):
    """EXP_IDENT : EXPRESSAO
                 | LERDOUBLE LPAR RPAR"""
    if len(p) == 4:
        p[0] = ("lerDouble")
        codegen.emit("LEIT")
    else:
        p[0] = p[1]

        
def p_expressao(p):
    "EXPRESSAO : TERMO OUTROS_TERMOS"

    if p[2] is not None:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]
        
        

def p_termo(p):
    """TERMO : OP_UN FATOR MAIS_FATORES"""
    op_un = p[1]  
    fator = p[2]  
    mais_fatores = p[3]  
    if op_un is not None:
        fator = (op_un, fator)
        codegen.emit(f"INVE ", fator) 
        codegen.incrementar_posicao()
         
        
    if mais_fatores is None:
        p[0] = fator
    else:
        p[0] = (fator, mais_fatores)



def p_op_un(p):
    """OP_UN : MENOS
             | empty"""
    p[0] = p[1] if len(p) > 1 else None

comandos_emitidos = set()
def p_fator(p):
    """FATOR : ID
             | NUMBER
             | LPAR EXPRESSAO RPAR"""

    if len(p) == 2:
        p[0] = p[1]
        if p.slice[1].type == 'ID':  
            if (f"CRVL {p[1]}") not in comandos_emitidos:
                comandos_emitidos.add((f"CRVL {p[1]}"))
                codegen.incrementar_posicao()
                codegen.emit(f"CRVL {p[1]}") 
        elif p.slice[1].type == 'NUMBER':  
            if (f"CRCT {p[1]}") not in comandos_emitidos:
                codegen.incrementar_posicao()
                comandos_emitidos.add(f"CRCT {p[1]}")
                codegen.emit(f"CRCT {p[1]}")
    else:
        p[0] = p[2]



def p_outros_termos(p):
    """OUTROS_TERMOS : OP_AD TERMO OUTROS_TERMOS
                     | empty"""
    if len(p) > 2:
        operador = p[1] 
        termo = p[2]  
        outros_termos = p[3]  
        codegen.incrementar_posicao()
        if operador == "+":
            codegen.emit("SOMA")  
        elif operador == "-":
            codegen.emit("SUBT")  
        if outros_termos is None:
            p[0] = (termo, operador)
        else: 
            p[0] = (termo, operador, outros_termos)
    else:
        p[0] = None  
    

def p_op_ad(p):
    """OP_AD : SUM
             | MENOS"""
    p[0] = p[1]
        
        
def p_mais_fatores(p):
    """MAIS_FATORES : OP_MUL FATOR MAIS_FATORES
                    | empty"""
    if len(p) == 4:
        operador = p[1]  
        fator = p[2]  
        mais_fatores = p[3]  
        if operador == "/" and fator == "0.0":
            print('Erro semântico: não é possível dividir por 0')
        codegen.incrementar_posicao()
        if operador == "*":
            codegen.emit("MULT")  
   
        elif operador == "/":
            codegen.emit("DIVI")  
        if mais_fatores is None:
            p[0] = (fator, operador)
        else:
            p[0] = (fator, operador, mais_fatores)
    else:
        p[0] = None  


def p_op_mul(p):
    """OP_MUL : MUL
              | DIVI"""
    p[0] = p[1]          


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}', token: {p.type} na linha {p.lineno}")
        global erros
        erros += 1
    else:
        print("Arquivo sem erros")


parser = yacc.yacc()


def token_generator(tokens):
    for token in tokens:
        yield token
    yield None
    
class CodeGenerator:
    def __init__(self):
        self.instructions = ["INPP"]  
        self.label_count = 0
        self.posicao = 0
        self.inM = -1

    def emit(self, instruction):
        
        self.instructions.append(instruction)
        with open("output.j", 'w') as f:
            for instruction in self.instructions:  
                f.write(f"{instruction}\n") 

    def new_label(self):
        
        label = f"L{self.label_count}"
        self.label_count += 1
        return label

    def get_code(self):
    
        return "\n".join(self.instructions)

    def reset(self):
     
        self.instructions = []
        self.label_count = 0
        
    def incrementar_posicao(self):
        self.posicao += 1
        return self.posicao
    
    def retorno_posicao(self):
        return self.posicao
    
    def retorno_metodo(self):
        return self.inM

codegen = CodeGenerator()

if __name__ == "__main__":
    # try:
        with open("tokens.txt", "r") as f:
            tokens = []
            for line in f:
                parts = line.split()
                if len(parts) == 4:  
                    tok_type, tok_value, lineno, lexpos = parts[0], parts[1], int(parts[2]), int(parts[3])

                    
                    token = lex.LexToken()
                    token.type = tok_type
                    token.value = tok_value
                    token.lineno = lineno
                    token.lexpos = lexpos
                    tokens.append(token)

            parser.parse(tokenfunc=token_generator(tokens).__next__)
            # if erros == 0:
            #     printar()
    # except Exception as e:
    #     print(f"Ocorreu um erro: {e}")