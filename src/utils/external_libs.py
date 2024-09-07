import json 
import re
from src.utils.logging import config_logger

logger = config_logger('Log config do External Libs')


def write_file(data, file_name = "file_output.json", is_json = False, encoding = 'utf-8', indent = 4):
    ''' Save file '''
    try:
        with open(file_name, 'w', encoding=encoding) as file:
            if is_json:
                json.dump(data, file, indent=indent)
            else: 
                file.write(data)
                

    except Exception as e:
        print(f"Erro ao salvar JSON no arquivo. Erro: {e}")
    pass 

def validate_string(str_data) -> bool:  
    ''' validar se possui formato YYYY-MM-DD '''
    pattern_1 = r'dt_arq|anomes|process_date|dt_incl'
    pattern_2 = r'\w=\d{2}'
    
    return bool(re.search(pattern_1, str_data) or re.search(pattern_2, str_data))

def read_file(path: str):
    ''' Read a File from a path '''
    try: 
        with open(path, 'r') as file: 
            return json.load(file)



    except Exception as e: 
        print(f"Erro ao ler o arquivo. Erro: {e}")

def process_json_table_list(list_response: dict) -> list:

    '''
    
    '''
    
    output_list = []
    

    for item in list_response:
        dict_itens = {}

        table_name = item["Table"]

        dict_itens['Table_Name'] = table_name['Name']

        try:
        
            if not table_name["StorageDescriptor"]["Location"].endswith('/'):
                table_name["StorageDescriptor"]["Location"] += '/'
            
            
            dict_itens["Location"]  = table_name["StorageDescriptor"]["Location"]
            dict_itens["TableType"] = table_name["TableType"]
            dict_itens["Columns"]   = table_name['StorageDescriptor']['Columns']
            
            output_list.append(dict_itens)

        except Exception as e:
            logger.warning("Tabela " + table_name["Name"] + " não foi adicionada.")     
            dict_itens["Table_Error"] = table_name["Name"]
            dict_itens["Location"] = ""
            dict_itens["Columns"] = []
            dict_itens["IsVerify"] = False
            output_list.append(dict_itens)

    return output_list

def prepare_list_from_json(path_json: str) -> list:

    ''' Prepara uma lista a partir do json de configuracao '''

    output_list = []
    
    file_data = read_file(path_json)

    for table_name, table_data in file_data.items():
        output_list.append(table_name)

    return output_list