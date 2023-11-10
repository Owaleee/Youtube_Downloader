from pytube import YouTube

while True:
    link = input("Qual o link do vídeo que você quer baixar? ")
    video = YouTube(link)

    # Obtém o título do vídeo
    titulo = video.title
    print(f'\nTítulo do vídeo: {titulo}\n')

    confirmacao = input(f'Esse é o titulo do video que você quer baixar? [S/N]\n')
    if confirmacao == 's':
        video = video.streams.get_highest_resolution()
        video.download()
        print(f'Pronto, vídeo baixado!')

    elif confirmacao == 'n':
        continue

    else:
        print('Opção inválida. Por favor, digite S ou N.')