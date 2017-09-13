from multiprocessing.connection import Listener, Client

def conn():
    if input('Are you the host?\n -> ').lower() in ('yes', 'y', 's', 'sim', 'yep'): #input('Are you the host?\n -> ')
        working = False
        atFirst = True
        while not working:
            try:
                working = True
                server = Listener(('', 28465))
            except OSError:
                working = False
                atFirst = False
                porta += 1
        if not atFirst:
            print('Porta solicitada ja em uso. No entanto, encontramos a porta', porta, 'disponível para uso')
        print('Esperando por conexao...')
        try:
            connection = server.accept()
        except Exception:
            traceback.print_exc()
    else:
        server = None
        IP = 'lipe.velasco.one:28465'
        foi = False
        while not foi:
            foi = True
            if ':' in IP:
                IP, porta = IP.split(':')[0], int(IP.split(':')[1])
            try:
                connection = Client((IP, porta))
            except Exception:#URLError:
                IP = input('Qual o IP do Host?\n -> ')
                foi = False

    return(connection, server)


#hehe 26.1.17
