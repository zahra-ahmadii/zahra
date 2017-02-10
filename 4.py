import math
import re
tokens = ('NUMBER','PLUS','MENHA','ZARB','TAGHSIM','PARANTEZBAZ','PRANTEZBASTE',
          'RESHTE','MOSAVI','MAIN','KOROSHEBAZ','KOROSHEBASTE','IF','ELSE'
          ,'WHILE','PRINT','INPUT','COTEITION','BODY','EQUAL','NOTEQUAL','K',
          'BO','BM','KM','M','KAMA','SIN','COS','TAN','POW','SQRT','INT','DOUBLE','STRING','FASELE','LINE','VOID') 
t_PLUS    = r'\+'
t_MENHA   =r'\-'
t_ZARB=r'\*'
t_TAGHSIM=r'\/'
t_MOSAVI=r'='
t_KOROSHEBASTE=r'}'
t_KAMA=r','
dic={}
global res,res2,elsres2
memID=0
global c,c1
c=0
c1=1
lbl_counter=0
f3=open("zari3.txt","w")
global flag,y
def t_VOID(t):
    r'void'
    return t
def t_INT(t):
    r'int'
    return t
def t_DOUBLE(t):
    r'double'
    return t
def t_STRING(t):
    r'string'
    return t
def t_FASELE(t):
    r'\ '
    return t
def t_PARANTEZBAZ(t):
    r'\('
    return t
def t_PRANTEZBASTE(t):
    r'\)'
    return t
def t_MAIN(t):
    r'main'
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
def t_M(t):
    r'=='
    return t
def memAloc():
    global memID
    memID += 1
    return '['+str(memID-1)+']'

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
def p_s_s(p):
    'START : S'
    p[0]=p[1]
def p_s_i(p):
    'S : INT MAIN PARANTEZBAZ PRANTEZBASTE KOROSHEBAZ A'
  
    p[0]=p[5]
def p_s_a(p):
    r'S : A'
    p[0]=p[1]
def p_SE(p):
    r'A : E '
    #print(p[1][0])
    p[0]=p[1]
def p_b(p):
    'A : BODY'
    p[0]=p[1]


def p_w(p):
    'A : WHILE PARANTEZBAZ CONDITION  PRANTEZBASTE KOROSHEBAZ A'
    L1='L'+lable_counter()
    L2='L'+lable_counter()
    #print(p[3])
    p[0]=(L1+','+p[3]+','+'jnz'+L2+','+p[6]+','+'goto'+L1+','+L2+'\n')
    f3.writelines(p[0])
    f3.writelines(p[5]+'\n')
    #print(p[0])
    

def p_ife(p):
    'A : IF PARANTEZBAZ CONDITION PRANTEZBASTE KOROSHEBAZ A'
    #print(p[6])
    L1='L'+lable_counter()
    L2='L'+lable_counter()
    p[0]=(p[3]+','+'jnz'+L1+','+p[6]+','+'goto'+L2+'\n')
    f3.writelines(p[0])
    f3.writelines(p[5]+'\n')
    #print(p[0])

def p_ife2(p):
    'A :  ELSE KOROSHEBAZ A'
    L1='L'+lable_counter()
    L2='L'+lable_counter()
    p[0]=(L1+','+p[3]+','+L2+'\n')
    #print(p[0])
    f3.writelines(p[0])
    f3.writelines(p[2]+'\n')
    
def p_la(p):
    'A : '
    p[0]=''
def p_koroshe(p):
    'A : KOROSHEBASTE'
    p[0]=(p[1])
    f3.writelines(p[0]+'\n')
def p_a_A(p):
    'A : A'
    p[0]=p[1]
def p_LINE(p):
    'A : LINE'
    p[0]=p[1]
def p_input(p):
    r'A : RESHTE MOSAVI INPUT PARANTEZBAZ PRANTEZBASTE'
    p[0]=p[1]
    f3.writelines(p[1]+'='+'INPUT'+'('+')'+'\n')
    x=input('vared kon reshte morede nazar ')
    f3.writelines(dic[p[1]][1]+'='+x+'\n')
    
