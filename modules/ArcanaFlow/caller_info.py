# caller_info.py
import inspect
import os

def get_caller_info():
    """
    Obtém informações do local (arquivo, linha) de onde a função foi chamada.
    Percorre a pilha para encontrar o chamador fora do módulo de log.
    """
    stack = inspect.stack()
    
    caller_info = None

    # stack[0] é esta função
    # stack[1] seria a função 'out' do ArcanaFlow
    # stack[2] seria a função 'action/error' do ArcanaFlow
    # stack[3] geralmente é o código do usuário que chamou o log
    
    # Vamos procurar o primeiro frame que NÃO seja este arquivo nem o arcana_flow
    for frame_info in stack:
        filename = frame_info.filename
        # Ignora arquivos internos do sistema ou do próprio logger
        if "caller_info.py" in filename or "arcana_flow.py" in filename or "importlib" in filename:
            continue
            
        caller_info = {
            'file': filename,
            'line': frame_info.lineno,
            'function_name': frame_info.function
        }
        break # Encontramos o primeiro arquivo externo

    # Limpeza para evitar memory leaks com frames
    del stack

    if not caller_info:
        return {'file': 'unknown', 'line': 0, 'function_name': 'unknown'}

    return caller_info