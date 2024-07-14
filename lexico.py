import ply.lex as lex
import re

class myLexer(object):
    reservada = {
        'int' : 'int',
        'def':  'def',
        'return': 'return',
        'while': 'while',
        'boolean': 'boolean',
        'class': 'class',
        'extends': 'extends',
        'public': 'public',
        'static': 'static',
        'void': 'void',
        'main': 'main',
        'String' : 'String',
        'System.out.println': 'PRINTLN',
        'if': 'if',
        'else': 'else',
        'length': 'length',
        'true': 'true',
        'false': 'false',
        'this': 'this',
        'new': 'new',
        'null': 'null',

    }

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
    ] + list(reservada.values())

    t_COLON = r'\:'
    t_LPAR = r'\('
    t_RPAR = r'\)'
    t_MENOS = r'\-'
    t_SUM = r'\+'
    t_MUL = r'\*'
    t_DIVI = r'/'
    t_POINT = r'\.'
    t_VIRGU = r'\,'
    t_ASSIGMENT = r'\='
    t_LCBRA = r'\{'
    t_RCBRA = r'\}'
    t_DIF = r'\!\='
    t_IGUAL = r'\=\='
    t_AND = r'\&\&'
    t_MEN = r'\<'
    t_NEG = r'\!'
    t_SEMICOLON = r'\;'
    t_LSBRA = r'\['
    t_RSBRA = r'\]'

    #IDENTIFICA AS PALAVRAS RESERVADAS
    def t_ID(self, t):
        r'[a-z_A-Z]+[0-9a-zA-Z]*'
        t.type = self.reservada.get(t.value.lower(), 'ID')
        return t

    #IDENTIFICA OS NUMEROS
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t
    #IDENTIFICA NOVAS LINHAS
    def t_novalinha(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        
    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1
    
    #IGNORA AS ESPAÇOS EM BRANCOS E COMENTARIOS
    t_ignore  = ' \t'
    t_ignore_COMMENT = r'\#.*'
    
    #IDENTIFICA OS ERROS
    def t_error(self, t):
        print("ERRO LEXICO '%s'" % t.value[0])
        t.lexer.skip(1)
        
    #MONTA O LEX    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    def test(self, data):
        self.lexer.input(data)
        with open('tokens.txt', 'w') as f:
            while True:
                tok = self.lexer.token()
                if not tok:
                    break
                print(tok)
                f.write(f"{tok}\n")
            
m = myLexer()
m.build()
m.test(
    '''
    class Factorial {
        public static void main ( String [] a ){
            System.out.println (new Fac (). ComputeFac (10));
        }
    }
    #Teste
    class Fac {
        public int ComputeFac (int num ){
            int num_aux ;
            if ( num < 1) 
                num_aux = 1;
            else
                num_aux = num * ( this . ComputeFac ( num -1));
        return num_aux ;
        }
    }
    '''
)
