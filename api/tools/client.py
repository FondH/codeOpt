from .llm.message import completion_with_chatgpt


class CodeOpt:

    def __init__(self, name, role_document):
        self.name = name
        self.role_document = role_document

    def run_harness(self, code,error, is_local=False, options=None):
        prompt = f'Mycode:{code}\nError:{error}'
        if is_local:
            application_prompt = f'''
            Please review the following code for syntax issues, naming convention problems, and serious vulnerabilities. Provide your feedback in the following format:
            [Advice]
            <Your advice goes here>
            
            [code]
            <Your suggested code goes here>
            
            Here is the code to review:
            {prompt}
                                '''
            response = completion_with_chatgpt(application_prompt)
        else:
            application_prompt = (
                """
Please review the following code for syntax issues, naming convention problems, and serious vulnerabilities. Provide your feedback in the following format:

1. [Advice]
Provide a list of specific suggestions and advice on how to improve the code, including any detected issues related to syntax, naming conventions, and vulnerabilities.

2. [Code]
Provide the revised version of the code with the suggested improvements applied. This section should only contain the updated code without additional explanations.

                """)
            response = completion_with_chatgpt(prompt,is_local=False, system=application_prompt)

        try:
            advice = response.split('[Advice]')[-1]
            code_  = advice.split('[Code]')[-1]
            return {
                'advice':advice,
                'code':code_
            }

        except Exception as e:

            return {
                'advice': response,
                'code':'AHa, CodeOpt has some errors'
            }

