from pytube import YouTube

# Solicita ao usuário um link
link = input("Qual o link do vídeo que você quer baixar? ")
video = YouTube(link)

# Obtém o título do vídeo
titulo = video.title
print(f'\nTítulo do vídeo: \033[93m{titulo}\033[0m\n')

# Verifica a opção escolhida pelo usuário
confirmacao = input(f'Quer baixar o vídeo ou só o áudio? [V/A]\n')

# Se escolheu baixar o vídeo
if confirmacao.lower() == 'v':
    print("\033[94mBaixando o Vídeo...\033[0m\n")
    ys = video.streams.get_highest_resolution()

 # Se escolheu baixar apenas o áudio
elif confirmacao.lower() == 'a':
    print("\033[94mBaixando apenas o Áudio...\033[0m\n")
    ys = video.streams.filter(only_audio=True).first()

else:
    print('\033[91mOpção inválida. Por favor, digite V ou A.\033[0m')
    exit()

# Inicia o download
print("\033[92m***DOWNLOAD EM PROGRESSO***\033[0m\n")
ys.download()
print("\033[92m***DOWNLOAD CONCLUÍDO***\033[0m\n")
