
tokens = ('NUMBER','PLUS','MENHA','ZARB','TAGHSIM','PARANTEZBAZ','PRANTEZBASTE',
          'RESHTE','MOSAVI','INTMAIN','KOROSHEBAZ','KOROSHEBASTE','IF','ELSE'
          ,'WHILE','PRINT','INPUT','COTEITION','BODY','EQUAL','NOTEQUAL','K',
          'BO','BM','KM','KAMA','SIN','COS','TAN','POW','SQRT') 
t_PLUS    = r'\+'
t_MENHA   =r'\-'
t_ZARB=r'\*'
t_TAGHSIM=r'\/'
t_MOSAVI=r'='
t_KOROSHEBASTE=r'}'
t_KAMA=r','
dic={}
memID=0
lbl_counter=0

def t_PARANTEZBAZ(t):
    r'\('
    return t
def t_PRANTEZBASTE(t):
    r'\)'
    return t
def t_INTMAIN(t):
    r'int main'
    return t
def t_KOROSHEBAZ(t):
    r'{'
    return t
def t_SIN(t):
    r'sin'
    return t
def t_COS(t):
    r'cos'
    return t
def t_TAN(t):
    r'tan'
    return t
def t_POW(t):
    r'pow'
    return t
def t_SQRT(t):
    r'sqrt'
    return t
#def t_KOROSHEBASTE(t):
 #   r'\}'
  #  return t
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_PRINT(t):
    r'print'
    return t
def t_INPUT(t):
    r'input'
    return t
def t_COTEITION(t):
    r'\''
    return t
def t_NOTEQUAL(t):
    r'!='
    return t
def t_BM(t):
    r'>='
    return t
def t_BO(t):
    r'>'
    return t
def t_KM(t):
    r'<='
    return t
def t_K(t):
    r'<'
    return t
def t_EQUAL(t):
    r':='
    return t
def memAloc():
    global memID
    memID += 1
    return '['+str(memID-1)+']'
def t_BODY(t):
    r'({.+?}) | (.+?);'
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
def t_NUMBER(t):
   r'\d+'
   #t.value = int(t.value)
   return t
def t_RESHTE(t):
    r'[a-zA-Z][a-zA-Z0-9 _\t]*'
    return t
t_ignore = " \t" 
def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1) 
 
import ply.lex as lex
lex.lex()
def lable_counter():
      global lbl_counter
      lbl_counter=lbl_counter+1
      return str(lbl_counter)
#def p_s_s(p):
  #  'START : S'
 #   p[0]=p[1]
#def p_s_i(p):
    #'S : INTMAIN PARANTEZBAZ PRANTEZBASTE KOROSHEBAZ A KOROSHEBASTE'
   # p[0]=p[5]
def p_s_a(p):
    r'S : A'
    p[0]=p[1]
def p_SE(p):
    r'A : E '
    print(p[1][0])
    p[0]=p[1]
def p_b(p):
    'A : BODY'
    p[0]=p[1]
def p_la(p):
    'A : '
    #p[0]=p[1]
def p_w(p):
    'A : WHILE PARANTEZBAZ CONDITION  PRANTEZBASTE KOROSHEBAZ A KOROSHEBASTE'
    p[0]=["IF" ,p[3],' JUMP ','LABLE',lable_counter(),p[6],'\n','ELSE','JUMP','LABLE',lable_counter(),':\n']
    print(p[0])
    
'''def p_if(p):
    'A : IF PARANTEZBAZ CONDITION PRANTEZBASTE KOROSHEBAZ A KOROSHEBASTE'
    p[0]=["IF" ,P[3],' JUMP ','LABLE',lable_counter(),'\n','LABLE',lable_counter(),':\n']
    #labl= newLabel()
    #p[0]=[p[3],"if_false","jump labl1",p[6],"goto labl1",labl1]'''
    
def p_ife(p):
    'A : IF PARANTEZBAZ CONDITION2 PRANTEZBASTE KOROSHEBAZ A  KOROSHEBASTE ELSE KOROSHEBAZ A KOROSHEBASTE '
    p[0]=["IF" ,p[3],' JUMP ','LABLE',lable_counter(),'ELSE',p[6],'\n','LABLE',lable_counter(),'GOTO L2','L1:',p[10],'L2:'':\n']
    print(p[0])
    
def p_input(p):
    r'A : RESHTE MOSAVI INPUT PARANTEZBAZ PRANTEZBASTE'
    if p[1] not in dic:
        
        print(p[1] +" is undifined")

def p_PRINT(p):
    'A : PRINT PARANTEZBAZ DD RESHTE DD PRANTEZBASTE'
    p[0]=('\''+p[4]+'\'')
    print(p[0])
def p_RESHTE2(p):
   'E : RESHTE MOSAVI RESHTE'
   p[1]=p[3]
   p[0]=p[1]
def p_RESHTE1(p):
   'E : RESHTE MOSAVI E'
   p[1]=p[3]
   p[0]=p[1]
   dic[p[1]]=p[3]
   global x
   x=p[1]
   print('کاهش با قانون s->RESHTE=E',p[1])
def p_CONDITION2(p):
    'CONDITION2 : TY K TY'
    if(p[2]=='<'):
      p[0]=(str(p[1])+'>='+str(p[3]))
def p_CONDITION(p):
    'CONDITION : TY K TY'         
    if(p[2]=='<'):
      p[0]=(str(p[1])+'<'+str(p[3]))
def p_ty(p):
    'TY : RESHTE'
    p[0]=p[1]
def p_ty2(p):
    'TY : F'
    p[0]=p[1]
def p_sin(p):
    'A : RESHTE MOSAVI SIN PARANTEZBAZ E PRANTEZBASTE'
    p[1]=sin(p[5])
    p[0]=p[1]