def p_PRINT(p):
    'A : PRINT PARANTEZBAZ DD RESHTE DD PRANTEZBASTE'
    if(p[3]=='\''):
        p[0]=('\''+p[4]+'\'')
    elif p[4] in dic:
        p[0]=dic[p[4]][1]
    
    f3.writelines('PRINT'+'('+p[0]+')'+'\n')
    
def p_RESHTE_e(p):
   'A : RESHTE MOSAVI E'
   #print(dic)
           
   if type(p[3]) == tuple:
      
       f3.writelines(p[3][0])
       f3.writelines(dic[p[1]][1]+"="+str(p[3][1])+'\n')
   elif(type(p[3])!= tuple):
     if p[1] in dic:
        
      p[0]=str(p[3])
      
      f3.writelines(dic[p[1]][1]+'='+str(p[3])+'\n')
     else:
        
        print('eror reshte=E',p[1])
def p_tabee(p):
    'A : TYYPPE RESHTE PARANTEZBAZ A PRANTEZBASTE KOROSHEBAZ A'
def p_tape2(p):
    'TYYPPE : TYPE'
    p[0]=p[1]
def p_tape3(p):
    'TYYPPE : VOID'
    p[0]=p[1]
def p_type(p):
    'A : TYPE RESHTE'
    dic[p[2]]=[p[1],memAloc()]
    #print(dic[p[2]])
def p_type1(p):
    'TYPE : INT'
    p[0]=p[1]
    #print(p[0])
def p_type2(p):
    'TYPE : DOUBLE'
    p[0]=p[1]
    #print(p[0])
def p_type3(p):
    'TYPE : STRING'
    p[0]=p[1]
    #print(p[0])   
def p_CONDITION2(p):
    'CONDITION2 : TY K TY'
    if(p[2]=='<'):
      p[0]=(str(p[1])+'>='+str(p[3]))
def p_CONDITION(p):
    'CONDITION : TY K TY'         
    if(p[2]=='<'):
      p[0]=(p[1]+'<'+p[3])
    elif(p[2]=='>'):
        p[0]=(p[1]+'>'+p[3])
    elif(p[2]=='>='):
        p[0]=(p[1]+'>='+p[3])
    elif(p[2]=='<='):
        p[0]=(p[1]+'<='+p[3])
    elif(p[2]=='!='):
        p[0]=(p[1]+'!='+p[3])
def p_ty2(p):
    'TY : F'
    p[0]=p[1]
def p_ty(p):
    'TY : RESHTE'
    #print(dic[p[1]][0])
   # print(p[1])
    if p[1] in dic:
     p[0]=dic[p[1]][1]
     
    else:
        print('eror reshte')

def p_sin(p):
    'A : RESHTE MOSAVI SIN PARANTEZBAZ NUMBER PRANTEZBASTE'
    
    
    dic[p[1]]=[math.sin(float(p[5]))]
    p[0]=p[1]
    f3.writelines(p[1]+'='+'SIN'+'('+p[5]+')'+'\n')
    #print(p[1],'=',dic[p[1]])
   
def p_cos(p):
    'A : RESHTE MOSAVI COS PARANTEZBAZ E PRANTEZBASTE'
    dic[p[1]]=[math.cos(float(p[5]))]
    p[0]=p[1]
    f3.writelines(p[1]+'='+'COS'+'('+p[5]+')'+'\n')
    #print(p[1],'=',dic[p[1]])
   
def p_tan(p):
    'A : RESHTE MOSAVI TAN PARANTEZBAZ E PRANTEZBASTE'
    dic[p[1]]=[math.tan(float(p[5]))]
    p[0]=p[1]
    f3.writelines(p[1]+'='+'TAN'+'('+p[5]+')'+'\n')
    #print(p[1],'=',dic[p[1]])
   
