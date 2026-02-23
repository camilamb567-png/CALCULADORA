from flask import Flask,request

app= Flask(__name__)

@app.route("/")
def home():
 import random
 a= random.randint(1,100)
 b= random.randint(1,100)
 
 return f'''




<h1> Aplicación Calculadora </h1>

<p> Opciones disponibles: </p>

<ul>

    <li><a href="/suma?a={a}&b={b}"> suma </a></li>  
    <li><a href="/resta?a={a}&b={b}"> resta  </a></li>
    <li><a href="/multiplicacion?a={a}&b={b}"> multiplicacion </a></li>
    <li><a href="/division?a={a}&b={b}"> division </a></li>
    <li><a href="/division_piso?a=10&b=5">División Piso</a></li>
   
    
    

  
 
</ul>

'''
#Esta es la ruta adicional en la aplicación


@app.route("/suma")
def ruta_suma():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado = a + b

    return f'''
    La suma de {a} y {b} es: {resultado}
    <br><br>
    <a href="/">Volver al Home</a>
    '''

@app.route("/resta")
def ruta_resta():
    a= request.args.get("a", type=float)
    b= request.args.get("b", type=float)
    resultado= a - b
    return f'''
    La resta de {a} y {b} es: {resultado}
    <br><br>
    <a href="/">Volver al Home</a>
    '''

@app.route("/multiplicacion")
def ruta_multiplicacion():
    a= request.args.get("a", type=float)
    b= request.args.get("b", type=float)
    resultado= a * b
    return f'''
    La multiplicación de {a} y {b} es: {resultado}
    <br><br>
    <a href="/">Volver al Home</a>
    '''


    


@app.route("/division")
def ruta_division():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado = a/b

    return f'''
    La división de {a} y {b} es: {resultado}
    <br><br>
    <a href="/">Volver al Home</a>
    '''

@app.route("/division_piso")
def ruta_division_piso():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado = a//b

    return f'''
    La división piso de {a} y {b} es: {resultado}
    <br><br>
    <a href="/">Volver al Home</a>
    '''

#esto nos permite actualizar rapidamente los cambios sin tener que reiniciar el servidor cada vez que hagamos una modificación en el código

if __name__ =="__main__":
    app.run(debug=True)

   