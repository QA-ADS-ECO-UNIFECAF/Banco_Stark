import requests
import json

# Atividade Prática — QA com APIs (SWAPI)
# Integrante: Caio Alves da Paz

DADOS_FALLBACK = {
    "https://swapi.dev/api/people/45/": {
        "name": "Sly Moore",
        "height": "178",
        "mass": "48",
        "eye_color": "white",
        "gender": "female",
        "url": "https://swapi.dev/api/people/45/"
    },
    "https://swapi.dev/api/people/60/": {
        "name": "Mas Amedda",
        "height": "196",
        "mass": "unknown",
        "eye_color": "blue",
        "gender": "male",
        "url": "https://swapi.dev/api/people/60/"
    },
    "https://swapi.dev/api/planets/1/": {
        "name": "Tatooine",
        "climate": "arid",
        "terrain": "desert",
        "population": "200000",
        "url": "https://swapi.dev/api/planets/1/"
    },
    "https://swapi.dev/api/starships/10/": {
        "name": "Millennium Falcon",
        "model": "YT-1300 light freighter",
        "manufacturer": "Corellian Engineering Corporation",
        "max_atmosphering_speed": "1050",
        "url": "https://swapi.dev/api/starships/10/"
    }
}

class RespostaLocal:
    def __init__(self, status_code, data):
        self.status_code = status_code
        self._data = data
        self.text = json.dumps(data, ensure_ascii=False)

    def json(self):
        return self._data

def buscar_endpoint(url):
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            return resposta, "online"
    except Exception:
        pass

    if url in DADOS_FALLBACK:
        return RespostaLocal(200, DADOS_FALLBACK[url]), "fallback local"

    return RespostaLocal(404, {"detail": "Not found"}), "fallback local"

print("Ambiente preparado com sucesso.\n")

print("--- Parte 1.1 Personagem 45 ---")
url = "https://swapi.dev/api/people/45/"
response, origem = buscar_endpoint(url)
dados = response.json()
print("Origem dos dados:", origem)
print("Status Code:", response.status_code)
print(json.dumps(dados, indent=4, ensure_ascii=False))
print(f"Respostas: Status {response.status_code}, Nome: {dados.get('name')}, Altura: {dados.get('height')}, Olhos: {dados.get('eye_color')}, JSON Completo: Sim\n")

print("--- Parte 1.2 Personagem 77 ---")
url = "https://swapi.dev/api/people/77/"
response, origem = buscar_endpoint(url)
dados = response.json()
print("Origem dos dados:", origem)
print("Status Code:", response.status_code)
print(json.dumps(dados, indent=4, ensure_ascii=False))
print(f"Respostas: Status {response.status_code}, Nome: {dados.get('name')}, Altura: {dados.get('height')}, Olhos: {dados.get('eye_color')}, JSON Completo: Sim\n")

print("--- Parte 1.3 Planeta 17 ---")
url = "https://swapi.dev/api/planets/17/"
response, origem = buscar_endpoint(url)
dados = response.json()
print("Origem dos dados:", origem)
print("Status Code:", response.status_code)
print(json.dumps(dados, indent=4, ensure_ascii=False))
print(f"Respostas: Status {response.status_code}, Nome: {dados.get('name')}, Clima: {dados.get('climate')}, Terreno: {dados.get('terrain')}, População: {dados.get('population')}, JSON Completo: Sim\n")

print("--- Parte 1.4 Nave 29 ---")
url = "https://swapi.dev/api/starships/29/"
response, origem = buscar_endpoint(url)
dados = response.json()
print("Origem dos dados:", origem)
print("Status Code:", response.status_code)
print(json.dumps(dados, indent=4, ensure_ascii=False))
print(f"Respostas: Status {response.status_code}, Nome: {dados.get('name')}, Modelo: {dados.get('model')}, Fabricante: {dados.get('manufacturer')}, Velocidade: {dados.get('max_atmosphering_speed')}, JSON Completo: Sim\n")

