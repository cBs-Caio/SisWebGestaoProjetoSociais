# Arquitetura do MVP

O sistema apoia a equipe administrativa da Obra Social Dom Bosco de Itaquera no cadastro de participantes, no registro de inscrições e no acompanhamento da frequência.

- Python 3.12+ e Django 5.2 LTS sustentam o código da aplicação, a autenticação e o painel administrativo.
- PostgreSQL 14+ é o banco de referência. O ORM do Django define o esquema, e as migrações versionadas registram a evolução das tabelas.
- SQLite permite demonstrações e testes locais sem provisionamento de banco.

## Fluxo administrativo

1. Cadastrar o participante e o curso.
2. Criar uma inscrição que vincula os dois registros.
3. Registrar presença ou ausência por inscrição e data.

Uma pessoa pode se inscrever em vários cursos. Cada par de participante e curso admite uma inscrição. O MVP considera uma chamada por dia para cada inscrição. O banco protege essas duas regras com restrições de unicidade e preserva o histórico de registros vinculados com chaves estrangeiras protegidas no ORM.

O painel do Django atende a operação interna. Portal público, listas de espera e relatórios ficam fora do MVP. Use dados fictícios em demonstrações acadêmicas.

## Referências

- [Django 5.2](https://docs.djangoproject.com/en/5.2/releases/5.2/)
- [PostgreSQL no Django](https://docs.djangoproject.com/en/5.2/ref/databases/#postgresql-notes)
