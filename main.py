#██╗   ██╗██████╗ ██╗███████╗██╗      ███████╗ █████╗ 
#██║   ██║██╔══██╗██║██╔════╝██║      ██╔════╝██╔══██╗
#██║   ██║██████╔╝██║█████╗  ██║      ███████╗███████║
#██║   ██║██╔══██╗██║██╔══╝  ██║      ╚════██║██╔══██║
#╚██████╔╝██║  ██║██║███████╗███████╗███████║ ██║  ██║
 #╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝ ╚═╝  ╚═╝

class pruebapy:
    
    def __init__(self, prueba, py):
        self.prueba = prueba
        self.py = py
        
p1 = pruebapy("Hola esto es una prueba en python", "Text 1")
p2 = pruebapy("Text 2", "Hola soy la prueba de python")
        
print(p1.prueba)
print(p2.py)

class pruebapy2:
    
    def __init__(self, prueba2, py2):
       self.prueba2 = prueba2
       self.py2 = py2
    
p3 = pruebapy2("Hola soy el segundo def", "Text 3")
p4 = pruebapy2("Text 4", "Soy el segundo nuevamente")

print(p3.prueba2)
print(p4.py2)

class pruebapy3:
    
    def __init__(self, prueba3, py3, github):
        self.prueba3 = prueba3
        self.py3 = py3
        self.github = github

p5 = pruebapy3("Hola soy el tercer def", "Text 5", "primer self")
p6 = pruebapy3("Text 6", "Soy el tercero nuevamente", "segundo self")
p7 = pruebapy3("Text 7", "tercer self", "Hola este pequeño proyecto basico aprendiz ira a mi Github, https://github.com/lilbossgrim-dev")

print(p5.prueba3)
print(p6.py3)
print(p7.github)
