#Padrão ANSI (Escape sequence)
# \033[m - Entre o colchete e o 'm' coloca as especificações dos seus caracteres, que serão:
## STYLE, TEXT E BACK
##STYLE = Comportamento (negrito? sublinhada?)
##TEXT = Cor do texto
##BACK =  Cor de fundo
\033[0;33;44m

#Códigos para estilos STYLE: 0 = sem estilo, 1 = negreito, 4 = sublinhado e 7 = inverter confg.
#Códigos para estilos TEXT: 30, 31, 32 ... 37. Na ordem: Branco, Vermelho, Verde, Amarelo, Azul, Lilás
##Azul Claro, Cinza
#Códigos para estilos BACK: 40, 41 ... 47. Na mesma ordem anterior

\033[0;30;41m
