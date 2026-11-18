# Bloco do n8n: Gerar auditoria
# Executado pelo nó Code do n8n, que fornece as entradas do fluxo.

dados = _items[0]["json"]

validacoes = []

for indice, relato in enumerate(dados["resultados"], start=1):
    validacoes.append({
        "item_resultado": indice,
        "status": relato["status"],
        "motivo": str(relato.get("motivo") or "").strip()
    })

return [{
    "json": {
        "projeto": dados["projeto"],
        "execucao_id": dados["execucao_id"],
        "registrado_em": dados["gerado_em"],
        "evento": "Triagem concluída",
        "resumo": dados["resumo"],
        "validacoes": validacoes
    }
}]
