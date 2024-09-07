from src.classes.Glue import Glue
from src.utils.logging import config_logger


logger = config_logger('Aplicacao para Criar ER de uma base Athena')
client_glue = Glue()



def prepare_diagram_pattern(dict_table):
    
    for table in dict_table:
        output = f'''Table {table}  {{ \n'''

        for column in dict_table[table]['Columns']:
            output += f'''    {column} string \n''' 
        
        output += '''}\n''' 

        print(output)  
    
    pass





if __name__ == '__main__':

    # list_tables = client_glue.get_list_tables("database_test")

    # er_diagram = {}

    # for table in list_tables:
    #     table_name = table['Table_Name']
    #     columns = table['Columns']

    #     er_diagram[table_name] = {'Columns': []}
    #     for column in columns:
    #         er_diagram[table_name]['Columns'].append(column['Name'])

    # print(er_diagram)

    dict_tables = {'table1_test': {'Columns': ['id', 'descritivo1', 'descritivo2', 'descritivo3']}, 'table_test_2': {'Columns': []}}

    prepare_diagram_pattern(dict_tables)
    

