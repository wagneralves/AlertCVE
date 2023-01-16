# AlertCVE

The AlertCVE tool was developed through a need to work together with a team.

Authors:<br>
Wagner Alves - Red Team Analyst<br>
Pedro Ricardo - Blue Team Analyst

This tool scans the official cve.org Twitter account and monitors all new posts about CVEs, filtering what exists in your organization and notifying you in a telegram group with a personalized message and the link to the new CVE.
The tool also records a CSV file with the notification logs so that it can be consumed by a SIEM, soon we will send it to a syslog to automate this process

## Settings

Fill in the data in the variables as follows in the AlertCVE.py file:

Developer Account Bearer Token on Twitter

```
TwitterToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

Telegram bot token

```
TelegranToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

Telegram group ID that will receive the alerts, NOTE: starts with sign -

```
GroupTelegram = '-XXXXXXXXXX'
```

## Filtering the CVEs

Fill in or change the applications.json file including the technologies in your environment to only receive alerts that may require some technical analysis of correction in your environment, avoiding receiving unnecessary notifications.
Example:

```
{
	"Aplication": [
			"office",
			"firebird",
			"fortigate"
	]
}
```

to add a new technology put a comma at the end of the last one and write the name you want to filter between double quotes, as an example we will add the apache web server:

```
{
	"Aplication": [
			"office",
			"firebird",
			"fortigate",
            "Apache"
	]
}
```

## Installation

```
git clone https://github.com/wagneralves/AlertCVE.git
cd AlertCVE
pip3 install -r requirements.txt
```


## Usage

```
python3 AlertCVE.py
```


<div align="center">
<img src="https://user-images.githubusercontent.com/5523049/212672624-07337a13-ea88-42e3-b64d-c781e2ddceb4.png" width="1080px" />
</div>
<br>

<div align="center">
<img src="https://user-images.githubusercontent.com/5523049/212563819-18045cbe-1422-4794-a29d-0683f3c2f20d.png" width="320px" />
</div>

## Control file

The controle.txt file exists to store the id of the last tweet consulted to avoid receiving CVE alerts twice

## LOG file

The logs_to_siem.csv file keeps every CVE log that was alerted to be imported by SIEM, we will soon send it via SYSLOG.
