# Bloco do n8n: Limpar espaços dos relatos
# Executado pelo nó Code do n8n, que fornece as entradas do fluxo.

resultados = []
for item in _items:
    relato = dict(item["json"])
    for campo in ("protocolo", "codigo_caso", "descricao"):
        valor = relato.get(campo)
        if isinstance(valor, str):
            relato[campo] = valor.strip()
    resultados.append({"json": relato})
return resultados
