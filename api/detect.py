import json
from api.tools.cpp import cpp_standard_check,cpp_syntax_analysis
from api.tools.python import py_standard_check,py_syntax_check
from api.tools.java import run_checkstyle
import os

def detect(file_path, language, detectModules):

    print(f'test {language}: {file_path} succ')

    if language == 'cpp':
        return ({
            'file_name': os.path.basename(file_path),
            'standard_check_res':cpp_standard_check(file_path),
            'syntax_check_res':cpp_syntax_analysis(file_path)
            })

    elif language == 'py':
        return ({
            'file_name':os.path.basename(file_path),
            'standard_check_res':py_standard_check(file_path),
            'syntax_check_res':py_syntax_check(file_path)
            })

    elif language == 'java':
        return ({
            'file_name': os.path.basename(file_path),
            'standard_check_res:':[run_checkstyle(file_path)],
            'syntax_check_res': [run_checkstyle(file_path)]
        })

    elif language == 'c':
        return ({
            'file_name': os.path.basename(file_path),
            'standard_check_res':cpp_standard_check(file_path),
            'syntax_check_res':cpp_syntax_analysis(file_path)
            })
    else:
        print(f'test {language}: {file_path} failed')
        return None

