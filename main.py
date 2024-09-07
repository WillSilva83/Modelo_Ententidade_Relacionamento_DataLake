from src.classes.Glue import Glue
from src.utils.logging import config_logger
from src.utils.external_libs import read_file, write_file

logger = config_logger('Aplicacao para Criar ER de uma base Athena')
client_glue = Glue()


def verify_relational_FK(table_name: str, relational_tables: dict) -> str:
    # Verifica se 'FK' está presente no dicionário da tabela
    if 'FK' in relational_tables[table_name]:
        fk_value = relational_tables[table_name]['FK']

        # Divide as múltiplas associações por '|'
        associations = fk_value.split(" | ")
        
        output = ""
        # Processa cada associação individualmente
        for association in associations:
            # Divide a associação em partes esquerda e direita
            left_part, right_part = association.split(" - ")
            
            # Separa tabela e coluna da parte esquerda e direita
            left_table, left_column = left_part.split(".")
            right_table, right_column = right_part.split(".")

            # Formata a string de saída para cada associação
            output += f'Ref: "{left_table}"."{left_column}" - "{right_table}"."{right_column}" \n'
        
        return output
    else: 
        return ""
     
def verify_relational_PK(table_name: str, column_name: str, relational_tables: dict) -> str:

    ## VERIFICAR A PK PRIMEIRO 

    if relational_tables[table_name]['PK'] == column_name:
        return "[primary key]"
    else:
        return ""
    
def prepare_diagram_pattern(dict_table, relational_tables: str):
    '''
        Funcao para criar no padrao do https://dbdiagram.io
    '''
    output = ""
    for table in dict_table:
        output += f'''\nTable {table}  {{ \n'''

        for column in dict_table[table]['Columns']:
            
            output += f'''    {column['Name']} {column['Type']} {verify_relational_PK(table, column['Name'], relational_tables)} \n''' 
        
        output += '''}\n\n'''
        
        output += verify_relational_FK(table, relational_tables)

    return output


if __name__ == '__main__':

    list_tables = client_glue.get_list_tables("database_test")

    er_diagram = {}

    for table in list_tables:
        table_name = table['Table_Name']
        columns = table['Columns']

        er_diagram[table_name] = {'Columns': []}

        for column in columns:
            column_info = {
                'Name': column['Name'],
                'Type': column['Type']
            }

            er_diagram[table_name]['Columns'].append(column_info)
    
        
    #er_diagram = {'table1_test': {'Columns': [{'Name': 'id', 'Type': 'bigint'}, {'Name': 'descritivo1', 'Type': 'string'}, {'Name': 'descritivo2', 'Type': 'string'}, {'Name': 'descritivo3', 'Type': 'string'}]}, 'table_test_2': {'Columns': [{'Name': 'id', 'Type': 'bigint'}, {'Name': 'id_table_1', 'Type': 'bigint'}, {'Name': 'descritivo1', 'Type': 'string'}, {'Name': 'descritivo2', 'Type': 'string'}, {'Name': 'descritivo3', 'Type': 'string'}, {'Name': 'descritivo4', 'Type': 'string'}, {'Name': 'descritivo5', 'Type': 'string'}]}}

    relational_tables = read_file("EXEMPLO_relational_tables.json")

    output = prepare_diagram_pattern(er_diagram, relational_tables)

    print(output)

    #write_file(output, "ER_EXEMPLO.json", True)
    

    




    
    
