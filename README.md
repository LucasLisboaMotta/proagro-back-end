# Proagro Back-End


Este projeto é o back-end deste repositório https://github.com/LucasLisboaMotta/proagro-front-end


Este foi o meu primeiro projeto em Phyton, o intuito era criar um back-end de uma aplicação que visa  criar os cadastros de pedidos dos produtores rurais de obrigações financeiras relativas a operações de crédito, em caso de  ocorrência de perdas nas lavouras.

Para inciar o projeto, você precisa do MySQL, é necessário configurar o arquivo `proagro/settings.py` na linha 82, a variavel DATABASES com as configurações do MySQL. 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proagro',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
Além disso, também é necessário criar uma database no banco de dados, você pode criar usando o comando
```
CREATE DATABASE proagro
```
em seguida, você  devera utilizar os  seguintes comandos para iniciar o servidor
```
python3 -m venv env
source env/bin/activate 
pip3 install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Apos esses comandos, o servidor devera iniciar na porta 8000

Na API deste projeto, possui uma única rota chamada `"exemptionrequests/"`

Nela permite o cadastro, leitura, edição e exclusão dos objetos salvos no banco de dados.

Esse objeto tem o seguinte formato:
```
{
  id, // string gerada automaticamente
  name, // string de no mínimo 10 caracteres
  email , // string de e-mail em formato valido
  date,  // uma data valida
  cpf, // string de exatos 11 caracteres
  latitude_location, // numero
  longitude_location, // numero
  event,  // string, apenas uma das opções: ['CHUVA EXCESSIVA',  'GEADA',  'GRANIZO',  'SECA',  'VENDAVAL',  'RAIO']
  create_at, //= data de criação do objeto, gerado automaticamente
  crop, // string, de no minimo 3 caracteres
}
```