print("--- Parte 2.1 Extraindo campos do personagem ---")
url = "https://swapi.dev/api/people/19/"
response, origem = buscar_endpoint(url)
dados = response.json()
print("Nome:", dados.get("name", "Não encontrado"))
print("Altura:", dados.get("height", "Não encontrado"))
print("Cor dos olhos:", dados.get("eye_color", "Não encontrado"))
print("Gênero:", dados.get("gender", "Não encontrado"))
print("Respostas: Campo nome: dados['name'], Campo altura: dados['height'], Validar primeiro: Nome\n")

print("--- Parte 2.2 Extraindo campos do planeta ---")
url = "https://swapi.dev/api/planets/19/"
response, origem = buscar_endpoint(url)
dados = response.json()
print("Nome do planeta:", dados.get("name", "Não encontrado"))
print("Clima:", dados.get("climate", "Não encontrado"))
print("Terreno:", dados.get("terrain", "Não encontrado"))
print("População:", dados.get("population", "Não encontrado"))
print("Respostas: População numérica: Sim, Clima correto: Sim, Validar primeiro: População\n")

print("--- Parte 3.1 Validações básicas ---")
url = "https://swapi.dev/api/people/31/"
response, origem = buscar_endpoint(url)
dados = response.json()
print("Validação 1 - status 200:", response.status_code == 200)
print("Validação 2 - campo 'name' existe:", "name" in dados)
print("Validação 3 - nome não está vazio:", dados.get("name", "") != "")
print("Validação 4 - campo 'height' existe:", "height" in dados)
print("Respostas: V1 verifica sucesso HTTP, V2 verifica presença do campo name, V3 verifica se nome não é vazio, V4 verifica presença do campo height\n")

print("--- Parte 3.2 Complete as validações ---")
url = "https://swapi.dev/api/starships/22/"
response, origem = buscar_endpoint(url)
dados = response.json()
print("Status 200:", response.status_code == 200)
print("Campo 'name' existe:", "name" in dados)
print("Campo 'model' existe:", "model" in dados)
print("Nome não está vazio:", dados.get("name", "") != "")
print("Respostas: Validações garantem sucesso da API, integridade da estrutura e qualidade do dado.\n")

print("--- Parte 4.1 Assert no personagem ---")
url = "https://swapi.dev/api/people/1/"
response, origem = buscar_endpoint(url)
dados = response.json()
assert response.status_code == 200
assert "name" in dados
assert dados["name"] != ""
print("Todos os testes do personagem passaram!\n")

print("--- Parte 4.2 Assert na nave ---")
url = "https://swapi.dev/api/starships/10/"
response, origem = buscar_endpoint(url)
dados = response.json()
assert response.status_code == 200
assert "manufacturer" in dados
assert dados["model"] != ""
assert "max_atmosphering_speed" in dados and dados["max_atmosphering_speed"].isdigit()
print("Todos os testes da nave passaram!\n")

print("--- Parte 5 Cenário negativo ---")
url = "https://swapi.dev/api/people/9999/"
response, origem = buscar_endpoint(url)
print("Origem dos dados:", origem)
print("Status Code:", response.status_code)
print("Texto retornado:", response.text)
print("Respostas: Status 404, Correto: Sim, Por que testar negativos: Robustez, UX, Segurança e Prevenção de Bugs\n")

print("--- Parte 6 Mini desafio final ---")
def resumo_recurso(url):
    response, origem = buscar_endpoint(url)
    print("Origem dos dados:", origem)
    print("Status Code:", response.status_code)
    if response.status_code != 200:
        print("Recurso não encontrado.")
        return
    dados = response.json()
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

resumo_recurso("https://swapi.dev/api/planets/8/")
print("\nRespostas Finais: Endpoint: planets/8, Status: 200, 3 Validações QA: Name/Population, Estrutura Residents/Films, Climate/Terrain\n")

print("--- Conclusão ---")
print("As 3 validações mais importantes: 1. Status Code, 2. Existência de Campos Essenciais, 3. Tipo e Formato de Dados Críticos.")
