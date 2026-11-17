# SisWebGestaoProjetoSociais

O projeto Sistema Web de Gestão de Projetos Sociais foi desenvolvido como proposta acadêmica para atender às necessidades administrativas da Obra Social Dom Bosco de Itaquera.

Consulte a [arquitetura do MVP](docs/arquitetura.md) para conhecer o fluxo de cadastro, inscrição e frequência.

## Executar localmente

Com Python 3.12 ou superior, crie e ative um ambiente virtual. No PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse [o painel administrativo](http://127.0.0.1:8000/admin/) e entre com a conta criada. Use dados fictícios na demonstração.

## Conectar ao PostgreSQL

Crie um banco vazio e uma conta com permissão para criar tabelas nele. Defina `POSTGRES_DB`, `POSTGRES_USER` e `POSTGRES_PASSWORD` no ambiente antes de rodar `migrate`. `POSTGRES_HOST` e `POSTGRES_PORT` assumem `localhost` e `5432`. Se `POSTGRES_DB` estiver ausente, a aplicação usa SQLite local.

As configurações padrão são para execução local. Para desativar a depuração, defina `DJANGO_DEBUG=0`, uma chave própria em `DJANGO_SECRET_KEY` e os hosts aceitos em `DJANGO_ALLOWED_HOSTS` separados por vírgula.

## Verificar

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

Cada pull request para a branch `main` executa essas verificações no GitHub Actions com PostgreSQL 16 temporário. A suíte usa um banco de teste criado pelo Django e as credenciais do workflow são exclusivas do ambiente descartável da execução.
