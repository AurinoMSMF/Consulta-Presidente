nome_lista_presidentes=["Deodoro da Fonseca", "Floriano Peixoto", "Prudente de Morais", "Campos Sales", "Rodrigues Alves", "Afonso Pena", "Nilo Peçanha", "Hermes da Fonseca", "Venceslau Brás", "Delfim Moreira", "Epitácio Pessoa", "Artur Bernardes", "Júlio Prestes", "Getúlio Vargas", "José Linhares", "Eurico Gaspar Dutra", "Café Filho", "Carlos Luz", "Nereu Ramos", "Juscelino Kubitschek", "Jânio Quadros", "Ranieri Mazzilli", "João Goulart", "Humberto Castelo Branco", "Artur da Costa e Silva", "Pedro Aleixo", "Emílio Garrastazu Médici", "Ernesto Geisel", "João Figueiredo", "Tancredo Neves", "José Sarney", "Fernando Collor", "Itamar Franco", "Fernando Henrique Cardoso", "Luiz Inácio Lula da Silva", "Dilma Rousseff", "Michel Temer", "Jair Bolsonaro"]
print("Boa noite! Esta é a lista atualizada com os nomes de todos os Presidentes da República Federativa do Brasil, do passado e presente. Espero que possa ajudá-lo.")
for nome_verifica in nome_lista_presidentes:
        while(nome_verifica not in nome_lista_presidentes):
                nome_verifica=input("Digite o nome para conferir se está na lista de presidentes do Brasil :D : ")
                nome_verifica= nome_verifica
                print("Este nome não consta na lista de presidentes do Brasil.")
                if(nome_verifica in nome_lista_presidentes):
                        print("Este é o presidente", nome_verifica,". Que governou, de fato, a Terra de Santa Cruz.")
        
        #def verificacao():
        #                verifica = nome_verifica 
        #                if nome_verifica in nome_lista_presidentes:
        #                       return verifica == True
        #               else:
        #                       return verifica == False
        #               print(type(verifica))
