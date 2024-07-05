import subprocess
import re
import json
import os,sys
import chardet

curr_dir = os.path.split(os.path.realpath(__file__))[0]
exe_root = os.path.join(curr_dir, 'exe')

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def cpp_standard_check(file_path):
    result = subprocess.run(['cpplint', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cpplint_output = result.stderr.decode('utf-8')

    with open(file_path, 'r', encoding=detect_file_encoding(file_path)) as f:
        lines = f.readlines()

    cpplint_errors = []
    for line in cpplint_output.split('\n'):
        match = re.match(r'^(.*?):(\d+):\s*(.*?\s+\[(.*?)\])', line)
        if match:
            line_num = int(match.group(2))
            line_content = lines[line_num - 1].strip() if line_num <= len(lines) else ''
            cpplint_errors.append({
                'line': line_num,
                'column': 0,
                'content': line_content,
                'message': match.group(3),
                'id': match.group(4),
            })

    return json.dumps({
        'file_name':os.path.basename(file_path),
        'file_path':file_path,
        'type':'cpplint',
        'res':cpplint_errors,
    })


def cpp_syntax_analysis(file_path):
    import xml.etree.ElementTree as ET
    cppcheck_path = os.path.join(exe_root, 'cppcheck/cppcheck.exe')

    result = subprocess.run([cppcheck_path, '--enable=all', '--xml', '--xml-version=2', file_path],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cppcheck_output = result.stderr.decode('latin-1')

    with open(file_path, 'r', encoding=detect_file_encoding(file_path)) as f:
        lines = f.readlines()

    # 解析XML输出
    root = ET.fromstring(cppcheck_output)
    errors = []
    for error in root.findall('errors/error'):
        location = error.find('location')
        if location is not None:
            line = int(location.attrib['line'])
            column = int(location.attrib['column'])

            line_content = lines[line - 1].strip() if line <= len(lines) else ''

            errors.append({
                'line': line,
                'column': column,
                'message': error.attrib['msg'],
                'id': error.attrib['id'],
                'severity': error.attrib['severity'],
                'type': 'cppcheck',
                'content': line_content,
            })
    return json.dumps({
        'file_name':os.path.basename(file_path),
        'file_path':file_path,
        'type':'cpplint',
        'res':errors,
    })




file_path = r'G:\\My_Projects\\codeopt\\api\\files\\Likou.cpp'
errors = cpp_standard_check(file_path)
errors_ = cpp_syntax_analysis(file_path)


print(len(errors) + len(errors_))