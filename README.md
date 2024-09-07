# Projeto do Modelo Ententidade Relacionamento 


Aplicação para gerar o modelo de entidade relacionamento com base em um database. 


```
Exemplo de Chamada 

python3 main.py "database" "EXEMPLO_relational_tables.json" "ER_EXEMPLO_20240907.txt"
```

database    - Corresponde ao Database no Amazon Glue. 

.json       - Corresponde ao Arquivo de configuração do JSON 



## Arquivo de Configuração JSON 

É apenas necessário explicitar apenas o nome da tabela que existe no 

```json
Exemplo de JSON 

{
    "NOME_TABELA_1": {
        "PK" : "id"

    },

    "NOME_TABELA_2" :{
        "PK" : "id",
        "FK" : "NOME_TABELA_1.ID_TABELA_1 - NOME_TABELA_2.ID_TABELA_1"
    },

    "NOME_TABELA_3" : {
        "PK" : "id",
        "FK" : "NOME_TABELA_1.ID_TABELA_1 - NOME_TABELA_3.ID_TABELA_1 | NOME_TABELA_2.ID_TABELA_2 - NOME_TABELA_3.ID_TABELA_2"
    }
}
```

### Pontos de Atenção sobre as Chaves

PK  - Corresponde a Primary Key da tabela. 

FK  - Corresponde ao relacionamento entre tabelas. 

"-" - Corresponde ao relacionamento da tabela, inicialmente apenas 1:1 está sendo esperado. 

"|" - Corresponde a separação de relacionamentos entre tabelas.

