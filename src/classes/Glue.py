import boto3 
from src.utils.logging import config_logger

logger = config_logger('App Tables S3 X Athena')


def process_json_table_list(tables_list_response: dict) -> list:
    '''
    
    '''
    
    output_list = []

    for table in tables_list_response:
        dict_itens = {}
        
        try: 
        
            dict_itens["Table_Name"] = table["Name"]
            
            # Adicionado para padronizar
            if not table["StorageDescriptor"]["Location"].endswith('/'):
                table["StorageDescriptor"]["Location"] += '/'
            
            dict_itens["Location"] = table["StorageDescriptor"]["Location"]
            dict_itens["TableType"] = table["TableType"]
            dict_itens["Columns"] = table['StorageDescriptor']['Columns']
            dict_itens["IsVerify"] = False
            
            output_list.append(dict_itens)
        
        except Exception as e: 
            logger.warning("Tabela " + table["Name"] + " não foi adicionada.")     
            dict_itens["Table_Error"] = table["Name"]
            dict_itens["Location"] = ""
            dict_itens["Columns"] = []
            dict_itens["IsVerify"] = False
            output_list.append(dict_itens)

    return output_list

class Glue():
    def __init__(self) -> None:
        pass

 

    def get_list_tables(self, database:str, glue = boto3.client('glue')) -> list:
        ''' 
            List tables from database
            Returns: list {Table_Name, Location, TableType}  
        '''
        
        
        try:
            response = glue.get_tables(DatabaseName=database, MaxResults=100)
            tables_list = response['TableList']

            if 'NextToken' in response:
                while 'NextToken' in response:
                    next_token = response['NextToken']
                    response = glue.get_tables(DatabaseName=database, NextToken=next_token, MaxResults=200)
                    tables_list.extend(response['TableList'])
                    
            
            return process_json_table_list(tables_list)

        except Exception as e:
            print(f"Erro ao retornar tabelas do Database: {database}. Erro: {e}")

    


