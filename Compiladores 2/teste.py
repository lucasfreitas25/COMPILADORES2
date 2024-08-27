import ply.yacc as yacc

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

# Definindo precedência dos operadores
precedence = (
    ('left', 'OP_AD'),
    ('left', 'OP_MUL'),
    ('left', 'OP_REL'),
)

# Definindo a gramática

def p_prog(p):
    "PROG : PUBLIC CLASS ID LBRACE PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ID RPAREN LBRACE CMDS RBRACE METODO RBRACE"
    p[0] = ("PROG", p[13], p[15], p[18])

def p_metodo(p):
    """METODO : PUBLIC STATIC TIPO ID LPAREN PARAMS RPAREN LBRACE DC CMDS RETURN EXPRESSAO SEMICOLON RBRACE
              | empty"""
    if len(p) == 14:
        p[0] = ("METODO", p[3], p[4], p[6], p[9], p[10], p[12])
    else:
        p[0] = None

def p_tipo(p):
    "TIPO : DOUBLE"
    p[0] = "double"

def p_params(p):
    """PARAMS : TIPO ID MAIS_PARAMS
              | empty"""
    if len(p) == 4:
        p[0] = ("PARAMS", p[1], p[2], p[3])
    else:
        p[0] = None

def p_mais_params(p):
    """MAIS_PARAMS : COMMA PARAMS
                   | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

def p_dc(p):
    """DC : VAR MAIS_DC
          | empty"""
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = None

def p_mais_dc(p):
    """MAIS_DC : SEMICOLON DC
               | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

def p_var(p):
    "VAR : TIPO VARS SEMICOLON"
    p[0] = (p[1], p[2])

def p_vars(p):
    "VARS : ID MAIS_VAR"
    p[0] = [p[1]] + (p[2] if p[2] else [])

def p_mais_var(p):
    """MAIS_VAR : COMMA VARS
                | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []

def p_cmds(p):
    """CMDS : CMD MAIS_CMDS
            | empty"""
    if len(p) == 3:
        p[0] = [p[1]] + (p[2] if p[2] else [])
    else:
        p[0] = []

def p_mais_cmds(p):
    """MAIS_CMDS : SEMICOLON CMDS
                 | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []

def p_cmd(p):
    """CMD : IF LPAREN CONDICAO RPAREN LBRACE CMDS RBRACE PFALSA
           | WHILE LPAREN CONDICAO RPAREN LBRACE CMDS RBRACE
           | PRINTLN LPAREN EXPRESSAO RPAREN
           | ID RESTO_IDENT"""
    if p[1] == 'if':
        p[0] = ("if", p[3], p[6], p[8])
    elif p[1] == 'while':
        p[0] = ("while", p[3], p[6])
    elif p[1] == 'System.out.println':
        p[0] = ("println", p[3])
    else:
        p[0] = ("assign_or_call", p[1], p[2])

def p_pfalsa(p):
    """PFALSA : ELSE LBRACE CMDS RBRACE
              | empty"""
    if len(p) == 5:
        p[0] = ("else", p[3])
    else:
        p[0] = None

def p_resto_ident(p):
    """RESTO_IDENT : ASSIGN EXP_IDENT
                   | LPAREN LISTA_ARG RPAREN"""
    if p[1] == '=':
        p[0] = ("assign", p[2])
    else:
        p[0] = ("call", p[2])

def p_lista_arg(p):
    """LISTA_ARG : ARGUMENTOS
                 | empty"""
    p[0] = p[1] if len(p) > 1 else []

def p_argumentos(p):
    """ARGUMENTOS : ID MAIS_IDENT"""
    p[0] = [p[1]] + (p[2] if p[2] else [])

def p_mais_ident(p):
    """MAIS_IDENT : COMMA ARGUMENTOS
                  | empty"""
    p[0] = p[2] if len(p) > 1 else []

def p_exp_ident(p):
    """EXP_IDENT : EXPRESSAO
                 | LERDOUBLE"""
    p[0] = p[1]

def p_condicao(p):
    "CONDICAO : EXPRESSAO OP_REL EXPRESSAO"
    p[0] = ("condition", p[1], p[2], p[3])

def p_expressao(p):
    "EXPRESSAO : TERMO OUTROS_TERMOS"
    p[0] = (p[1], p[2])

def p_termo(p):
    "TERMO : OP_UN FATOR MAIS_FATORES"
    p[0] = (p[1], p[2], p[3])

def p_op_un(p):
    """OP_UN : '-'
             | empty"""
    p[0] = p[1] if len(p) > 1 else None

def p_fator(p):
    """FATOR : ID
             | NUMERO_REAL
             | LPAREN EXPRESSAO RPAREN"""
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
    """OP_AD : '+'
             | '-'"""
    p[0] = p[1]

def p_mais_fatores(p):
    """MAIS_FATORES : OP_MUL FATOR MAIS_FATORES
                    | empty"""
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = None

def p_op_mul(p):
    """OP_MUL : '*'
              | '/'"""
    p[0] = p[1]

def p_empty(p):
    "empty :"
    p[0] = None

# Tratamento de erros
def p_error(p):
    print(f"Erro de sintaxe em {p.value}")

# Construa o parser
parser = yacc.yacc()

if __name__ == "__main__":
    try:
        with open("tokens.txt", "r") as f:
            data = f.read()
            parser.parse(data)
            print("Análise concluída sem erros.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
