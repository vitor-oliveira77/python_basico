# try e except : código especifico para identificar erros e mudar ações. 
# Funciona mais rapido que if e else 
#try: tentar executar o código
#except: ocorreu algum erro ao executar 

numero_str = input( 
    'vou dobrar o número que você digitar:'

) 

try: 
    numero_float = float(numero_str) 
    print('Float:', {numero_str} é {numero_float * 2:})
except:
    print('Isso não é um número')

