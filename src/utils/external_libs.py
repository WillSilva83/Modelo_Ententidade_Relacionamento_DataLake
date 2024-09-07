import json 
import re

def write_file(data, file_name = "file_output.json", is_json = False, encoding = 'utf-8', ensure_ascii = False, indent = 4):
    ''' Save file '''
    try:
        with open(file_name, 'w', encoding=encoding) as file:
            if is_json:
                json.dump(data, file, ensure_ascii=ensure_ascii, indent=indent)
            else: 
                for line in data: 
                    file.write(f"{line}\n")
                

    except Exception as e:
        print(f"Erro ao salvar JSON no arquivo. Erro: {e}")
    pass 

def validate_string(str_data) -> bool:  
    ''' validar se possui formato YYYY-MM-DD '''
    pattern_1 = r'dt_arq|anomes|process_date|dt_incl'
    pattern_2 = r'\w=\d{2}'
    
    return bool(re.search(pattern_1, str_data) or re.search(pattern_2, str_data))