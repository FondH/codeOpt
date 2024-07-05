import requests
import os

remot_url = 'http://localhost:11434'

os.environ['http_proxy'] = ''
os.environ['https_proxy'] = ''


class LocalClient:
    """

    """
    def __init__(self, base_url=remot_url):
        __my_model_list__ = ['phi3:mini', 'qwen2:1.5b',
                             'qwen2:1.5b', 'llama3:latest']

        self.base_url = base_url

    def generate(self, model, messages, temperature=0.8):
        url = f"{self.base_url}/api/generate"
        options = {
            "temperature": temperature,
        }
        payload = {
            "model": model,
            "prompt": messages,
            "stream": False,
            "options": options
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ollama chat Request failed: {e}")
            return None

    def chat(self, model, messages, temperature=0.8):
        url = f"{self.base_url}/api/chat"
        options = {
            "temperature": temperature,
        }
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "options": options
        }
        try:
            """ 
            response.json():<dict>=>
                dict_keys(['model', 'created_at', 'message'=> dict_keys(['role', 'content']),   
                'done_reason', 'done', 
                'total_duration', 
                'load_duration',
                'prompt_eval_duration', 
                'eval_count', 'eval_duration'])
            """
            response = requests.post(url, json=payload)
            response.raise_for_status()
            # logger.info(f"Request successful. Status code: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ollama chat Request failed: {e}")
            return None


class RemoteClient:
    def __init__(self, base_url=remot_url):
        # https://blog.zhexuan.org/pages/freeapi.html
        __my_model_list__ = ['llama-2-7b-chat-hf-lora', 'llama-3-8b-instruct']

        self.base_url = 'http://127.0.0.1:8787'

    def generate(self, messages, system=None, model=None):
        url = f"{self.base_url}/api"
        data = {
            "question": messages,
            "system": system
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ollama chat Request failed: {e}")
            return None

