import json
from api.tools.cpp import cpp_standard_check,cpp_syntax_analysis
from api.tools.python import py_standard_check,py_syntax_check
from api.tools.java import run_checkstyle
import os

default_model_setting = {
  'model': 'model1',
  'proxy': '',
  'temperature': 0.7,
  'maxTokens': 100,
  'topP': 0.9,
  'frequencyPenalty': 0,
  'presencePenalty': 0
}
default_stragtegy ={"python":{"syntaxMethod":"classic","vulnerabilityMethod":"none","styleCheckMethod":"classic"},
                    "go":{"syntaxMethod":"classic","vulnerabilityMethod":"none","styleCheckMethod":"classic"},
                    "java":{"syntaxMethod":"classic","vulnerabilityMethod":"none","styleCheckMethod":"classic"},
                    "cpp":{"syntaxMethod":"classic","vulnerabilityMethod":"none","styleCheckMethod":"classic"},
                    "ts":{"syntaxMethod":"classic","vulnerabilityMethod":"none","styleCheckMethod":"classic"},
                    "ruby":{"syntaxMethod":"classic","vulnerabilityMethod":"none","styleCheckMethod":"classic"},
                    "php":{"syntaxMethod":"classic","vulnerabilityMethod":"none","styleCheckMethod":"classic"}}
def detect(file_path, language, default_stragtegy=None,detectModules=None):

    errors = None
    try:
        if language == 'cpp' or 'c':
            errors= {
                'file_name': os.path.basename(file_path),
                'standard_check_res':cpp_standard_check(file_path),
                'syntax_check_res':cpp_syntax_analysis(file_path)
                }

        elif language == 'py':
            errors=  {
                'file_name':os.path.basename(file_path),
                'standard_check_res':py_standard_check(file_path),
                'syntax_check_res':py_syntax_check(file_path)
                }

        elif language == 'java':
            errors=  {
                'file_name': os.path.basename(file_path),
                'standard_check_res:':[run_checkstyle(file_path)],
                'syntax_check_res': [run_checkstyle(file_path)]
            }

        elif language == 'php':
            errors=  {
                'file_name': os.path.basename(file_path),
                'standard_check_res':cpp_standard_check(file_path),
                'syntax_check_res':cpp_syntax_analysis(file_path)
                }
        else:
            print(f'test {language}: {file_path} failed')
            return None
    except:
        pass
    po = 'None llm'
    if detectModules:
        try:
            ai_res = model_answer(file_path, errors,detectModules)
            errors['ai_res'] = ai_res
            po = 'USEing LLm'
        except:
            pass

    print(f'test {language}: {file_path}  succ' ,po)

    return errors

from tools.client import CodeOpt
codeOpt = CodeOpt('codeOpt bot', 'This is a AI coding helper, help you do some work')

import chardet
def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']
def model_answer(file_path,errors, model_setting=None):
    try:
        with open(file_path,'r',encoding=detect_file_encoding(file_path)) as f:
            #print('file_len:', f.read().__len__())
            #print('errors', errors.__str__().__len__())
            answ = codeOpt.run_harness(f.read(),'there are some syntax errors or just formated errors', is_local=False,options=model_setting)
        return answ
    except Exception as e:
        print(f'detect model_answer with error {e}')
        return {
                'advice':'somthing wrong',
                'code':'somthing wrong'
            }




if __name__ == '__main__':
    file_path = r'G:\\My_Projects\\codeopt\\api\\files\\No16-02.cpp'
    errors= detect(file_path, 'c', detectModules=True)
    print(errors)
