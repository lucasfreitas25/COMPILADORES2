import ply.yacc as yacc
from lexico import myLexer

# Definição de tokens e palavras reservadas
reservada = {
    'int': 'INT',
    'def': 'DEF',
    'return': 'RETURN',
    'while': 'WHILE',
    'boolean': 'BOOLEAN',
    'class': 'CLASS',
    'extends': 'EXTENDS',
    'public': 'PUBLIC',
    'static': 'STATIC',
    'void': 'VOID',
    'main': 'MAIN',
    'String': 'STRING',
    'System.out.println': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'length': 'LENGTH',
    'true': 'TRUE',
    'false': 'FALSE',
    'this': 'THIS',
    'new': 'NEW',
    'null': 'NULL',
    'double': 'DOUBLE'
}

tokens = [
    'ID', 'COLON', 'LPAR', 'RPAR', 'MENOS', 'SUM', 'MUL', 'DIVI', 
    'POINT', 'VIRGU', 'NUMBER', 'ASSIGMENT', 'LCBRA', 'RCBRA', 
    'DIF', 'IGUAL', 'AND', 'MEN', 'MAI_IGUAL', 'MEN_IGUAL', 'MAI', 
    'NEG', 'SEMICOLON', 'LSBRA', 'RSBRA'
] + list(reservada.values())

# Definição de precedência
precedencia = (
    ('left', 'SUM', 'MENOS'),
    ('left', 'MUL', 'DIVI'),
)

# Definição da gramática
def p_prog(p):
    'PROG : PUBLIC CLASS ID LCBRA PUBLIC STATIC VOID MAIN LPAR STRING LSBRA RSBRA ID RPAR LCBRA CMDS RCBRA METODO RCBRA'
    pass

def p_metodo(p):
    """METODO : PUBLIC STATIC TIPO ID LPAR PARAMS RPAR LCBRA DC CMDS RETURN EXPRESSAO SEMICOLON RCBRA
              | empty"""
    pass

def p_params(p):
    """PARAMS : TIPO ID MAIS_PARAMS
              | empty"""
    pass

def p_mais_params(p):
    """MAIS_PARAMS : VIRGU PARAMS
                   | empty"""
    pass

def p_dc(p):
    """DC : VAR MAIS_DC
          | empty"""
    pass

def p_mais_dc(p):
    """MAIS_DC : SEMICOLON DC
               | empty"""
    pass

def p_var(p):
    'VAR : TIPO VARS SEMICOLON'
    pass

def p_vars(p):
    'VARS : ID MAIS_VAR'
    pass

def p_mais_var(p):
    """MAIS_VAR : VIRGU VARS
                | empty"""
    pass

def p_tipo(p):
    """TIPO : DOUBLE"""
    pass

def p_cmds(p):
    """CMDS : CMD MAIS_CMDS
            | empty"""
    pass

def p_mais_cmds(p):
    """MAIS_CMDS : SEMICOLON CMDS
                 | empty"""
    pass

def p_cmd(p):
    """CMD : IF LPAR CONDICAO RPAR LCBRA CMDS RCBRA PFALSA
           | WHILE LPAR CONDICAO RPAR LCBRA CMDS RCBRA
           | PRINT LPAR EXPRESSAO RPAR
           | ID RESTO_IDENT"""
    pass

def p_pfalsa(p):
    """PFALSA : ELSE LCBRA CMDS RCBRA 
              | empty"""
    pass

def p_resto_ident(p):
    """RESTO_IDENT : IGUAL EXP_IDENT
                   | LPAR LISTA_ARG RPAR"""
    pass

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
    pass

def p_argumentos(p):
    """ARGUMENTOS : ID MAIS_IDENT 
                  | empty"""
    pass

def p_mais_ident(p):
    """MAIS_IDENT : VIRGU ARGUMENTOS 
                  | empty"""
    pass

def p_exp_ident(p):
    """EXP_IDENT : EXPRESSAO
                 | TERMO"""
    p[0] = p[1]

# def p_condicao(p):
#     """CONDICAO : EXPRESSAO RELACAO EXPRESSAO"""
#     pass

def p_expressao(p):
    "EXPRESSAO : TERMO OUTROS_TERMOS"
    pass

def p_termo(p):
    """TERMO : OP_UN FATOR MAIS_FATORES"""
    pass

def p_op_un(p):
    """OP_UN : MENOS
             | empty"""
    pass

def p_fator(p):
    """FATOR : ID
             | DOUBLE
             | LPAR EXPRESSAO RPAR"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_outros_termos(p):
    """OUTROS_TERMOS : OP_AD TERMO OUTROS_TERMOS
                     | empty"""
    pass

def p_op_ad(p):
    """OP_AD : SUM
             | MENOS"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
        
        
def p_mais_fatores(p):
    """MAIS_FATORES : OP_MUL FATOR MAIS_FATORES
                    | empty"""
    pass

def p_op_mul(p):
    """OP_MUL : MUL
              | DIVI"""
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_empty(p):
    """empty :"""
    pass


def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo (EOF)")


parser = yacc.yacc()

if __name__ == "__main__":
    try:
        with open("tokens.txt", "r") as f:
            data = f.read()
            parser.parse(data)
            print("Análise concluída sem erros.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
