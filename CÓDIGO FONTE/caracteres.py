#caracteres.py

# Dígitos
digitos = list('0123456789')

# Letras maiúsculas
letras_maiusculas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Letras minúsculas
letras_minusculas = list('abcdefghijklmnopqrstuvwxyz')

# Pontuações e símbolos comuns
pontuacoes = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

# Espaço
espacos = [' ']

# Letras acentuadas e especiais
letras_acentuadas = [
    'á','à','â','ã','ä','é','è','ê','ë','í','ì','î','ï',
    'ó','ò','ô','õ','ö','ú','ù','û','ü','ç',
    'Á','À','Â','Ã','Ä','É','È','Ê','Ë','Í','Ì','Î','Ï',
    'Ó','Ò','Ô','Õ','Ö','Ú','Ù','Û','Ü','Ç','ñ','Ñ'
]

# Símbolos extras
simbolos_extra = ['€','£','¥','¢','§','©','®','™','°','±','×','÷','µ','¶']

# Junta todas as listas numa única lista chamada BASE_CARACTERES
BASE_CARACTERES = (
    digitos +
    letras_maiusculas +
    letras_minusculas +
    pontuacoes +
    espacos +
    letras_acentuadas +
    simbolos_extra
)
