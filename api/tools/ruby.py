from .run_climate import run_codeclimate
import json,os
from .cpp import detect_file_encoding
def ruby_syntax_check(file_path, engine_name='brakeman'):
    """

    :param abs_file_path:
    :return: json: [
                'detail':{
            'line': error['line'],
            'column': error['column'],
            'message': error['message'],
            'id': error['message-id'],
            'type': 'pylint',
             }]
    """
    result = run_codeclimate(file_path,engine_name)
    pylint_output = json.loads(result)
    with open(file_path, 'r', encoding=detect_file_encoding(file_path)) as f:
        lines = f.readlines()

    formatted_errors = []
    for error in pylint_output:
        line_content = lines[error['line'] - 1].strip() if error['line'] <= len(lines) else ''
        formatted_errors.append({
            'line': error['location']['lines']['begin'],
            'column': 0,  # Assuming 'column' information is not provided in the JSON data
            'content': line_content,  # Assuming 'line_content' needs to be fetched from the actual file
            'message': error['description'],
            'id': error['categories'][0] if error['categories'] else None,
            'code': error['fingerprint'],  # Assuming 'fingerprint' as the closest match for 'message-id'
        })
    return json.dumps({
        'file_name':os.path.basename(file_path),
        'file_path':file_path,
        'type':'phpmd',
        'res':formatted_errors,
    })