from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def getNomeEmails ():
    nomes = []
    emails = []
    dados = []

    with open ('emails.csv', 'r' , encoding='utf8') as arquivo:
        for info in arquivo:
            dados.append(info.replace('\n','',).split())
        
    for item in dados:
        nomes.append(item[0].replace(',',''))
        emails.append(item[1])
    
    return nomes, emails

def getTemplate()
    
    with open('template.txt','r', encoding='utf8') as arquivo:
        template = arquivo.read()
        return Template (template)


def conect(nomes, emails, template):
    s = smtplib.SMTP(host='meu host', port='minha porta')
    s.starttlsr()
    s.login('seu email','senha')

    for nome, email in zip(nomes, emails):
        msg = MIMEMultipart()

        mensagem = template.substitute(nome_pessoa = nome.title())

    #configurando setup
        msg['From'] = 'seu email'
        msg['To'] = email
        msg['Subject'] = 'mensagem de titulo'

        msg.attach(MIMEText(mensagem, 'plain'))

        s.send_message(msg)



# conect(getNomeEmails()[0], getNomeEmails()[1], getTemplate())

        


getNomeEmails()
