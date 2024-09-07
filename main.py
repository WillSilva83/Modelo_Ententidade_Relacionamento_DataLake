from src.classes.Glue import Glue
from src.utils.logging import config_logger


logger = config_logger('Aplicacao para Criar ER de uma base Athena')
client_glue = Glue()



def prepare_diagram_pattern(dict_table):
    '''
        Funcao para criar no padrao do https://dbdiagram.io
    '''
    for table in dict_table:
        output = f'''Table {table}  {{ \n'''

        for column in dict_table[table]['Columns']:
            
            output += f'''    {column['Name']} {column['Type']} \n''' 
        
        output += '''}\n''' 

        print(output)  
    pass



if __name__ == '__main__':

    #list_tables = client_glue.get_list_tables("database_test")

    # er_diagram = {}

    # for table in list_tables:
    #     table_name = table['Table_Name']
    #     columns = table['Columns']

    #     er_diagram[table_name] = {'Columns': []}

    #     for column in columns:
    #         column_info = {
    #             'Name': column['Name'],
    #             'Type': column['Type']
    #         }

    #         er_diagram[table_name]['Columns'].append(column_info)

    #print(er_diagram)
    
        
    er_diagram = {'table1_test': {'Columns': [{'Name': 'id', 'Type': 'bigint'}, {'Name': 'descritivo1', 'Type': 'string'}, {'Name': 'descritivo2', 'Type': 'string'}, {'Name': 'descritivo3', 'Type': 'string'}]}, 'table_test_2': {'Columns': [{'Name': 'id', 'Type': 'bigint'}, {'Name': 'id_table_1', 'Type': 'bigint'}, {'Name': 'descritivo1', 'Type': 'string'}, {'Name': 'descritivo2', 'Type': 'string'}, {'Name': 'descritivo3', 'Type': 'string'}, {'Name': 'descritivo4', 'Type': 'string'}, {'Name': 'descritivo5', 'Type': 'string'}]}}

    prepare_diagram_pattern(er_diagram)
    
