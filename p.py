
import requests
import socket

def obter_localizacao_por_ip(ip):
    url = f"http://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def obter_nome_da_maquina(ip):
    try:
        nome, _, _ = socket.gethostbyaddr(ip)
        return nome
    except socket.herror:
        return "Nome da máquina não encontrado."

def main():
    # Insira aqui o IP que você deseja obter a localização e o nome da máquina
    ip = "8.8.8.8"  # Exemplo: Endereço IP do Google DNS

    localizacao = obter_localizacao_por_ip(ip)
    if localizacao:
        print("Informações de localização:")
        print(f"IP: {localizacao['ip']}")
        print(f"País: {localizacao['country']}")
        print(f"Região: {localizacao['region']}")
        print(f"Cidade: {localizacao['city']}")
        print(f"Latitude: {localizacao['loc'].split(',')[0]}")
        print(f"Longitude: {localizacao['loc'].split(',')[1]}")
    else:
        print("Não foi possível obter informações de localização.")

    nome_maquina = obter_nome_da_maquina(ip)
    print(f"Nome da máquina correspondente ao IP {ip}: {nome_maquina}")

if __name__ == "__main__":
    main()
