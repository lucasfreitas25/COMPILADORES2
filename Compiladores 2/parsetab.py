
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGMENT BOOLEAN CLASS COLON DEF DIF DIVI DOUBLE ELSE EXTENDS FALSE ID IF IGUAL INT LCBRA LENGTH LPAR LSBRA MAI MAIN MAI_IGUAL MEN MENOS MEN_IGUAL MUL NEG NEW NULL NUMBER POINT PRINT PUBLIC RCBRA RETURN RPAR RSBRA SEMICOLON STATIC STRING SUM THIS TRUE VIRGU VOID WHILEPROG : PUBLIC CLASS ID LCBRA PUBLIC STATIC VOID MAIN LPAR STRING LSBRA RSBRA ID RPAR LCBRA CMDS RCBRA METODO RCBRAMETODO : PUBLIC STATIC TIPO ID LPAR PARAMS RPAR LCBRA DC CMDS RETURN EXPRESSAO SEMICOLON RCBRA\n              | emptyPARAMS : TIPO ID MAIS_PARAMS\n              | emptyMAIS_PARAMS : VIRGU PARAMS\n                   | emptyDC : VAR MAIS_DC\n          | emptyMAIS_DC : SEMICOLON DC\n               | emptyVAR : TIPO VARS SEMICOLONVARS : ID MAIS_VARMAIS_VAR : VIRGU VARS\n                | emptyTIPO : DOUBLECMDS : CMD MAIS_CMDS\n            | emptyMAIS_CMDS : SEMICOLON CMDS\n                 | emptyCMD : IF LPAR CONDICAO RPAR LCBRA CMDS RCBRA PFALSA\n           | WHILE LPAR CONDICAO RPAR LCBRA CMDS RCBRA\n           | PRINT LPAR EXPRESSAO RPAR\n           | ID RESTO_IDENTPFALSA : ELSE LCBRA CMDS RCBRA \n              | emptyRESTO_IDENT : IGUAL EXP_IDENT\n                   | LPAR LISTA_ARG RPARCONDICAO : EXPRESSAO IGUAL EXPRESSAO\n                | EXPRESSAO MEN EXPRESSAO\n                | EXPRESSAO MEN_IGUAL EXPRESSAO\n                | EXPRESSAO MAI EXPRESSAO\n                | EXPRESSAO MAI_IGUAL EXPRESSAO\n                | EXPRESSAO DIF EXPRESSAO\n                | NEG EXPRESSAOLISTA_ARG : ARGUMENTOS \n                 | emptyARGUMENTOS : ID MAIS_IDENT \n                  | emptyMAIS_IDENT : VIRGU ARGUMENTOS \n                  | emptyEXP_IDENT : EXPRESSAO\n                 | TERMOEXPRESSAO : TERMO OUTROS_TERMOSTERMO : OP_UN FATOR MAIS_FATORESOP_UN : MENOS\n             | emptyFATOR : ID\n             | DOUBLE\n             | LPAR EXPRESSAO RPAROUTROS_TERMOS : OP_AD TERMO OUTROS_TERMOS\n                     | emptyOP_AD : SUM\n             | MENOSMAIS_FATORES : OP_MUL FATOR MAIS_FATORES\n                    | emptyOP_MUL : MUL\n              | DIVIempty :'
    
