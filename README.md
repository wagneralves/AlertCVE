# AlertCVE

Preencha os dados nas variáveis da seguinte forma no arquivo AlertCVE.py:

Bearer Token da conta de desenvolvedor no Twitter
TwitterToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

Token do bot do Telegran
TelegranToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'

ID do grupo do Telegram que receberá os alertas, OBS: começa com sinal de -
GrupoTelegram = '-XXXXXXXXXX'

# Filtrando as CVEs

Preencha ou altere o arquivo applications.json incluindo as tecnologias do seu ambiente para receber alertas apenas que possam demandar alguma análise técnica de correção em seu ambiente evitando receber notificações desnecessárias.
Exemplo:

{
	"Aplication": [
			"office",
			"firebird",
			"fortigate"
	]
}

para adicionar uma nova rtecnologia coloca uma vírgula ao final da ultima e escreve entre aspas duplas o nome que deseja filtrar, como exemplo adicionaremos o servidor web apache:

{
	"Aplication": [
			"office",
			"firebird",
			"fortigate",
            "Apache"
	]
}

# Instalação

pip install -r requirements.txt

# Utilização

python3 AlertCVE.py

<div align="center">
<img src="https://user-images.githubusercontent.com/5523049/212563819-18045cbe-1422-4794-a29d-0683f3c2f20d.png" width="320px" />
</div>

# Arquivo de controle

O arquivo controle.txt existe para guardar o id do último tweet consultado para evitar receber em duplicidade os alertas de CVEs

# Arquivo de LOG

O arquivo logs_to_siem.csv guarda todo log de CVE que foi alertada para ser importado pelo SIEM, em breve faremos um envio via SYSLOG.