import boto3 

class AthenaObj: 
    def __init__(self, athena_client =  boto3.client('athena')):
        self.athena_client = athena_client
    
    def prepare_query(self, database: str, table: str, type: str, partition = '') -> str: 
    
        if type == "volume":
            query_string = f"""SELECT COUNT(1) FROM {database}.{table}"""
        
        elif type == "volume_by_partition":
            query_string = f"""SELECT COUNT(1), {partition} FROM {database}.{table}"""
        
        return query_string    

    def get_execution_id(self, athena_client: boto3.client, query_string: str, database : str):
        
        result_config =  's3://test/' #config.OUTPUTLOCATION

        try:
            response = athena_client.start_query_execution(
                QueryString = query_string, 
                QueryExecutionContext = {'Database' : database},
                ResultConfiguration = {'OutputLocation' : result_config}
            )
            return response['QueryExecutionId']
        
        except Exception as error: 
            print(f"Erro no response do Athena: {error}")
            return None 

    def get_query_results(self, query_execution_id):
        athena_client = boto3.client('athena')
        
        while True:
            response = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
            state = response['QueryExecution']['Status']['State']
            
            if state == 'SUCCEEDED':
                break
            elif state in ['FAILED', 'CANCELLED']:
                raise Exception(f'Query {state.lower()}')
            
        
        response = athena_client.get_query_results(QueryExecutionId=query_execution_id)
        
        return response






