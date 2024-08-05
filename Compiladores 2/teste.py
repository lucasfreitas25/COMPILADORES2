import ply.lex as lex
import ply.yacc as yacc
import keyboard as key
import re
import ply.lex as lex

tokens = (
    'CLASS',
    'PUBLIC',
    'STATIC',
    'VOID',
    'MAIN',
    'STRING',
    'INT',
    'BOOLEAN',
    'IF',
    'ELSE',
    'WHILE',
    'PRINT',
    'RETURN',
    'EXTENDS',
    'TRUE',
    'FALSE',
    'THIS',
    'NEW',
    'IDENTIFIER',
    'INTEGER_LITERAL',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'SEMI',
    'COMMA',
    'DOT',
    'ASSIGN',
    'AND',
    'LT',
    'PLUS',
    'MINUS',
    'TIMES',
    'NOT'
)

reserved = {
    'class': 'CLASS', 
    'public': 'PUBLIC', 
    'static': 'STATIC',
    'void': 'VOID', 
    'main': 'MAIN', 
    'String': 'STRING', 
    'int': 'INT',
    'boolean': 'BOOLEAN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'System.out.println': 'PRINT',
    'return': 'RETURN',
    'extends': 'EXTENDS',
    'true': 'TRUE',
    'false': 'FALSE',
    'this': 'THIS',
    'new': 'NEW'
}

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMI = r';'
t_COMMA = r','
t_DOT = r'\.'
t_ASSIGN = r'='
t_AND = r'&&'
t_LT = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_NOT = r'!'

t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_INTEGER_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_program(p):
    'Program : MainClass ClassDeclarationList'
    pass

def p_class_declaration_list(p):
    '''ClassDeclarationList : ClassDeclaration ClassDeclarationList
                            | empty'''
    pass

def p_main_class(p):
    'MainClass : CLASS IDENTIFIER LBRACE PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET IDENTIFIER RPAREN LBRACE Statement RBRACE RBRACE'
    pass

def p_class_declaration(p):
    '''ClassDeclaration : CLASS IDENTIFIER LBRACE VarDeclarationList MethodDeclarationList RBRACE
                        | CLASS IDENTIFIER EXTENDS IDENTIFIER LBRACE VarDeclarationList MethodDeclarationList RBRACE'''
    pass

def p_var_declaration_list(p):
    '''VarDeclarationList : VarDeclaration VarDeclarationList
                          | empty'''
    pass

def p_var_declaration(p):
    'VarDeclaration : Type IDENTIFIER SEMI'
    pass

def p_method_declaration_list(p):
    '''MethodDeclarationList : MethodDeclaration MethodDeclarationList
                             | empty'''
    pass

def p_method_declaration(p):
    'MethodDeclaration : PUBLIC Type IDENTIFIER LPAREN ParameterList RPAREN LBRACE VarDeclarationList StatementList RETURN Expression SEMI RBRACE'
    pass

def p_type(p):
    '''Type : INT LBRACKET RBRACKET
            | BOOLEAN
            | INT
            | IDENTIFIER'''
    pass

def p_statement_list(p):
    '''StatementList : Statement StatementList
                     | empty'''
    pass

def p_statement(p):
    '''Statement : LBRACE StatementList RBRACE
                 | IF LPAREN Expression RPAREN Statement ELSE Statement
                 | WHILE LPAREN Expression RPAREN Statement
                 | PRINT LPAREN Expression RPAREN SEMI
                 | IDENTIFIER ASSIGN Expression SEMI
                 | IDENTIFIER LBRACKET Expression RBRACKET ASSIGN Expression SEMI'''
    pass

def p_expression(p):
    '''Expression : Expression AND Expression
                  | Expression LT Expression
                  | Expression PLUS Expression
                  | Expression MINUS Expression
                  | Expression TIMES Expression
                  | Expression LBRACKET Expression RBRACKET
                  | Expression DOT IDENTIFIER LPAREN ExpressionList RPAREN
                  | INTEGER_LITERAL
                  | TRUE
                  | FALSE
                  | IDENTIFIER
                  | THIS
                  | NEW INT LBRACKET Expression RBRACKET
                  | NEW IDENTIFIER LPAREN RPAREN
                  | NOT Expression
                  | LPAREN Expression RPAREN'''
    pass

def p_parameter_list(p):
    '''ParameterList : Type IDENTIFIER ParameterListRest
                     | empty'''
    pass

def p_parameter_list_rest(p):
    '''ParameterListRest : COMMA Type IDENTIFIER ParameterListRest
                         | empty'''
    pass

def p_expression_list(p):
    '''ExpressionList : Expression ExpressionListRest
                      | empty'''
    pass

def p_expression_list_rest(p):
    '''ExpressionListRest : COMMA Expression ExpressionListRest
                          | empty'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
data = '''
class Main {
    public static void main(String[] args) {
        System.out.println(1);
    }
}
'''

lexer.input(data)
for token in lexer:
    print(token)

parser.parse(data)
