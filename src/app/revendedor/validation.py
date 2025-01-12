from datetime import datetime
import re

def validar_cpf(cpf: str) -> str:
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)
    
    cpf = cpf.zfill(11)
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        raise ValueError("O cpf informado está invalido.") 
    
    # Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
    if cpf == cpf[0] * len(cpf):
        raise ValueError("O cpf informado está invalido.") 
    
    # Calcula os dígitos verificadores
    def calcular_digito(cpf_parcial):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(len(cpf_parcial) + 1, 1, -1)))
        resto = soma % 11
        if resto<2:
            return "0"
        return str(11 - resto)
    
    # Valida o primeiro dígito verificador
    primeiro_digito = calcular_digito(cpf[:9])
    if cpf[9] != primeiro_digito:
        raise ValueError("O cpf informado está invalido.") 
    
    # Valida o segundo dígito verificador
    segundo_digito = calcular_digito(cpf[:10])
    if cpf[10] != segundo_digito:
        raise ValueError("O cpf informado está invalido.") 
    
    return cpf

def create_at_to_str(data):
    if isinstance(data,datetime):
        data = data.isoformat()  # Ou qualquer formato que desejar
    return data
