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
    'NEG', # !
    'SEMICOLON', # ;
    'LSBRA', # [
    'RSBRA' # ] 
] 
procedencia = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    'Program : MainClass ClassDeclarationList'
    pass

def p_class_declaration_list(p):
    '''ClassDeclarationList : ClassDeclaration ClassDeclarationList
                            | empty'''
    pass

def p_main_class_palavras_chaves(p):
    'MainClass : CLASS ID LBRACE PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ID RPAREN LBRACE Statement RBRACE RBRACE'
    pass

def p_class_declaration(p):
    '''ClassDeclaration : CLASS ID LBRACE VarDeclarationList MethodDeclarationList RBRACE
                        | CLASS ID EXTENDS ID LBRACE VarDeclarationList MethodDeclarationList RBRACE'''
    pass

def p_var_declaration_list(p):
    '''VarDeclarationList : VarDeclaration VarDeclarationList
                          | empty'''
    pass

def p_var_declaration(p):
    'VarDeclaration : Type ID SEMI'
    pass

def p_method_declaration_list(p):
    '''MethodDeclarationList : MethodDeclaration MethodDeclarationList
                             | empty'''
    pass

def p_method_declaration(p):
    'MethodDeclaration : PUBLIC Type ID LPAREN ParameterList RPAREN LBRACE VarDeclarationList StatementList RETURN Expression SEMI RBRACE'
    pass

def p_type(p):
    '''Type : INT LBRACKET RBRACKET
            | BOOLEAN
            | INT
            | ID'''
    pass

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
    '''ParameterList : Type ID ParameterListRest
                     | empty'''
    pass

def p_parameter_list_rest(p):
    '''ParameterListRest : VIRGU Type ID ParameterListRest
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