def p_pow(p):
    'A : RESHTE MOSAVI POW PARANTEZBAZ E KAMA E PRANTEZBASTE'
    dic[p[1]]=[math.pow(float(p[5]),float(p[7]))]
    p[0]=p[1]
    f3.writelines(p[1]+'='+'POW'+'('+p[5]+','+p[7]+')'+'\n')
    #print(p[1],'=',dic[p[1]])
def p_sqrt(p):
    'A : RESHTE MOSAVI SQRT PARANTEZBAZ E PRANTEZBASTE'
    dic[p[1]]=[math.sqrt(float(p[5]))]
    p[0]=p[1]
    f3.writelines(p[1]+'='+'SQRT'+'('+p[5]+')'+'\n')
    #print(p[1],'=',dic[p[1]])

def p_e_e_t(p):
   'E : E PLUS T'
   
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
   p[0] = (beforCode + 'ADD ' + str(oprand1) + ',' +str( oprand2) + ','+ mem+'\n' ,mem)
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
    p[0] = (beforCode + 'SUB ' + str(oprand1) + ',' + str(oprand2) + ','+ mem+'\n' ,mem)
def p_e_t(p):
   'E : T'
   p[0]=p[1]
def p_t_t_f(p):
    'T : T ZARB F' 
   
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
    p[0] = (beforCode + 'MUL ' + str(oprand1) + ',' + str(oprand2) + ','+ mem+'\n' ,mem)
    
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
    p[0] = (beforCode + 'TAGHSIM ' + str(oprand1) + ',' + str(oprand2) + ','+ mem+'\n' ,mem)
   
   # print('کاهش با قانون T → T / F  ',p[0])
def p_t_f(p):
   'T : F'
   p[0]=p[1]
   #print('کاهش با قانون T->F ',p[0])
def p_f_e(p):
   'F : PARANTEZBAZ E PRANTEZBASTE'
   p[0]=(p[2])
   global x
   x=p[0]
   #print('کاهش با قانون F->(E)',p[0])
def p_f_e_m(p):
   'F : MENHA PARANTEZBAZ E PRANTEZBASTE'
   p[0]=-(p[3])
   global x
   x=p[0]
   #print('کاهش با قانون F->-(E)',p[0])

def p_f_a3(p):
   
   'F : DD RESHTE DD'  
   if(p[1]=='\''):
     p[0]=p[2]
     #print(p[0]+"kkkkkk")
def p_f_a2(p):
   
   'F : RESHTE'
   
   if p[1] in dic:
    p[0]=dic[p[1]][1]
def p_DD2(p):
    r'DD : '
    #p[0]=
def p_DD(p):
    r'DD : COTEITION'
    p[0]=p[1]

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

def p_tab4(p):
    'A : ELIST'
    p[0]=p[1]
def p_tab3(p):
    'ELIST : RESHTE PARANTEZBAZ E'
    
def p_tab2(p):
    'ELIST : ELIST KAMA E'
def p_tab(p):
    'F : ELIST PRANTEZBASTE'
def p_error(p):
   print("Syntax error at '%s'" % p.value)
 
import ply.yacc as yacc


p=yacc.yacc()
f2_read=open("zari.txt","r")


while True:
   
   line1=f2_read.readline() 
   if line1=="END\n" :
       f2_read.close()
       break
   else:
    p.parse(line1)
