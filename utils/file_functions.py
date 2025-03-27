import os


def copy_file(input_name:str,output_name:str):
    
    if os.path.exists(input_name):
        with open(input_name,'r') as file:
            content = file.read()
            with open(output_name,'a') as file2:
                file2.write(content)
        return True
    else:
        return False
    # "Error, the file doe's not exist"
