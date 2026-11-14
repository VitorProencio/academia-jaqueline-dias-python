# Sistema de Controle de Estoque — Academia de Dança Jaqueline Dias

Conversao do prototipo original PHP para **Python 3.12 + Django 5.2**, com interface inspirada no sistema original e arquivos CSS e imagens fornecidos no projeto. MVP academico: **Dashboard**, **Cadastro de Itens** e **Entrada de Mercadoria**. Nao inclui vendas, financeiro, saida de estoque ou historico de movimentacoes.

## Inicio rapido (Windows)

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/login/` e entre com o usuario criado. Para testes automatizados:

```powershell
coverage run manage.py test
coverage report
```

No Linux/macOS, use `python3 -m venv .venv` e `source .venv/bin/activate`.

## Banco de dados

Por padrao, usa **SQLite local** para permitir executar e testar sem configurar MySQL. Para **MySQL 8**, configure as variaveis `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_HOST`, `MYSQL_PORT` no ambiente antes de executar `migrate`. O esquema tem duas entidades de dominio: `categorias` e `produtos`. O Django cria tambem suas tabelas internas de autenticacao, sessoes e migracoes. **Nao aponte o projeto para o banco PHP existente sem backup e plano de migracao**, pois o esquema Django e o legado podem divergir.

## Funcionalidades

- Dashboard: lista produtos e indicadores para estoque zerado, baixo (1 a 9) e disponivel (10 ou mais).
- Cadastro: categoria e produto com custo/venda.
- Entrada: soma quantidades positivas com atualizacao atomica e campos opcionais de custo, venda e observacao.
- Autenticacao: login de usuarios Django e CSRF nos formularios.
- Testes: regras de status, consulta, cadastro, entrada e restricao de acesso.
- CI: GitHub Actions em push e pull request.

## Publicacao e evidencias

Crie um repositorio **publico** no GitHub, publique o codigo sem `db.sqlite3`, `.env` ou senhas, e capture um print da pagina inicial. Abra um Pull Request de uma branch de melhoria para documentar a revisao. Registre prints e resultados **reais** dos testes e do pipeline apos executa-los; a inclusao dos arquivos de testes e CI nao significa que ja foram executados.

## Observacoes

Este pacote e uma **primeira conversao de codigo**, nao uma copia executada e homologada do PHP. A interface preserva cores, logo e organizacao principal, mas nao e uma reproducao pixel a pixel. A imagem do produto e o botao de adicionar multiplos produtos do prototipo PHP nao foram incluidos nesta versao inicial. Antes de disponibilizar em producao, configurar seguranca, HTTPS, chave secreta, hospedagem, logs e backup.

## Objetivo do projeto

Sistema de controle de estoque desenvolvido para a Academia de Danca Jaqueline Dias.

## Funcionalidades do MVP

- Cadastro de categorias e produtos.
- Consulta de produtos e quantidades disponiveis.
- Registro de entrada de mercadorias.
- Identificacao de produtos com estoque baixo ou zerado.

## Tecnologias utilizadas

- Python 3
- Django 5
- MySQL
- HTML e CSS
- Bootstrap

## Controle de versao

O projeto utiliza Git para registrar a evolucao do codigo e GitHub para armazenar o repositorio remoto.
