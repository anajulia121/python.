import time
def operacao_lenta():
    time.sleep(2)
    return "operecação concluida"
inicio=time.time()
resultado=operacao_lenta()
fim=time.time()
print(f"tempo de execução: {fim-inicio} segundos")