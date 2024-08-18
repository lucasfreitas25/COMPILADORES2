import ply.yacc as yacc
import keyboard as key
import re
from lexico import myLexer, tokens

tokens = [
    'ID',
    'COLON', # :
    'LPAR', # (
    'RPAR', # )
    'MENOS', # -
    'SUM', # +
    'MUL', # *
    'DIVI', # /
    'POINT', # .
    'VIRGU', # ,
    'NUMBER',
    'ASSIGMENT', # =
    'LCBRA', # {
    'RCBRA', # }
    'DIF', # !=
    'IGUAL', # ==
    'AND', # &&
    'MEN', # <
    'MAI_IGUAL', # >=
    'MEN_IGUAL', # <=
    'MAI', # >
    'NEG', # !
    'SEMICOLON', # ;
    'LSBRA', # [
    'RSBRA' # ] 
    ] 

procedencia = (
    ('left', 'SUM', 'MENOS'),
    ('left', 'MUL', 'DIVI'),
)

def p_program(p):
    'Program : MainClass ClassDeclarationList'
    pass

def p_class_declaration_list(p):
    '''ClassDeclarationList : ClassDeclaration ClassDeclarationList
                            | empty'''
    pass

#Definição da MAIN
def p_prog(p):
    'PROG : PUBLIC CLASS ID LBRACE PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ID RPAREN LBRACE CMDS RBRACE METODO RBRACE'
    pass

#Definição quando ha extends
def p_class_declaration(p):
    '''ClassDeclaration : CLASS ID LBRACE VarDeclarationList MethodDeclarationList RBRACE
                        | CLASS ID EXTENDS ID LBRACE VarDeclarationList MethodDeclarationList RBRACE'''
    pass

def p_method_declaration_list(p):
    '''MethodDeclarationList : MethodDeclaration MethodDeclarationList
                             | empty'''
    pass

#Definição do metodos
def p_metodo(p):
    '''METODO : PUBLIC STATIC TIPO ID LPAREN PARAMS RPAREN LBRACE DC CMDS RETURN EXPRESSAO SEMI RBRACE
              | empty'''
    pass

#Defini as regras dos parametros do metodos
def p_params(p):
    '''PARAMS : TIPO ID MAIS_PARAMS
              | empty'''
    pass

#Virgula apos o outro parametro
def p_mais_params(p):
    '''MAIS_PARAMS : VIRGU PARAMS
                   | empty'''
    pass

#Mais de uma declaração
def p_dc(p):
    '''DC : VAR MAIS_DC
          | empty'''
    pass

#ponto e virgula entre parametros
def p_mais_dc(p):
    '''MAIS_DC : SEMI DC
               | empty'''
    pass

#Defini as regras de declaração de variavel
def p_var_declaration_list(p):
    '''VarDeclarationList : VarDeclaration VarDeclarationList
                          | empty'''
    pass
    
def p_var(p):
    'VAR : TIPO VARS SEMI'
    pass

def p_vars(p):
    'VARS :  ID MAIS_VAR '
    pass

#VIRGULA APOS MAIS VARIAVEIS
def p_mais_var(p):
    '''MAIS_VAR : VIRGU VARS
                | empty'''
    pass
#TIPOS ACEITOS
def p_tipo(p):
    '''TIPO : INT LBRACKET RBRACKET
            | BOOLEAN
            | INT
            | ID
            | DOUBLE
            '''
    pass

def p_cmds(p):
    '''CMDS : CMD MAIS_CMDS
            | empty'''
    pass

def p_mais_cmds(p):
    '''MAIS_CMDS : SEMI CMDS
                 | empty'''
    pass
def p_statement_condicionais(p):
    '''
    statement : 
    '''

def operacoes(p):
    '''expressão: PLUS expression                 
           | expression MINUS expression                
           | expression TIMES expression                
           | expression DIVIDE expression               
           | LPAREN expression RPAREN                   
           | NUMBER  
                  '''
                  
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] /p[3]
        
def p_operacoes_logicas_booleanas(t):
    '''expression : expression MAIOR expression
                  | expression MENOR expression
                  | expression EQUALS expression
                  | expression DIFF expression
                  | expression AND expression
                  '''
    if t[2] == '>'  : t[0] = t[1] > t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    elif t[2] == '==': t[0] = t[1] == t[3]
    elif t[2] == '!=': t[0] = t[1] != t[3]
    elif t[2] == '&&': t[0] = t[1] and t[3]
        
        
def p_parameter_list(p):
    '''ParameterList : TIPO ID ParameterListRest
                     | empty'''
    pass

def p_parameter_list_rest(p):
    '''ParameterListRest : VIRGU TIPO ID ParameterListRest
                         | empty'''
    pass

def p_expression_list(p):
    '''ExpressionList : Expression ExpressionListRest
                      | empty'''
    pass

def p_expression_list_rest(p):
    '''ExpressionListRest : VIRGU Expression ExpressionListRest
                          | empty'''
    pass

def p_vazio(p):
    'optitem : item'
    '        | vazio'
    ...
            
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}'")
    else:
        print("Erro de sintaxe em EOF")
        
parser = yacc.yacc()    

if __name__ == "__main__":
    with open("tokens.txt", "r") as f:
        data = f.read()
        parser.parse(data)