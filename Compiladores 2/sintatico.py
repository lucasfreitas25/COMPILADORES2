import ply.yacc as yacc
import ply.lex as lex
from lexico import myLexer

# Definição de tokens e palavras reservadas
tokens = myLexer.tokens

# Definição de precedência
precedencia = (
    ('left', 'SUM', 'MENOS'),
    ('left', 'MUL', 'DIVI'),
)
lista_vars = []
nova_lista = []
metodos = {}

# Definição da gramática
def p_prog(p):
    'PROG : PUBLIC CLASS ID LCBRA PUBLIC STATIC VOID MAIN LPAR STRING LSBRA RSBRA ID RPAR LCBRA CMDS RCBRA METODO RCBRA'
    p[0] = ("PROG", p[13], p[15], p[18])

def p_metodo(p):
    """METODO : PUBLIC STATIC TIPO ID LPAR PARAMS RPAR LCBRA CMDS RETURN EXPRESSAO SEMICOLON RCBRA
              | empty"""
    if len(p) == 14:
        global metodos
        metodos[p[4]] = p[3]
        p[0] = ("METODO", p[3], p[4], p[6], p[9], p[10], p[12])
    else:
        p[0] = None


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

    lista_vars.append(p[2])

    global nova_lista
    nova_lista = [item for sublista in lista_vars for item in sublista]
    nova_lista = [str(item) for item in nova_lista]
    

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
        
def p_tipo(p):
    """TIPO : DOUBLE"""
            
    p[0] = "DOUBLE" 


def p_cmds(p):
    """CMDS : CMD MAIS_CMDS
            | CMD_COND CMDS
            | DC
            | empty"""
    if len(p) == 3:
        p[0] = [p[1]] + (p[2] if p[2] else [])
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
        p[0] = ("if", p[3], p[6], p[8])
    elif p[1] == 'while':
        p[0] = ("while", p[3], p[6])
    else:
        p[0] = ("assign_or_call", p[1], p[2])
        
def p_cmd(p):
    """CMD : PRINT LPAR EXPRESSAO RPAR
           | ID RESTO_IDENT"""
    var = p[1]
    if p[1] == 'System.out.println':
        p[0] = ("println", p[3])
    elif p[1] in metodos:
        p[0] = ("method_call", p[1], p[2])
    elif var not in nova_lista:
        print(f"Erro semântico: {var} não declarada")
    else:
        p[0] = ("assign_or_call", p[1], p[2])
    

def p_pfalsa(p):
    """PFALSA : ELSE LCBRA CMDS RCBRA 
              | empty"""
    if len(p) == 5:
        p[0] = ("else", p[3])
    else:
        p[0] = None

def p_resto_ident(p):
    """RESTO_IDENT : ASSIGMENT EXP_IDENT
                   | LPAR LISTA_ARG RPAR"""
    if p[1] == '=':
        p[0] = ("ASSIGMENT", p[2])
    else:
        p[0] = ("call", p[2])

def p_condicao(p):
    """CONDICAO : EXPRESSAO IGUAL EXPRESSAO
                | EXPRESSAO MEN EXPRESSAO
                | EXPRESSAO MEN_IGUAL EXPRESSAO
                | EXPRESSAO MAI EXPRESSAO
                | EXPRESSAO MAI_IGUAL EXPRESSAO
                | EXPRESSAO DIF EXPRESSAO
                | NEG EXPRESSAO"""
    if len(p) == 5:  
        if p[2] == '==':
            p[0] = p[1] == p[3]
        elif p[2] == '<':
            p[0] = p[1] < p[3]
        elif p[2] == '<=':
            p[0] = p[1] <= p[3]
        elif p[2] == '>':
            p[0] = p[1] > p[3]
        elif p[2] == '>=':
            p[0] = p[1] >= p[3]
        elif p[2] == '!=':
            p[0] = p[1] != p[3]
    elif len(p) == 3: 
        p[0] = not p[2]
    
    
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
        p[0] = ("lerDouble",)
    else:
        p[0] = p[1]

def p_expressao(p):
    "EXPRESSAO : TERMO OUTROS_TERMOS"
    p[0] = (p[1], p[2])

def p_termo(p):
    """TERMO : OP_UN FATOR MAIS_FATORES"""
    p[0] = (p[1], p[2], p[3])
    

def p_op_un(p):
    """OP_UN : MENOS
             | empty"""
    p[0] = p[1] if len(p) > 1 else None

def p_fator(p):
    """FATOR : ID
             | NUMBER
             | LPAR EXPRESSAO RPAR"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_outros_termos(p):
    """OUTROS_TERMOS : OP_AD TERMO OUTROS_TERMOS
                     | empty"""
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
        
    else:
        p[0] = None


def p_op_ad(p):
    """OP_AD : SUM
             | MENOS"""
    if len(p) == 3:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        
        
def p_mais_fatores(p):
    """MAIS_FATORES : OP_MUL FATOR MAIS_FATORES
                    | empty"""
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = None

def p_op_mul(p):
    """OP_MUL : MUL
              | DIVI"""
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            print("Erro semântico: divisão por zero!")
            p[0] = None
        else:
            p[0] = p[1] / p[3]

def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}', token: {p.type} na linha {p.lineno}")
    else:
        print("Arquivo sem erros")



parser = yacc.yacc()

def token_generator(tokens):
    for token in tokens:
        yield token
    yield None

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
            
            
    # except Exception as e:
    #      print(f"Ocorreu um erro: {e}")