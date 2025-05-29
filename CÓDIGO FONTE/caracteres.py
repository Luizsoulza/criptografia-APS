# Dígitos
digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Letras maiúsculas
letras_maiusculas = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Letras minúsculas
letras_minusculas = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Pontuações e símbolos comuns
pontuacoes = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

# Espaço
espacos = [' ']

# Letras acentuadas
letras_acentuadas = [
    'á','à','â','ã','ä','é','è','ê','ë','í','ì','î','ï',
    'ó','ò','ô','õ','ö','ú','ù','û','ü','ç',
    'Á','À','Â','Ã','Ä','É','È','Ê','Ë','Í','Ì','Î','Ï',
    'Ó','Ò','Ô','Õ','Ö','Ú','Ù','Û','Ü','Ç','ñ','Ñ'
]

# Símbolos extras
simbolos_extra = ['€','£','¥','¢','§','©️','®️','™️','°','±','×','÷','µ','¶']

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