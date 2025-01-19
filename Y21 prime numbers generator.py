import os # limpiar consola
import time

eleccion=True
valor=''
valorA=''
valor1=''
valor2=''
valor3=''
frase=''
cuestionario=''

def clear_console(): #FUNCION LIMPIAR CONSOLA
    if os.name == 'nt': # selector de sistema operativo para borrar el texto de la consola
        os.system('cls')     # Comando para Windows
        
    else:
        os.system('clear')   # Comando para Unix/Linux/Mac

    return()

def codg70(num,let,act):
      
      abc='a,b,c,d,e,f,g,h,i,j,k,l,ll,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
      ABC='A,B,C,D,E,F,G,H,I,J,K,L,LL,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
      NUM='0,1,2,3,4,5,6,7,8,9'
      SIMB= '¡,!,(,),[,],¬'

      cod=abc+','+ABC+','+NUM+','+SIMB
      cod70=cod.split(',')

      n=''
      s=0

      
      #codificado a  base 70

      if act==1:
            for n in cod70:
                  if s==num:
                        return(n)
                  s+=1

      if act==2:
            for n in cod70:
                  if n==let:
                        return(s)
                  s+=1


def db70ab10(letrs):
      num=0
      l=0
      n=''
      m=''
      o=0
      p=0
      q=0
      llave=0

      for n in letrs:  # proceso se hace escalonado de abajo hacia arriba, la llave 0
                   # multiplica el cociente por 5, la llave 1 le suma el ultimo cociente
                   # la llave 2 suma cocientes anteriores y multiplica por 70        

            l=int(codg70(num,n,2)) # cambio de codigo base 70 a base 10
            
            if llave==2:
                  p=l+(p*70) # multiplica por 70 operacion y suma resto hasta final de interación

            if llave==1: # suma el primer resto al proceso de la llave 0 durante la segunda iteracion
                  p= l+p
                  llave=2

            if llave==0: # multiplicar ultimo cociente por 70
                         # en la primera iteración
                  p=l*70
                  llave=1

              
      n=str(p)  

      return(n)            
            

def db10ab5(num):
      cif=int(num)
      llave=True
      n=''
      m=''
      o=''
      p=0
      
      while llave==True:
            p=cif%5
            cif=cif//5
            m=str(p)+m
            if cif<5:
                  m=str(cif)+m
                  llave=False

      return(m)



def db70ab5(num):
      
      num=db70ab10(num)
      return(db10ab5(num))
      

def animacion():   

      p=0
      q=0
      u=12
      s=''
      r=[]
      
      dib=('ak]7!u!2U','azjyyXii','afmU1J4i','bcQEEii','bcQnAPD','c9yO3W','c9yO3W','c9yO3W','akLKfE]ayQRb','akLKfE]dDm0S','akLKfE[]AuGN','akLKfE]al[aX','dZZp(CSNajN7')

      while p<13:
            if p==13:
                  break
            clear_console()
            r.append(p) # crea la figura que se crea en cada iteración
                        # dentro de la lista r
            q=12-p
            p=p+1

            print('\n\n\n')

            while q>0:
                  print('')
                  q=q-1
                  
            for s in r:
                  s=db70ab5(dib[s])
                  s=s.replace('4','').replace('3','y').replace('0',' ')
                  print('                                       '+s)


            time.sleep(0.000000007)

      time.sleep(0.7)
      
      print('\n\n                                       (Yogalidof 21 Proyect)')

      time.sleep(1)

      clear_console()



animacion()

print ('\n\n    This program is part of an altruistic work and challenges that I propose to myself.')
print ('    The altruistic part is that it makes life easier for other people.')
print ('    Achieving challenges is good for your health, it keeps your self-esteem strong.')
print ('    it is beneficial on two sides. I don`t know that little "be intelligently selfish"')
print ('    or the saying "helping others is helping oneself"\n\n')
print ('    It`s an open source type program, you can see the programming code and change it with a')
print ('    program to make programs, type IDLE. It is a way of providing transparency and that it is not infected\n\n')
print ('    If you like this program and want to know more curious things you can visit my channel \n    de youtube https://www.youtube.com/@yogalidof.21 ')
print ('    Also visit my page and read some free books on \n    https://www.calameo.com/accounts/1582946  \n\n')
print ('    Or my free open source programs page en https://github.com/y21-proyect')
print ('    Some important, my webs are in spanhis lenguaje')
print ('    You don`t need to give a like, I don`t live from this. Best regards \n\n    Doc \n\n\n    Press ENTER to continue...')
input('')


clear_console()



dividendo=19
divisor=1
cociente=0
resto=0
valor=''
valor2=0
txt=''

ciclo=0
llave=True
primos=[2,3,5,7,11,13,17,19]

resultado=''

print('This program will make a new txt document with the prime numbers')
txt=input('type the name for this new txt and press ENTER ')

txt=txt+'.txt'

valor=input('\nHow many prime numbers do you want inside? ')

valor2=int(valor)

print('making ',valor, 'prime numbers inside',txt)
print('I will advise you when it finish')


while ciclo<valor2:  #bucle buscador numeros primos
        
        if llave==True:
                
                #print('\nProceso divisiones usando lista de primos')
                
                for divisor in primos: # filtro de primos ya encontrados en lista
                        #print('ENTRADA',dividendo,divisor,cociente,resto, primos)
                        
                        cociente=dividendo//divisor
                        resto=dividendo%divisor

                        #print('DIVISIONES: ',dividendo,divisor,cociente,resto,primos)

                        
                        if resto==0:
                                #print('Multiplo de ',divisor)
                                dividendo+=2                               
                                break
                        
                if resto!=0:
                        llave=False
                        #print('\nProceso divisiones sin usar lista de primos')
                     
                       
        else:
                                
                #print('ENTRADA',dividendo,divisor,cociente,resto, primos)

                cociente=dividendo//divisor
                resto=dividendo%divisor

                #print('DIVISIONES: ',dividendo,divisor,cociente,resto,primos)
                               
                if resto==0 and cociente==1:
                        #print('# numero primo localizado',divisor)
                        primos.append(divisor)
                        llave=True
                        ciclo+=1
                        dividendo+=2


                else:
                        divisor+=2

with open(txt, 'a', encoding='utf-8') as txt:
        for divisor in primos:
                resultado=str(divisor)+'\n'
                txt.write(resultado)

print('\nProcess finished')

input()
