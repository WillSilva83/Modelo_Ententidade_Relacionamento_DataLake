import boto3 
from src.utils.external_libs import validate_string

class S3():
    def __init__(self) -> None:
        pass

    def get_list_buckets(self, s3 = boto3.client('s3')) -> list:
        ''' Return a list of Buckets '''

        response = s3.list_buckets() 
        list_buckets = []

        for bucket in response['Buckets']:
            list_buckets.append(bucket['Name'])

        return list_buckets

    def get_list_dir(self, bucket_name: str, s3 = boto3.client('s3'), is_format_output = False, prefix='') -> list:
        """
        Lista todos os diretórios (prefixos) de um bucket S3.

        Parameters:
        - bucket_name (str): Nome do bucket S3.

        Returns:
        - list: Lista de diretórios.
        """
    
        paginator = s3.get_paginator('list_objects_v2')
    
        result = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
        
        list_dirs = set()
        
        for page in result:
            if 'Contents' in page:
                for obj in page['Contents']:
                    key = obj['Key']
                    # Adiciona todos os níveis de diretórios
                    prefixos = key.split('/')[:-1]
                    for i in range(1, len(prefixos) + 1):
                        if is_format_output:
                            output = f"s3://{bucket_name}/{'/'.join(prefixos[:i]) + '/'}"
                            # Retorna apenas diretorios sem data 
                            if not validate_string(output):
                                list_dirs.add(output)
                        else: 
                            list_dirs.add('/'.join(prefixos[:i]) + '/')
        
        return list_dirs

    def is_table(self):
        pass