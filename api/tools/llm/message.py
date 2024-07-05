from .client import LocalClient,RemoteClient
def completion_with_ollama(text: str, model: str = "phi3:mini") -> str:
    response = LocalClient().generate(
        model=model,
        messages=text
    )
    if response:
        return response["response"]
    else:
        return "Error with the remoteclient"


def completion_with_ollama_remote(text: str, system: str = "") -> str:
    response = RemoteClient().generate(
        system=system,
        messages=text
    )
    if response:
        return response["response"]
    else:
        return "Error with the remoteclient"


def completion_with_chatgpt(text: str,
                            model: str = "phi3:mini",
                            system: str = "You are a helpful assistant.",
                            is_local: bool = True,
                            is_openai: bool = False) -> str:
    if is_local:
        return completion_with_ollama(text, model)

    else:
        return completion_with_ollama_remote(text, system)