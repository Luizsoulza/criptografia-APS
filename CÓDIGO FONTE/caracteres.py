digitos = list('0123456789')

letras_maiusculas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

letras_minusculas = list('abcdefghijklmnopqrstuvwxyz')

pontuacoes = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

espacos = [' ']

letras_acentuadas = [
    'á','à','â','ã','ä','é','è','ê','ë','í','ì','î','ï',
    'ó','ò','ô','õ','ö','ú','ù','û','ü','ç',
    'Á','À','Â','Ã','Ä','É','È','Ê','Ë','Í','Ì','Î','Ï',
    'Ó','Ò','Ô','Õ','Ö','Ú','Ù','Û','Ü','Ç','ñ','Ñ'
]

simbolos_extra = ['€','£','¥','¢','§','©','®','™','°','±','×','÷','µ','¶']

BASE_CARACTERES = (
    digitos +
    letras_maiusculas +
    letras_minusculas +
    pontuacoes +
    espacos +
    letras_acentuadas +
    simbolos_extra
)
