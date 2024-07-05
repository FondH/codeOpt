import subprocess
import re,os
import json
# id代表错误码，但是错误码是针对不同检测工具而言的，所以涉及到错误码的都想办法使用文字代替，实在代替不了就设置为空
#
def py_syntax_check(file_path):
    """

    :param file_path:
    :return: json: [
                'detail':{
            'line': error['line'],
            'column': error['column'],
            'message': error['message'],
            'id': error['message-id'],
            'type': 'pylint',
             }]
    """
    result = subprocess.run(['pylint', file_path, '-f', 'json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pylint_output = result.stdout.decode('utf-8')
    pylint_errors = json.loads(pylint_output)

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    formatted_errors = []
    for error in pylint_errors:
        line_content = lines[error['line'] - 1].strip() if error['line'] <= len(lines) else ''
        formatted_errors.append({
            'line': error['line'],
            'column': error['column'],
            'content': line_content,
            'message': error['message'],
            'id': error['symbol'],
            'code': error['message-id'],
        })

    return json.dumps({
        'file_name':os.path.basename(file_path),
        'file_path':file_path,
        'type':'pylint',
        'res':formatted_errors,
    })


def py_standard_check(file_path):
    result = subprocess.run(['flake8',  file_path],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    checkstyle_output = result.stdout

    errors = []
    for line in checkstyle_output.split('\n'):
        if line.strip() == '' or not file_path in line:
            continue
        parts = line.split(':')
        if len(parts) < 4:
            continue  # 跳过无效行

        # parts[2] 应该是行号， [3]是列号
        try:
            line_number = int(parts[2].strip())
            column_number = int(parts[3].strip())
            message = parts[4:][0].strip()[5:]
            #print(message)
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
            'content': line_content,
        })
    return json.dumps({
        'file_name': os.path.basename(file_path),
        'file_path': file_path,
        'type': 'pylint',
        'res': errors,
    })

# file_path = r'G:\A大三下\软件工程\codeopt\api\__init__.py'
# errors = py_standard_check(file_path)
# er = py_syntax_check(file_path)
# print(errors)
# print(er)

# with open('lint_errors.json', 'w') as f:
#     json.dump(errors, f, indent=4)
