class FilaNormal:

     codigo:int = 0
     fila = []
     clientesatendidos=[]
     senhatual:str = ""
     #essas coisas -> sao para colocar se retorna alguma coisa ou nao e qual o timo da forma doq esta sendo retornado
#nao tem argumento depois do self entao colocar nome
     def gera_senha(self)->None:
         self.senhatual = f"nm{self.codigo}"

# nao a argumentos e nao retorna nada entao por isso do -> nome
     def reseta_fila(self)->None:
         #caso sja maior qe sem iguala a 0
        if self.codigo >=100:
            self.codigo=0
        else:
            self.codigo+=1
     def atualiza_fila(self)->None:
         self.reseta_fila()
         self.gera_senha()
         self.fila.append(self.senhatual)

#msotrando que retorna uma str entao coloca ->
     def chama_cliente(self,caixa:int)->str:
         #sempre que chamar esse vai colocar o 1 cliente e colocar ele dentro de clientes  atentidos
        print(self.fila)
        cliente_atual:str=self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return f"Client atual: {cliente_atual},Dirija-se  ao caixa: {caixa}"







