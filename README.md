Projeto_Final
Este projeto implementa um pipeline de ingestão de dados em tempo quase real (near real-time) utilizando Apache NiFi, com o objetivo de capturar, autenticar e armazenar informações do sistema de transporte público de São Paulo (SPTrans) e dos arquivos GTFS (dados estáticos de transporte).

A arquitetura foi projetada para coletar dados diretamente da API Olho Vivo, autenticar com o token da SPTrans, capturar posições e previsões de chegada dos ônibus e armazenar tudo na camada Bronze de um Data Lake hospedado no MinIO (S3).


1- Nifi

O fluxo **Projeto.json** contém os seguintes componentes principais:

**1.1 GET-API**

Tipo: **GenerateFlowFile**

Função: Inicia o pipeline, gerando um arquivo contendo o token de autenticação.

{ "token": "SEU_TOKEN_SPTRANS" }


Frequência: Executa a cada 1 minuto.

🔐 2. Autenticação-token

Tipo: InvokeHTTP

Descrição: Realiza a autenticação na API Olho Vivo com o token informado.

Método: POST

URL: https://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token=<TOKEN>

Saída esperada: Retorna true e gera o cookie de sessão (ASP.NET_SessionId).

🍪 3. CapturarCookie

Tipo: UpdateAttribute

Função: Extrai o cookie da resposta do Login e armazena em um atributo cookie_header.

Expressão:

${set-cookie:replaceAll('.*apiCredentials=([^;]+);.*','$1')}


Esse cookie será usado nas próximas requisições à API Olho Vivo.

📍 4. Capturar-dados-Posição

Tipo: InvokeHTTP

Descrição: Requisição à API Olho Vivo para obter a posição em tempo real dos veículos.

Método: GET

URL: https://api.olhovivo.sptrans.com.br/v2.1/Posicao

Header Dinâmico: Cookie: apiCredentials=${cookie_header}

Saída: JSON contendo informações sobre veículos, horários e coordenadas GPS.

📊 5. Ingestão-bronze (Posições)

Tipo: PutS3Object

Descrição: Armazena os dados de posição no bucket MinIO (raw/sptrans/posicoes/).

Endpoint: http://minio:9000

Chave do objeto:

sptrans/posicoes/${filename}

🕒 6. Capturar-Previsão-Chegada

Tipo: InvokeHTTP

Descrição: Consulta a API de previsão de chegada por parada.

Método: GET

URL:

https://api.olhovivo.sptrans.com.br/v2.1/Parada/Buscar?termosBusca=123458


Header Dinâmico: Cookie: apiCredentials=${cookie_header}

Saída: JSON com previsões de chegada para paradas e linhas específicas.

📥 7. Ingestão-bronze (Previsão)

Tipo: PutS3Object

Descrição: Armazena os dados de previsão no MinIO em:

sptrans/previsao/${filename}

🗂️ 8. GTFS-TXT e Ingestão-bronze (GTFS)

Tipo: GetFile + PutS3Object

Função: Faz ingestão dos arquivos GTFS (stops.txt, routes.txt, trips.txt, etc.) para o bucket raw/GTFS/Metadados/.

Permite correlacionar os dados estáticos de rotas e paradas com os dados dinâmicos da API Olho Vivo.

2-Spark

3-FastApi

4-Postgres

5-PowerBi
