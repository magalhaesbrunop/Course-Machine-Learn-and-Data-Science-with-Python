file = open('file.txt', 'a') #escreve no arquivo e nao faz substituição do conteudo
file1 = open('file.txt', 'r+b') #leitura modo binario
file2 = open('file.txt', 'w+b') #escrita modo binario
file3 = open('file.txt', 'w') #escreve no arquivo e se for salvo mais de uma vez,
                                # substitui o conteudo do arquivo anterior
#arq3.write('machine learning')
file3.write('Aprendendo python')

text = '''
Aprendendo python
machine learning
pau no seu cu
'''

file3.write(text)
file3.close()



