from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

@app.route("/")
def index ():
    return render_template ("index.html")

@app.route("/index.html" , methods=['POST'])
def cal_imc():
     nome = request.form ["nome"]
     peso = float (request.form ["peso"])
     altura = float ( request.form ["altura"])

     imc = peso / (altura ** 2)
     caminho_arquivo = 'models/notas.txt'

     with open(caminho_arquivo, 'a' ) as arquivo:
        arquivo.write(f"{nome};{peso};{altura};{imc}\n")
    
     return redirect("/")

@app.route("/consultar")
def consultar():
    registros = []
    caminho_arquivo = 'models/notas.txt'
 
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            if len(item) == 4:
                registros.append({
                'nome': item [0],
                'peso': item [1],
                'altura': item [2],
                'imc': item [3]       
         })
    return render_template("consultar.html" , prod=registros)
                
@app.route('/excluir_registros', methods=['POST'])
def excluir_registros():
    linha = request.form.get('linha')

    
    return redirect(url_for('consultar.html')) 


app.run(host='127.0.0.1', port=80, debug=True)