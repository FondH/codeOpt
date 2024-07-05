import json
import os
import subprocess
from .run_climate import run_codeclimate

def run_checkstyle(file_path, checkstyle_jar='checkstyle-8.37-all.jar', config_file='google_checks.xml'):
    checkstyle_jar_path = os.path.abspath(os.path.join('exe/checkstyle', checkstyle_jar))
    config_path = os.path.abspath(os.path.join('exe/checkstyle', config_file))
    file_path = os.path.abspath(file_path)

    print("Checkstyle JAR path:", checkstyle_jar_path)
    print("Config file path:", config_path)
    print("File to check path:", file_path)

    command = ['java', '-jar', checkstyle_jar_path, '-c', config_path, file_path]
    print("Command:", ' '.join(f'"{arg}"' if ' ' in arg else arg for arg in command))

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', shell=True)

    # 从 stderr 中读取输出
    checkstyle_output = result.stdout
    print("Checkstyle Output:", checkstyle_output)

    errors = []
    for line in checkstyle_output.split('\n'):
        if line.strip() == '' or not file_path in line:
            continue
        parts = line.split(':')
        if len(parts) < 4:
            continue  # 跳过无效行

        # parts[1] 应该是行号，如果不是数字则继续
        try:
            line_number = int(parts[2].strip())
            column_number = int(parts[3].strip())
            message = ':'.join(parts[4:]).strip()
        except ValueError:
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        line_content = lines[line_number - 1].strip() if line_number <= len(lines) else ''

        errors.append({
            'line': line_number,
            'column': column_number,
            'message': message,
            'type': 'checkstyle',
            'line_content': line_content,
        })
    return errors

#
# file_path = r'G:\My_Projects\codeopt\api\tools\instance\java_test.java'  # 替换为你要分析的文件路径
# errors = run_checkstyle(file_path)
# print(errors)