_lr_action_items = {'PUBLIC':([0,5,27,],[2,6,44,]),'$end':([1,68,],[0,-1,]),'CLASS':([2,],[3,]),'ID':([3,13,16,25,26,29,31,32,33,37,38,39,50,55,57,58,62,65,70,71,72,73,74,75,81,83,84,88,89,90,97,108,116,120,123,124,125,126,131,132,133,134,136,138,139,],[4,14,17,-59,43,17,-59,-59,-59,60,-46,-47,-59,-59,-53,-54,-59,43,-59,-59,-59,-59,-59,-59,60,-57,-58,101,-16,17,17,114,17,-59,129,17,-59,-9,-8,-59,-11,-12,129,-59,-10,]),'LCBRA':([4,15,69,77,112,115,],[5,16,90,97,116,120,]),'STATIC':([6,44,],[7,67,]),'VOID':([7,],[8,]),'MAIN':([8,],[9,]),'LPAR':([9,17,21,22,23,25,31,32,33,37,38,39,50,55,57,58,62,70,71,72,73,74,75,81,83,84,101,138,],[10,26,31,32,33,-59,-59,-59,-59,62,-46,-47,-59,-59,-53,-54,-59,-59,-59,-59,-59,-59,-59,62,-57,-58,105,-59,]),'STRING':([10,],[11,]),'LSBRA':([11,],[12,]),'RSBRA':([12,],[13,]),'RPAR':([14,26,40,41,42,43,48,51,52,53,54,56,59,60,61,64,65,66,76,79,80,82,85,86,87,91,92,93,94,95,96,98,99,100,104,105,109,110,114,117,118,119,122,],[15,-59,63,-36,-37,-59,69,-59,77,78,-44,-52,-59,-48,-49,-38,-59,-41,-35,-59,-45,-56,100,-40,-39,-29,-30,-31,-32,-33,-34,-51,-59,-50,-55,-59,115,-5,-59,-4,-59,-7,-6,]),'IF':([16,29,90,97,116,120,124,125,126,131,132,133,134,139,],[21,21,21,21,21,-59,21,-59,-9,-8,-59,-11,-12,-10,]),'WHILE':([16,29,90,97,116,120,124,125,126,131,132,133,134,139,],[22,22,22,22,22,-59,22,-59,-9,-8,-59,-11,-12,-10,]),'PRINT':([16,29,90,97,116,120,124,125,126,131,132,133,134,139,],[23,23,23,23,23,-59,23,-59,-9,-8,-59,-11,-12,-10,]),'RCBRA':([16,18,19,20,24,27,28,29,30,34,35,36,45,46,47,54,56,59,60,61,63,78,79,80,82,90,97,98,99,100,102,103,104,106,107,111,113,116,121,127,142,143,],[-59,27,-59,-18,-24,-59,-17,-59,-20,-27,-42,-43,68,-3,-19,-44,-52,-59,-48,-49,-28,-23,-59,-45,-56,-59,-59,-51,-59,-50,106,107,-55,-59,-22,-21,-26,-59,127,-25,143,-2,]),'IGUAL':([17,49,51,54,56,59,60,61,79,80,82,98,99,100,104,],[25,70,-59,-44,-52,-59,-48,-49,-59,-45,-56,-51,-59,-50,-55,]),'SEMICOLON':([19,24,34,35,36,51,54,56,59,60,61,63,78,79,80,82,98,99,100,104,106,107,111,113,125,127,128,129,134,135,137,140,141,],[29,-24,-27,-42,-43,-59,-44,-52,-59,-48,-49,-28,-23,-59,-45,-56,-51,-59,-50,-55,-59,-22,-21,-26,132,-25,134,-59,-12,-13,-15,-14,142,]),'RETURN':([19,20,24,28,29,30,34,35,36,47,54,56,59,60,61,63,78,79,80,82,98,99,100,104,106,107,111,113,120,124,125,126,127,130,131,132,133,134,139,],[-59,-18,-24,-17,-59,-20,-27,-42,-43,-19,-44,-52,-59,-48,-49,-28,-23,-59,-45,-56,-51,-59,-50,-55,-59,-22,-21,-26,-59,-59,-59,-9,-25,138,-8,-59,-11,-12,-10,]),'MENOS':([25,31,32,33,36,50,51,55,57,58,59,60,61,62,70,71,72,73,74,75,79,80,82,99,100,104,138,],[38,38,38,38,58,38,58,38,-53,-54,-59,-48,-49,38,38,38,38,38,38,38,58,-45,-56,-59,-50,-55,38,]),'DOUBLE':([25,31,32,33,37,38,39,50,55,57,58,62,67,70,71,72,73,74,75,81,83,84,105,118,120,132,138,],[-59,-59,-59,-59,61,-46,-47,-59,-59,-53,-54,-59,89,-59,-59,-59,-59,-59,-59,61,-57,-58,89,89,89,89,-59,]),'NEG':([31,32,],[50,50,]),'SUM':([36,51,59,60,61,79,80,82,99,100,104,],[57,57,-59,-48,-49,57,-45,-56,-59,-50,-55,]),'VIRGU':([43,114,129,],[65,118,136,]),'MEN':([49,51,54,56,59,60,61,79,80,82,98,99,100,104,],[71,-59,-44,-52,-59,-48,-49,-59,-45,-56,-51,-59,-50,-55,]),'MEN_IGUAL':([49,51,54,56,59,60,61,79,80,82,98,99,100,104,],[72,-59,-44,-52,-59,-48,-49,-59,-45,-56,-51,-59,-50,-55,]),'MAI':([49,51,54,56,59,60,61,79,80,82,98,99,100,104,],[73,-59,-44,-52,-59,-48,-49,-59,-45,-56,-51,-59,-50,-55,]),'MAI_IGUAL':([49,51,54,56,59,60,61,79,80,82,98,99,100,104,],[74,-59,-44,-52,-59,-48,-49,-59,-45,-56,-51,-59,-50,-55,]),'DIF':([49,51,54,56,59,60,61,79,80,82,98,99,100,104,],[75,-59,-44,-52,-59,-48,-49,-59,-45,-56,-51,-59,-50,-55,]),'MUL':([59,60,61,99,100,],[83,-48,-49,83,-50,]),'DIVI':([59,60,61,99,100,],[84,-48,-49,84,-50,]),'ELSE':([106,],[112,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROG':([0,],[1,]),'CMDS':([16,29,90,97,116,124,],[18,47,102,103,121,130,]),'CMD':([16,29,90,97,116,124,],[19,19,19,19,19,19,]),'empty':([16,19,25,26,27,29,31,32,33,36,43,50,51,55,59,62,65,70,71,72,73,74,75,79,90,97,99,105,106,114,116,118,120,124,125,129,132,138,],[20,30,39,42,46,20,39,39,39,56,66,39,56,39,82,39,87,39,39,39,39,39,39,56,20,20,82,110,113,119,20,110,126,20,133,137,126,39,]),'RESTO_IDENT':([17,],[24,]),'MAIS_CMDS':([19,],[28,]),'EXP_IDENT':([25,],[34,]),'EXPRESSAO':([25,31,32,33,50,62,70,71,72,73,74,75,138,],[35,49,49,53,76,85,91,92,93,94,95,96,141,]),'TERMO':([25,31,32,33,50,55,62,70,71,72,73,74,75,138,],[36,51,51,51,51,79,51,51,51,51,51,51,51,51,]),'OP_UN':([25,31,32,33,50,55,62,70,71,72,73,74,75,138,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'LISTA_ARG':([26,],[40,]),'ARGUMENTOS':([26,65,],[41,86,]),'METODO':([27,],[45,]),'CONDICAO':([31,32,],[48,52,]),'OUTROS_TERMOS':([36,51,79,],[54,54,98,]),'OP_AD':([36,51,79,],[55,55,55,]),'FATOR':([37,81,],[59,99,]),'MAIS_IDENT':([43,],[64,]),'MAIS_FATORES':([59,99,],[80,104,]),'OP_MUL':([59,99,],[81,81,]),'TIPO':([67,105,118,120,132,],[88,108,108,123,123,]),'PARAMS':([105,118,],[109,122,]),'PFALSA':([106,],[111,]),'MAIS_PARAMS':([114,],[117,]),'DC':([120,132,],[124,139,]),'VAR':([120,132,],[125,125,]),'VARS':([123,136,],[128,140,]),'MAIS_DC':([125,],[131,]),'MAIS_VAR':([129,],[135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROG","S'",1,None,None,None),
  ('PROG -> PUBLIC CLASS ID LCBRA PUBLIC STATIC VOID MAIN LPAR STRING LSBRA RSBRA ID RPAR LCBRA CMDS RCBRA METODO RCBRA','PROG',19,'p_prog','sintatico.py',45),
  ('METODO -> PUBLIC STATIC TIPO ID LPAR PARAMS RPAR LCBRA DC CMDS RETURN EXPRESSAO SEMICOLON RCBRA','METODO',14,'p_metodo','sintatico.py',49),
  ('METODO -> empty','METODO',1,'p_metodo','sintatico.py',50),
  ('PARAMS -> TIPO ID MAIS_PARAMS','PARAMS',3,'p_params','sintatico.py',54),
  ('PARAMS -> empty','PARAMS',1,'p_params','sintatico.py',55),
  ('MAIS_PARAMS -> VIRGU PARAMS','MAIS_PARAMS',2,'p_mais_params','sintatico.py',59),
  ('MAIS_PARAMS -> empty','MAIS_PARAMS',1,'p_mais_params','sintatico.py',60),
  ('DC -> VAR MAIS_DC','DC',2,'p_dc','sintatico.py',64),
  ('DC -> empty','DC',1,'p_dc','sintatico.py',65),
  ('MAIS_DC -> SEMICOLON DC','MAIS_DC',2,'p_mais_dc','sintatico.py',69),
  ('MAIS_DC -> empty','MAIS_DC',1,'p_mais_dc','sintatico.py',70),
  ('VAR -> TIPO VARS SEMICOLON','VAR',3,'p_var','sintatico.py',74),
  ('VARS -> ID MAIS_VAR','VARS',2,'p_vars','sintatico.py',78),
  ('MAIS_VAR -> VIRGU VARS','MAIS_VAR',2,'p_mais_var','sintatico.py',82),
  ('MAIS_VAR -> empty','MAIS_VAR',1,'p_mais_var','sintatico.py',83),
  ('TIPO -> DOUBLE','TIPO',1,'p_tipo','sintatico.py',87),
  ('CMDS -> CMD MAIS_CMDS','CMDS',2,'p_cmds','sintatico.py',91),
  ('CMDS -> empty','CMDS',1,'p_cmds','sintatico.py',92),
  ('MAIS_CMDS -> SEMICOLON CMDS','MAIS_CMDS',2,'p_mais_cmds','sintatico.py',96),
  ('MAIS_CMDS -> empty','MAIS_CMDS',1,'p_mais_cmds','sintatico.py',97),
  ('CMD -> IF LPAR CONDICAO RPAR LCBRA CMDS RCBRA PFALSA','CMD',8,'p_cmd','sintatico.py',101),
  ('CMD -> WHILE LPAR CONDICAO RPAR LCBRA CMDS RCBRA','CMD',7,'p_cmd','sintatico.py',102),
  ('CMD -> PRINT LPAR EXPRESSAO RPAR','CMD',4,'p_cmd','sintatico.py',103),
  ('CMD -> ID RESTO_IDENT','CMD',2,'p_cmd','sintatico.py',104),
  ('PFALSA -> ELSE LCBRA CMDS RCBRA','PFALSA',4,'p_pfalsa','sintatico.py',108),
  ('PFALSA -> empty','PFALSA',1,'p_pfalsa','sintatico.py',109),
  ('RESTO_IDENT -> IGUAL EXP_IDENT','RESTO_IDENT',2,'p_resto_ident','sintatico.py',113),
  ('RESTO_IDENT -> LPAR LISTA_ARG RPAR','RESTO_IDENT',3,'p_resto_ident','sintatico.py',114),
  ('CONDICAO -> EXPRESSAO IGUAL EXPRESSAO','CONDICAO',3,'p_condicao','sintatico.py',118),
  ('CONDICAO -> EXPRESSAO MEN EXPRESSAO','CONDICAO',3,'p_condicao','sintatico.py',119),
  ('CONDICAO -> EXPRESSAO MEN_IGUAL EXPRESSAO','CONDICAO',3,'p_condicao','sintatico.py',120),
  ('CONDICAO -> EXPRESSAO MAI EXPRESSAO','CONDICAO',3,'p_condicao','sintatico.py',121),
  ('CONDICAO -> EXPRESSAO MAI_IGUAL EXPRESSAO','CONDICAO',3,'p_condicao','sintatico.py',122),
  ('CONDICAO -> EXPRESSAO DIF EXPRESSAO','CONDICAO',3,'p_condicao','sintatico.py',123),
  ('CONDICAO -> NEG EXPRESSAO','CONDICAO',2,'p_condicao','sintatico.py',124),
  ('LISTA_ARG -> ARGUMENTOS','LISTA_ARG',1,'p_lista_arg','sintatico.py',143),
  ('LISTA_ARG -> empty','LISTA_ARG',1,'p_lista_arg','sintatico.py',144),
  ('ARGUMENTOS -> ID MAIS_IDENT','ARGUMENTOS',2,'p_argumentos','sintatico.py',148),
  ('ARGUMENTOS -> empty','ARGUMENTOS',1,'p_argumentos','sintatico.py',149),
  ('MAIS_IDENT -> VIRGU ARGUMENTOS','MAIS_IDENT',2,'p_mais_ident','sintatico.py',153),
  ('MAIS_IDENT -> empty','MAIS_IDENT',1,'p_mais_ident','sintatico.py',154),
  ('EXP_IDENT -> EXPRESSAO','EXP_IDENT',1,'p_exp_ident','sintatico.py',158),
  ('EXP_IDENT -> TERMO','EXP_IDENT',1,'p_exp_ident','sintatico.py',159),
  ('EXPRESSAO -> TERMO OUTROS_TERMOS','EXPRESSAO',2,'p_expressao','sintatico.py',167),
  ('TERMO -> OP_UN FATOR MAIS_FATORES','TERMO',3,'p_termo','sintatico.py',171),
  ('OP_UN -> MENOS','OP_UN',1,'p_op_un','sintatico.py',175),
  ('OP_UN -> empty','OP_UN',1,'p_op_un','sintatico.py',176),
  ('FATOR -> ID','FATOR',1,'p_fator','sintatico.py',180),
  ('FATOR -> DOUBLE','FATOR',1,'p_fator','sintatico.py',181),
  ('FATOR -> LPAR EXPRESSAO RPAR','FATOR',3,'p_fator','sintatico.py',182),
  ('OUTROS_TERMOS -> OP_AD TERMO OUTROS_TERMOS','OUTROS_TERMOS',3,'p_outros_termos','sintatico.py',189),
  ('OUTROS_TERMOS -> empty','OUTROS_TERMOS',1,'p_outros_termos','sintatico.py',190),
  ('OP_AD -> SUM','OP_AD',1,'p_op_ad','sintatico.py',194),
  ('OP_AD -> MENOS','OP_AD',1,'p_op_ad','sintatico.py',195),
  ('MAIS_FATORES -> OP_MUL FATOR MAIS_FATORES','MAIS_FATORES',3,'p_mais_fatores','sintatico.py',203),
  ('MAIS_FATORES -> empty','MAIS_FATORES',1,'p_mais_fatores','sintatico.py',204),
  ('OP_MUL -> MUL','OP_MUL',1,'p_op_mul','sintatico.py',208),
  ('OP_MUL -> DIVI','OP_MUL',1,'p_op_mul','sintatico.py',209),
  ('empty -> <empty>','empty',0,'p_empty','sintatico.py',216),
]
