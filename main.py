import sys
from src.classes.Glue import Glue
from src.utils.logging import config_logger
from src.utils.external_libs import read_file, write_file, process_json_table_list, prepare_list_from_json

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

    '''
        PROCESSA DIAGRAMA DE ENTIDADE E RELACIONAMENTO
    '''

    if len(sys.argv) < 4:
        logger.error("Faltam parametros para execucao do script.")
        sys.exit(1)

    
    ## Argumentos

    database = sys.argv[1]
    path_json = sys.argv[2]
    output_file = sys.argv[3]


    list_tables = prepare_list_from_json(path_json) 

    dict_list_tables = client_glue.get_table(database, list_tables)

    tables = process_json_table_list(dict_list_tables)

    er_diagram = {}

    ## Prepara para gerar o ER.

    for table in tables:

        table_name = table['Table_Name']
        columns = table['Columns']

        er_diagram[table_name] = {'Columns': []}

        for column in columns:
            column_info = {
                'Name': column['Name'],
                'Type': column['Type']
            }

            er_diagram[table_name]['Columns'].append(column_info)
    


    relational_tables = read_file(path_json)

    output = prepare_diagram_pattern(er_diagram, relational_tables)

    write_file(output, output_file, False)
