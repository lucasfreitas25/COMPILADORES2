import ply.yacc as yacc
from lexico import myLexer

# Definição de tokens e palavras reservadas
reservada = {
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
    ('left', 'IGUAL', 'DIF', 'MEN', 'MAI', 'MEN_IGUAL', 'MAI_IGUAL')
)


# Definição da gramática adaptada
def p_prog(p):
    'PROG : PUBLIC CLASS ID LCBRA PUBLIC STATIC VOID MAIN LPAR STRING LSBRA RSBRA ID RPAR LCBRA CMDS RCBRA METODO RCBRA'
    p[0] = {"op": "PROG", "main": p[15], "cmds": p[18]}

def p_metodo(p):
    """METODO : PUBLIC STATIC TIPO ID LPAR PARAMS RPAR LCBRA CMDS RETURN EXPRESSAO SEMICOLON RCBRA
              | empty"""
    if len(p) == 14:
        p[0] = {"op": "metodo", "tipo": p[3], "nome": p[4], "params": p[6], "cmds": p[9], "retorno": p[10]}
    else:
        p[0] = None

def p_params(p):
    """PARAMS : TIPO ID MAIS_PARAMS
              | empty"""
    if len(p) == 4:
        p[0] = {"tipo": p[1], "id": p[2], "mais_params": p[3]}
    else:
        p[0] = None

def p_mais_params(p):
    """MAIS_PARAMS : VIRGU PARAMS
                   | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

def p_cmds(p):
    """CMDS : CMD MAIS_CMDS
            | CMD_COND CMDS
            | DC
            | empty"""
    if len(p) == 3:
        p[0] = {"op": "cmds", "cmd": p[1], "mais_cmds": p[2]}
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = []

def p_mais_cmds(p):
    """MAIS_CMDS : SEMICOLON CMDS"""
    p[0] = p[2]

def p_cmd_cond(p):
    """CMD_COND : IF LPAR CONDICAO RPAR LCBRA CMDS RCBRA PFALSA
           | WHILE LPAR CONDICAO RPAR LCBRA CMDS RCBRA"""
    if p[1] == 'if':
        p[0] = {"op": "if", "condicao": p[3], "then": p[6], "else": p[8]}
    elif p[1] == 'while':
        p[0] = {"op": "while", "condicao": p[3], "body": p[6]}

def p_cmd(p):
    """CMD : PRINT LPAR EXPRESSAO RPAR
           | ID RESTO_IDENT"""
    if p[1] == 'System.out.println':
        p[0] = {"op": "print", "expr": p[3]}
    else:
        p[0] = {"op": "assign_or_call", "id": p[1], "resto": p[2]}

def p_pfalsa(p):
    """PFALSA : ELSE LCBRA CMDS RCBRA 
              | empty"""
    if len(p) == 5:
        p[0] = {"op": "else", "cmds": p[3]}
    else:
        p[0] = None

def p_condicao(p):
    """CONDICAO : EXPRESSAO IGUAL EXPRESSAO
                | EXPRESSAO MEN EXPRESSAO
                | EXPRESSAO MEN_IGUAL EXPRESSAO
                | EXPRESSAO MAI EXPRESSAO
                | EXPRESSAO MAI_IGUAL EXPRESSAO
                | EXPRESSAO DIF EXPRESSAO"""
    p[0] = {"op": p[2], "left": p[1], "right": p[3]}

def p_expressao(p):
    "EXPRESSAO : TERMO OUTROS_TERMOS"
    p[0] = {"op": "expr", "termo": p[1], "outros_termos": p[2]}

def p_termo(p):
    """TERMO : OP_UN FATOR MAIS_FATORES"""
    p[0] = {"op": p[1] or "", "fator": p[2], "mais_fatores": p[3]}

def p_fator(p):
    """FATOR : ID
             | NUMBER
             | LPAR EXPRESSAO RPAR"""
    if len(p) == 2:
        p[0] = {"op": "var", "value": p[1]} if isinstance(p[1], str) else {"op": "number", "value": p[1]}
    else:
        p[0] = p[2]

def p_error(p):
    print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}, tipo de token: {p.type}")

def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc()

# Função principal
if __name__ == "__main__":
    try:
        with open("tokens.txt", "r") as f:
            data = f.read()            
            parser.parse(data)
            print("Análise concluída sem erros.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
