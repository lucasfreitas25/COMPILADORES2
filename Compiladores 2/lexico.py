import ply.lex as lex
import re

class myLexer(object):
    reservada = {
        'int' : 'INT',
        'def':  'DEF',
        'return': 'RETURN',
        'while': 'WHILE',
        'boolean': 'BOOLEAN',
        'class': 'CLASS',
        'extends': 'EXTENDS',
        'public': 'PUBLIC',
        'static': 'STATIC',
        'void': 'VOID',
        'main': 'MAIN',
        'String' : 'STRING',
        'System.out.println': 'PRINT',
        'if': 'IF',
        'else': 'ELSE',
        'length': 'length',
        'true': 'TRUE',
        'false': 'FALSE',
        'this': 'THIS',
        'new': 'NEW',
        'null': 'NULL',
        'double': 'DOUBLE',
        'lerDouble': 'LERDOUBLE'

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
        'MAI_IGUAL', # >=
        'MEN_IGUAL', # <=
        'MAI', # >
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
    t_MAI_IGUAL = r'>='
    t_MEN_IGUAL = r'<='
    t_MAI = r'>'
    t_NEG = r'\!'
    t_SEMICOLON = r'\;'
    t_LSBRA = r'\['
    t_RSBRA = r'\]'
    
    
    
    def t_PRINT(self, t):
        r'System\.out\.println'
        return t
    #IDENTIFICA AS PALAVRAS RESERVADAS
    def t_ID(self, t):
        r'[a-z_A-Z]+[0-9a-zA-Z]*'
        t.type = self.reservada.get(t.value, 'ID')
        return t

    #IDENTIFICA OS NUMEROS
    def t_NUMBER(self, t):
        r'\d+(\.\d+)?'
        t.value = float(t.value)
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
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            # Gravar apenas o tipo do token, o valor, a linha e a posição separados por espaços
            tokens.append(f'{tok.type} {tok.value} {tok.lineno} {tok.lexpos}')
        
        with open('tokens.txt', 'w') as f:
            f.write("\n".join(tokens))
            
m = myLexer()
m.build()
m.test(
    """
    public class Teste {
        public static void main(String[] args) {
            somar();
        }
        public static double somar(){
            double cont;
            double a,b,c;
            cont = 10;
            while(cont > 0) {
                a = lerDouble();
                b = lerDouble();
                if (a > b) {
                    c = a - b;
                } else {
                    c = b + a;
                }
                System.out.println(c);
                cont = cont - 1;
                
            }
            return c;
        }
    }"""
)


