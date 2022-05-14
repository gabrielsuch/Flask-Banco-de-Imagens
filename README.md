# Banco de Imagens


Rubrica - E6 - Banco de imagens

| Critérios	| Descrição | Pts |
|---|---|---|
| POST /upload JPG - 201 | Subir a imagem JPG menor que 1MB para o sistema e retornar uma mensagem de sucesso e status code 201. | 1.0 pts |
|POST /upload - Nome de arquivo ja existente - 409|  Ao tentar subir uma imagem com um nome ja existente no sistema, retornar uma mensagem de error e status code 409.| 1.0 pts|
|POST /upload GIF - 201| Subir a imagem GIF menor que 1MB para o sistema e retornar uma mensagem de sucesso e status code 201.|1.0 pts| 
|POST /upload PNG - 201| Subir a imagem PNG menor que 1MB para o sistema e retornar uma mensagem de sucesso e status code 201.|1.0 pts |
|POST /upload - Extensão não suportada - 415|Ao tentar subir um tipo de arquivo não suportado pelo sistema, retornar uma mensagem de error e status code 415.|1.0 pts|
|POST /upload - Arquivo maior que 1MB - 413|Ao tentar subir um arquivo com tamanho maior que 1MB, retornar uma mensagem de error e status code 413.|1.0 pts|
|GET /files - 200|Retornar uma lista com o nome de todas as imagens salvas no sistema, com o status code 200.|1.0 pts|
|GET /files/jpg - 200|Retornar uma lista com o nome de todas as imagens JPG salvas no sistema, com o status code 200.|1.0 pts|
|GET /files/png - 200|Retornar uma lista com o nome de todas as imagens PNG salvas no sistema, com o status code 200.|1.0 pts|
|GET /files/gif - 200|Retornar uma lista com o nome de todas as imagens GIF salvas no sistema, com o status code 200.|1.0 pts|
|GET /files/<formato-invalido> - 404|Ao tentar acessar a rota com um formato de arquivo não permitido pelo sistema, retornar uma mensagem de error e status code 404.|1.0 pts|
|GET /download/<name.extension> - 200|Fazer o download de uma imagem pelo seu nome, retornando o download da imagem e status code 200. Deve funcionar para os 3 formatos válidos.|3.0 pts|
|GET /download/<name.extension> - Nome de arquivo inválido - 404|Ao tentar fazer o download de um arquivo com nome não encontrado no sistema, retornar mensagem de error e status code 404.|1.0 pts|
|GET /download-zip?<query_params> - 200|Deverá fazer o download da extensão passada por query params em formato zip.|1.0 pts|
|GET /download-zip?<query_params> - Arquivo não existente - 404|Se o diretório do tipo de extensão passado por query_params estiver vazio, ou se o tipo de arquivo não existir, retornar uma mensagem de error e status code 404.|1.0 pts|
|Alteração no .env no nome do diretório|Ao executar, criar o diretório a ser utilizado para salvamento das imagens.|1.0 pts|
|Análise do código|Organização dos módulos e pacotes, boas práticas.|1.0 pts|
|Arquivos requirements.txt, .env.example e .gitignore.| |1.0 pts
| | | Total de pontos: 20.0
