import os, urllib.request, datetime
#from urllib.request import urlopen


items = ('Jogo.py', 'BoatClass.py', 'Functions.py', 'connect.py')
imgs = ('cruiser.png', 'destroyer.png', 'patrulha.png', 'portavioes.png', 'submarine.png')

url = 'http://44.128.0.2:15000/'

error = False
while not error:
    try:
        error = True
        for file in items:
            server = urllib.request.urlopen(url+file)
            info = server.read()
            gamefile = open(file, 'wb')
            gamefile.write(info)
            gamefile.close()
        directory = 'Boats'
        if not os.path.exists(directory):
            os.makedirs(directory)
            for img in imgs:
                server = urllib.request.urlopen(url+'/Boats/'+img)
                with open(directory+'/'+img, 'wb') as file:
                    file.write(server.read())
            
    except URLError:
        input('Error:', url, 'não acessível.\nnovo url para update:\n -> ')
        error = False