def p_cos(p):
    'A : RESHTE MOSAVI COS PARANTEZBAZ E PRANTEZBASTE'
    p[1]=cos(p[5])
    p[0]=p[1]
def p_tan(p):
    'A : RESHTE MOSAVI TAN PARANTEZBAZ E PRANTEZBASTE'
    p[1]=tan(p[5])
    p[0]=p[1]
def p_pow(p):
    'A : RESHTE MOSAVI POW PARANTEZBAZ E KAMA E PRANTEZBASTE'
    p[1]=pow(p[5],p[7])
    p[0]=p[1]
def p_sqrt(p):
    'A : RESHTE MOSAVI SQRT PARANTEZBAZ E PRANTEZBASTE'
    p[1]=sqrt(p[5])
    p[0]=p[1]
def p_DD(p):
    r'DD : COTEITION'
    p[0]=p[1]
def p_DD2(p):
    r'DD : '
    p[0]='0'
'''def p_TY(p):
    'TY : RESHTE'
    P[0]=P[1]'''
def p_e_e_t(p):
   'E : E PLUS T'
   #p[0] = p[1]+p[3]
   oprand1 =''
   oprand2 =''
   beforCode = ''
   if type(p[1]) == tuple:
        oprand1 = p[1][1]
        beforCode += p[1][0]
   else:
        oprand1 = p[1]
   if type(p[3]) == tuple:
        oprand2 = p[3][1]
        beforCode += p[3][0]
   else:  
        oprand2 = p[3]

   mem = memAloc()
   p[0] = (beforCode + 'ADD ' + oprand1 + ',' + oprand2 + ','+ mem+'\n' ,mem)
  # print(p[0])
   global x
   x=p[0]
   #print('کاهش با قانون E → E + E  ',p[0])
def p_e_e_t2(p):
    'E : E MENHA T' 
    #p[0] = p[1]-p[3]
    oprand1 =''
    oprand2 =''
    beforCode = ''
    if type(p[1]) == tuple:
        oprand1 = p[1][1]
        beforCode += p[1][0]
    else:
        oprand1 = p[1]
    if type(p[3]) == tuple:
        oprand2 = p[3][1]
        beforCode += p[3][0]
    else:  
        oprand2 = p[3]

    mem = memAloc()
    p[0] = (beforCode + 'SUB ' + oprand1 + ',' + oprand2 + ','+ mem+'\n' ,mem)
    global x
    x=p[0]
    #print('کاهش با قانون E → E - E  ',p[0])
def p_e_t(p):
   'E : T'
   p[0]=p[1]
   global x
   x=p[0]
   #print('کاهش با قانون E->T ',p[0])
def p_t_t_f(p):
    'T : T ZARB F' 
    #p[0] = p[1]*p[3]
    oprand1 =''
    oprand2 =''
    beforCode = ''
    if type(p[1]) == tuple:
        oprand1 = p[1][1]
        beforCode += p[1][0]
    else:
        oprand1 = p[1]
    if type(p[3]) == tuple:
        oprand2 = p[3][1]
        beforCode += p[3][0]
    else:  
        oprand2 = p[3]

    mem = memAloc()
    p[0] = (beforCode + 'MUL ' + oprand1 + ',' + oprand2 + ','+ mem+'\n' ,mem)
    global x
    x=p[0]
    #print('کاهش با قانون T → T * F  ',p[0])
def p_t_t_f2(p):
    'T : T TAGHSIM F' 
    #p[0] = p[1]/p[3]
    oprand1 =''
    oprand2 =''
    beforCode = ''
    if type(p[1]) == tuple:
        oprand1 = p[1][1]
        beforCode += p[1][0]
    else:
        oprand1 = p[1]
    if type(p[3]) == tuple:
        oprand2 = p[3][1]
        beforCode += p[3][0]
    else:  
        oprand2 = p[3]

    mem = memAloc()
    p[0] = (beforCode + 'ADD ' + oprand1 + ',' + oprand2 + ','+ mem+'\n' ,mem)
    global x
    x=p[0]
   # print('کاهش با قانون T → T / F  ',p[0])
def p_t_f(p):
   'T : F'
   p[0]=p[1]
   global x
   x=p[0]
   #print('کاهش با قانون T->F ',p[0])
def p_f_e(p):
   'F : PARANTEZBAZ E PRANTEZBASTE'
   p[0]=(p[2])
   global x
   x=p[0]
   print('کاهش با قانون F->(E)',p[0])
def p_f_e_m(p):
   'F : MENHA PARANTEZBAZ E PRANTEZBASTE'
   p[0]=-(p[3])
   global x
   x=p[0]
   print('کاهش با قانون F->-(E)',p[0])

   

     
def p_f_a(p):
   
   'F : NUMBER'
   p[0]=p[1]
   global x
   x=p[0]
   #print('کاهش با قانون F → a  ',p[1])

def p_f_a_m(p):
   
   'F : MENHA NUMBER'
   p[0]=-p[2]
   global x
   x=p[0]
   #print('کاهش با قانون F → -a  ',p[1])
def p_tab(p):
    'F : ELIST PRANTEZBASTE'
def p_tab2(p):
    'ELIST : ELIST KAMA E'
def p_tab3(p):
    'ELIST : RESHTE PARANTEZBAZ E'
def p_error(p):
   print("Syntax error at '%s'" % p.value)
 
import ply.yacc as yacc
#f2=open("zari.txt","a")
#f2.writelines("END")
#f2.close()

p=yacc.yacc()
f2_read=open("zari.txt","r")


while True:
  
   line1=f2_read.readline() 
   if line1=="END" :
       f2_read.close()
       break
   else:
    p.parse(line1)
    
    
   
   