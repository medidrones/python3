# \r\n -> CRLF - Windows
# \n -> LF - Linux e Mac (OBS: No Windows apartir da versão 10 funciona)
print(12, 34, 1011, sep="-", end='\r\n')
print(56, 78, sep='-', end='##\n')
print(9, 10, sep='-', end='\n')