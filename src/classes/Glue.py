import boto3 
from src.utils.logging import config_logger
from src.utils.external_libs import process_json_table_list

logger = config_logger('App Tables S3 X Athena')

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

    def get_table(self, database_name:str, list_tables: list, glue = boto3.client('glue')) -> dict: 
        ''' Return Columns Tables '''

        out_respose = []

        for table in list_tables:
            try: 
                response = glue.get_table(DatabaseName=database_name, Name=table) 
                out_respose.append(response)


            except Exception as e: 
                print(f"Erro ao retornar a tabela {table}. Erro: {e}")
                return []
            
        return out_respose
    
            
    


