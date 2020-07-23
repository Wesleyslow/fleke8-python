class FilaPrieoritaria:
    codigo:int = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str =""

    def gera_senha_atual(self):
        self.senha_atual= f"nm{self.codigo}"


    def reseta_fila(self):
        if self.codigo >= 100:
            self.codigo=0
        else:
            self.codigo+=1


    def atualiza_fila(self)->None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)


    def chama_cliente(self,caixa:int)->str:
        cliente_atual:str=self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Client atual: {cliente_atual},Dirija-se  ao caixa: {caixa}"


    def estatistica(self,dia:str,agencia:int,flag:str)-> dict:
        if flag!='Detail':
            estatistica = {f'{agencia}-{dia}':len(self.clientes_atendidos)}

        else:
            estatistica = {}
            estatistica['dia']=dia
            estatistica['agencia']=agencia
            estatistica['clientes atendidos']=self.clientes_atendidos
            estatistica['Quantidade clientes Atendidos']=len(self.clientes_atendidos)

        return estatistica






