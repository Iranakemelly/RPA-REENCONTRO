# Bloco do n8n: Gerar resumo do lote vazio
# Executado pelo nó Code do n8n, que fornece as entradas do fluxo.

dados = _items[0]["json"]

return [{
    "json": {
        "projeto": "Reencontra",
        "execucao_id": str(dados["resumo_execucao_id"]).strip(),
        "gerado_em": dados["resumo_gerado_em"],
        "mensagem": "Nenhum relato recebido para processamento.",
        "resumo": {
            "recebidos": 0,
            "aguardando_revisao": 0,
            "precisam_correcao": 0,
            "duplicados_removidos": 0,
            "total_resultados": 0
        },
        "resultados": []
    }
}]
