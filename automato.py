class Automato:
    '''
        Classe responsável por armazenar as informações do autômato e realizar as operações nele
    '''
    def __init__(self, args=None, deterministico=False):
        if args:
            self.nome = args['nome']
            self.estados = args['estados']
            self.transicoes = args['transicoes']
            self.inicial = args['inicial']
            self.finais = self.__removeDuplicatas(args['finais'])
            self.deterministico = deterministico

    def __str__(self):
        return f'Automato: {self.nome}\nDeterministico? {str(self.deterministico)}\nEstados: {str(self.estados)}\nTransicoes: {str(self.transicoes)}\nEstado inicial: {self.inicial}\nEstados Finais: {str(self.finais)}'

    def determinizar(self, override=False):
        '''
            Determiniza um autômato não-determinístico SEM MOVIMENTOS VAZIOS
        '''
        
        finais = []
        novosEstados = {}
        done = [] # Para evitar recursão infinita, iremos guardar onde já percorremos
        fila = [self.inicial] #Inicializa a fila a partir do ponto inicial

        while(fila):
            query = fila.pop(0)
            estados = query.split(',')
            try:
                for transicao in self.transicoes:

                    # Inicializando auxiliar
                    alcancaveis = []

                    # Encontra todos os estados alcancaveis, removendo suas duplicatas
                    for estado in estados:
                        alcancaveis.extend(self.estados[estado][transicao])
                    alcancaveis = self.__removeDuplicatas(alcancaveis)

                    # Cria o nome do novo estado
                    novoEstado = ','.join(alcancaveis)

                    # Verifica se é um estado final, e se for, adiciona ele a lista
                    for alcancavel in alcancaveis:
                        if alcancavel in self.finais:
                            finais.append(novoEstado)

                    # Mostra que novosEstados[query] é um objeto, já que Python <<<< Ruby, e marca a transicao
                    if query not in novosEstados:
                        novosEstados[query] = {}
                    novosEstados[query][transicao] = novoEstado

                    # Check anti-recursão
                    if novoEstado not in done:
                        fila.append(novoEstado) # Próximo estado a ser identificada as transições
                        done.append(novoEstado) # Array que mantém informações para evitar recursão infinita

            except: # Para evitar de tentar encontrar strings vazias, morre silenciosamente
                pass

        newAutomato = Automato({
                                'nome': self.nome + '_Deterministico',
                                'estados': novosEstados,
                                'transicoes': self.transicoes,
                                'inicial': self.inicial,
                                'finais': finais}, deterministico=True)

        # Override == True ? sobrescreve automato atual : retorna um novo automato
        if override:
            self.deterministico, self.estados, self.finais, self.inicial, self.nome, self.transicoes  = [getattr(newAutomato,aut) for aut in dir(newAutomato) if not aut.startswith('__') and not callable(getattr(newAutomato,aut))]
            return self

        return newAutomato

    ###############


    def reconhecer(self, palavra):
        '''
            Verifica se uma determinada palavra é reconhecida ou não pela linguagem que o autômato reconhece
            @param palavra -> string separada por vírgulas, representando cada uma das transições
        '''

        # Se o automato não for deterministico, cria um cópia determinizada
        automato = self
        if not self.deterministico:
            automato = self.determinizar()

        # Estado atual inicial e transicoes a serem feitas
        atual, transicoes = automato.inicial, palavra.split(',')

        # Itera sobre as transicoes, e lida com rejeição por indefinição
        for transicao in transicoes:
            try:
                atual = automato.estados[atual][transicao]
            except KeyError: # Para por indefinição
                return 'REJEITA'

        # Após terminar de ler a palavra, caso esteja em um estado final, aceita a palavra, caso contrário, rejeita
        if atual in automato.finais:
            return 'ACEITA'
        else:
            return 'REJEITA'


    def __removeDuplicatas(self, array):
        '''
            Remove valores duplicados em uma array e a ordena
            i.e.: __removeDuplicatas([1,2,2,1,6,4]) => [1,2,4,6]
        '''
        arrayNew = []
        for val in array:
            if val not in arrayNew:
                arrayNew.append(val)

        return sorted(arrayNew)
