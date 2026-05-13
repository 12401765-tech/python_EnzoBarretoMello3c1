from flask import Flask

app = Flask(__name__)

@app.route("/")
def curriculo():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meu Currículo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: 30px auto;
                background: #fff;
                padding: 40px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                border-radius: 8px;
            }
            header {
                border-bottom: 2px solid #0056b3;
                padding-bottom: 20px;
                margin-bottom: 25px;
            }
            h1 {
                margin: 0;
                color: #0056b3;
                font-size: 28px;
            }
            h2 {
                color: #0056b3;
                border-bottom: 1px solid #ddd;
                padding-bottom: 5px;
                font-size: 20px;
                margin-top: 25px;
            }
            .contato {
                font-size: 14px;
                color: #666;
                margin-top: 5px;
            }
            .item {
                margin-bottom: 15px;
            }
            .item-titulo {
                font-weight: bold;
                color: #111;
            }
            .item-subtitulo {
                font-style: italic;
                color: #555;
                font-size: 14px;
            }
            .lista-habilidades {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
                padding-left: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Enzo Barrêto Mello</h1>
                <div class="contato">
                    Desenvolvedor | Belo Horizonte - Minas Gerais<br>
                    Telefone: (31) 99500-9963 | Email: enzobarreto.mello@gmail.com<br>
                    LinkedIn: linkedin.com | GitHub: github.com
                </div>
            </header>

            <section>
                <h2>Objetivo Profissional</h2>
                <p>Breve resumo de uma ou duas linhas sobre seus objetivos de carreira e como você pretende contribuir para a empresa que está se candidatando.</p>
            </section>

            <section>
                <h2>Experiência Profissional</h2>
                
                <div class="item">
                    <div class="item-titulo">Nome do Cargo / Função</div>
                    <div class="item-subtitulo">Nome da Empresa | Mês/Ano de Início – Mês/Ano de Término (ou Atual)</div>
                    <ul>
                        <li>Descrição das suas responsabilidades diárias no cargo.</li>
                        <li>Destaque para conquistas e resultados quantificáveis.</li>
                        <li>Ferramentas ou tecnologias utilizadas no cotidiano.</li>
                    </ul>
                </div>

                <div class="item">
                    <div class="item-titulo">Nome do Cargo Anterior</div>
                    <div class="item-subtitulo">Nome da Empresa | Mês/Ano de Início – Mês/Ano de Término</div>
                    <ul>
                        <li>Principais atividades desenvolvidas na função.</li>
                        <li>Projetos em que colaborou ativamente.</li>
                    </ul>
                </div>
            </section>

            <section>
                <h2>Formação Acadêmica</h2>
                
                <div class="item">
                    <div class="item-titulo">Nome do Curso / Graduação</div>
                    <div class="item-subtitulo">Nome da Instituição de Ensino | Ano de Conclusão: 202X</div>
                </div>
            </section>

            <section>
                <h2>Habilidades Técnicas e Competências</h2>
                <ul class="lista-habilidades">
                    <li>Habilidade / Tecnologia 1</li>
                    <li>Habilidade / Tecnologia 2</li>
                    <li>Habilidade / Tecnologia 3</li>
                    <li>Habilidade / Tecnologia 4</li>
                </ul>
            </section>

            <section>
                <h2>Idiomas</h2>
                <ul>
                    <li>Português – Nativo</li>
                    <li>Inglês – Nível de fluência (Ex: Intermediário, Avançado, Fluente)</li>
                </ul>
            </section>
        </div>

    </body>
    </html>"""

if __name__ == '__main__':
    app.run(debug=True)


