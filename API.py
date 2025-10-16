import requests           # Biblioteca para fazer chamadas HTTP (GET, POST, etc)
import json               # Para salvar os dados como JSON em arquivo
import time               # Para fazer o script esperar entre requisições (sleep)

# Criamos uma classe para encapsular toda a lógica da SPTrans
class SPTransClient:
    def __init__(self, token):
        self.token = "84dfde66637e13d4307f9408fc4d5c36474c7dc322310ef71f264dda3fe75704"                  # O token da API fornecido pela SPTrans
        self.session = requests.Session()   # Cria uma sessão HTTP (mantém o cookie automaticamente)
        self.logged_in = False              # Flag para verificar se já fez login

# Método que faz o login na API usando o token
    def login(self):
        login_url = f"https://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={self.token}"
        response = self.session.post(login_url)  # Envia POST para autenticar

        # Se retornar 200 e a resposta for "true", login foi bem-sucedido
        if response.status_code == 200 and response.text.lower() == "true":
            print(" Login bem-sucedido.")
            self.logged_in = True
        else:
            # Caso contrário, exibe erro e marca como não logado
            print(f" Falha no login: {response.status_code} - {response.text}")
            self.logged_in = False

 # Método para buscar a posição dos ônibus
    def get_posicoes(self):
        # Se ainda não estiver logado, tenta logar
        if not self.logged_in:
            self.login()

        # Endpoint da API que traz a posição dos ônibus
        url = "https://api.olhovivo.sptrans.com.br/v2.1/Posicao"
        response = self.session.get(url)  # Envia GET com o cookie da sessão

        # Se o cookie tiver expirado, a API responde com 401
        if response.status_code == 401:
            print("Sessão expirada. Tentando relogar...")
            self.login()                    # Faz login novamente
            response = self.session.get(url)  # Reenvia a requisição

        # Se a resposta for 200, retorna os dados em JSON
        if response.status_code == 200:
            print(" Dados recebidos com sucesso.")
            return response.json()
        else:
            # Caso contrário, exibe erro
            print(f"Erro ao buscar posição: {response.status_code}")
            return None

# Bloco principal que executa o script em loop (near real-time)
if __name__ == "__main__":
    # Instancia o cliente com seu token da API
    client = SPTransClient(token="84dfde66637e13d4307f9408fc4d5c36474c7dc322310ef71f264dda3fe75704")

    # Loop infinito que roda a cada 2 minutos
    while True:
        dados = client.get_posicoes()  # Pega os dados da API
        if dados:
            # Salva os dados no arquivo local (usado pelo NiFi com GetFile, por exemplo)
            with open("posicao_onibus.json", "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
        
        # Espera 2 minutos antes de repetir (near real-time)
        time.sleep(120)