f3.writelines('END\n')  
f3.close()    
import re
f_read1=open("zari3.txt","r")
araye={}
res='y'
res2='y'
elsres2='y'
while(1):

 line2=f_read1.readline()
 order=line2
 result=re.match("END\n",order)
 if(result):
     break
 result=re.match(r'ADD ((\[(\d+)\])|(\d+|(\d+\.\d+))|([a-zA-Z][a-zA-Z0-9 _\t]*)),((\[(\d+)\])|(\d+|(\d+\.\d+))|([a-zA-Z][a-zA-Z0-9 _\t]*)),\[(\d+)\]',order)
 if(result and res2 !='n' and res !='n'):
    if(result.group(3)!=None):
        a=araye[result.group(3)]
       
    elif(result.group(4)!=None):
         a=float(result.group(4))
    if(result.group(6)!=None):
        a=str(result.group(6))
        
    if(result.group(9)!=None):
         b=araye[result.group(9)]
      
    elif(result.group(10)!=None):
       b=float(result.group(10))
       
    if(result.group(12)!=None):
        b=str(result.group(12))
    araye[result.group(13)]=a+b
 result=re.match(r'SUB ((\[(\d+)\])|(\d+|(\d+\.\d+))|([a-zA-Z][a-zA-Z0-9 _\t]*)),((\[(\d+)\])|(\d+|(\d+\.\d+))|([a-zA-Z][a-zA-Z0-9 _\t]*)),\[(\d+)\]',order)
 if(result and res2 !='n' and res !='n'):
    if(result.group(3)!=None):
        a=araye[result.group(3)]
       
    elif(result.group(4)!=None):
         a=float(result.group(4))
    if(result.group(6)!=None):
        b=str(result.group(6))
    if(result.group(9)!=None):
         b=araye[result.group(9)]
      
    elif(result.group(10)!=None):
       b=float(result.group(10))
       
    if(result.group(12)!=None):
        b=str(result.group(12))
    if(type(a)==str and type(b)==str):
        
        araye[result.group(13)]=a[:a.find(b)]+a[a.find(b)+len(b):]
       
    else:
       araye[result.group(13)]=a-b
 result=re.match(r'MUL ((\[(\d+)\])|(\d+|(\d+\.\d+))),((\[(\d+)\])|(\d+|(\d+\.\d+))),\[(\d+)\]',order)
 if(result and res2 !='n' and res !='n'):
    if(result.group(3)==None):
      a=int(result.group(4))
    else:
        a=araye[result.group(3)]
   
    if(result.group(8)==None):
      b=int(result.group(9))
    else:
        b=araye[result.group(8)]
    
    araye[result.group(11)]=a*b
 result=re.match(r'TAGHSIM ((\[(\d+)\])|(\d+|(\d+\.\d+))),((\[(\d+)\])|(\d+|(\d+\.\d+))),\[(\d+)\]',order)
 
 if(result and res2 !='n' and res !='n'):
    if(result.group(3)==None):
        a=float(result.group(4))
    else:
        a=araye[result.group(3)]
    if(result.group(8)==None):
      b=float(result.group(9))
    else:
        b=araye[result.group(8)]
    
    araye[result.group(11)]=a/b
 result=re.match(r'\[(\d+)\]=((\[(\d+)\])|(\d+)|([a-zA-Z][a-zA-Z0-9 _\t]*))\n',order)
 if(result and res2 =='y' and res !='n'):
     #if(res2 =='y' and res !='n'):
       
        if(result.group(4)!=None):
            araye[result.group(1)]=araye[result.group(4)]
            
        elif(result.group(5)!=None):
            araye[result.group(1)]=float(result.group(5))
        else:
            araye[result.group(1)]=result.group(6)
 result=re.match(r'PRINT(\()(\'?)((\[(\d+)\])|(\d+|\d+\.\d+)|([a-zA-Z][a-zA-Z0-9 _\t]*))(\'?)(\))',order)
 if(result and res2 !='n' and res !='n'):
     if(result.group(2)==''):
             print(araye[result.group(5)])
            
     if(result.group(2)!=''):
          print(result.group(3))
 result=re.match(r'([a-zA-Z][a-zA-Z0-9 _\t]*)=INPUT(\()(\))',order)
 #if(result and res2 !='n'):
     
     #araye[result.group(1)]=input()
     
     #f3.writelines(dic[result.group(1)][1]+'='+araye[result.group(1)]+'\n')
     
 result=re.match(r'([a-zA-Z][a-zA-Z0-9 _\t]*)=SIN(\()(\d+)(\))',order)
 if(result and res2 !='n' and res !='n'):
     araye[result.group(1)]=math.sin(float(result.group(3)))
 result=re.match(r'([a-zA-Z][a-zA-Z0-9 _\t]*)=COS(\()(\d+)(\))',order)
 if(result and res2 !='n' and res !='n'):
     araye[result.group(1)]=math.cos(float(result.group(3)))
 result=re.match(r'([a-zA-Z][a-zA-Z0-9 _\t]*)=TAN(\()(\d+)(\))',order)
 if(result and res2 !='n' and res !='n'):
     araye[result.group(1)]=math.tan(float(result.group(3)))
 result=re.match(r'([a-zA-Z][a-zA-Z0-9 _\t]*)=POW(\()(\d+),(\d+)(\))',order)
 if(result and res2 !='n' and res !='n'):
     araye[result.group(1)]=math.pow(float(result.group(3)),float(result.group(4)))
 result=re.match(r'([a-zA-Z][a-zA-Z0-9 _\t]*)=SQRT(\()(\d+)(\))',order)
 if(result and res2 !='n' and res !='n'):
     araye[result.group(1)]=math.sqrt(float(result.group(3)))
 result=re.match(r'L(\d+),((\[(\d+)\])(<|>|<=|>=|!=|==)(\[(\d+)\])),jnzL(\d+),(.*),gotoL(\d+),L(\d+)\n',order)
 if(result):
     a=araye[result.group(4)]
     b=araye[result.group(7)]
     if(result.group(5)=='<'):
         if(a<b):
             res='y'
             global c
             c=b-a
             #print(res)
         else:
            res='n'
     elif(result.group(5)=='>'):
         if(a>b):
             res='y'
             global c
             c=a-b
             #print(res)
         else:
            res='n'
     elif(result.group(5)=='<='):
      if(a<=b):
             res='y'
             global c
             c=(b-a)+1
             #print(res)
      else:
            res='n'
     elif(result.group(5)=='>='):
       if(a>=b):
             res='y'
             global c
             c=(a-b)+1
             #print(res)
       else:
            res='n'
     elif(result.group(5)=='!='):
      if(a!=b):
             res='y'
             global c
             
             if(a>b):
               c=(a-b)+1
             elif(a<b):
                 c=(b-a)+1
             #print(res)
             else:
               res='n'
     elif(result.group(5)=='=='):
      if(a==b):
             res='y'
             
             #print(res)
      else:
            res='n'
 result=re.match(r'((\[(\d+)\])(<|>|<=|>=|!=|==)(\[(\d+)\])),jnzL(\d+),(.*),gotoL(\d+)\n',order)
 if(result):
     a=araye[result.group(3)]
     b=araye[result.group(6)]
     if(result.group(4)=='<'):
         if(a<b):
             
             res2='y'
             elsres2='n'
             #print(a,b,elsres2)
         else:
            res2='n'
     elif(result.group(4)=='>'):
         if(a>b):
             
             res2='y'
             elsres2='n'
             #print(a,b,elsres2)
         else:
            res2='n'
     elif(result.group(4)=='>='):
         if(a>=b):
             
             res2='y'
             elsres2='n'
             #print(a,b,elsres2)
         else:
            res2='n'
     elif(result.group(4)=='<='):
         if(a<=b):
             
             res2='y'
             elsres2='n'
             #print(a,b,elsres2)
         else:
            res2='n'
     elif(result.group(4)=='!='):
         if(a!=b):
             
             res2='y'
             elsres2='n'
             #print(a,b,elsres2)
         else:
            res2='n'
     elif(result.group(4)=='=='):
         if(a==b):
             
             res2='y'
             elsres2='n'
             #print(a,b,elsres2)
         else:
            res2='n'
 result=re.match(r'L(\d+),(.*),L(\d+)\n',order)
 if(result):
     
     if(elsres2=='n'):
         res2='n'
 result=re.match(r'}\n',order)
 if(result):
     if(res2 =='n'):
         res2='y'
     
    
     if( res=='y' and(c1<c-1)):
             c1=c1+1
             #print(c)
             f_read1.close();
             f_read1=open("zari3.txt","r")
             line2=f_read1.readline()
            
             while(1):
                 if(line2!='{'+'\n'):
                     line2=f_read1.readline()
                     
                 else:
                   break
     elif(res =='n'):
         res='y'
print(araye)

#print(dic)   
