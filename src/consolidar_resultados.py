# Bloco do n8n: Consolidar resultados
# Executado pelo nó Code do n8n, que fornece as entradas do fluxo.

metadados = _items[0]["json"]

recebidos = int(metadados["total_recebidos"])
execucao_id = str(metadados["resumo_execucao_id"]).strip()
gerado_em = str(metadados["resumo_gerado_em"]).strip()

resultados = []

for item in _items:
    relato = dict(item["json"])

    relato.pop("total_recebidos", None)
    relato.pop("resumo_gerado_em", None)
    relato.pop("resumo_execucao_id", None)

    resultados.append(relato)

aguardando_revisao = sum(
    1 for relato in resultados
    if relato.get("status") == "Aguardando revisão humana"
)

precisam_correcao = sum(
    1 for relato in resultados
    if relato.get("status") == "Precisa de correção"
)

return [{
    "json": {
        "projeto": "Reencontra",
        "execucao_id": execucao_id,
        "gerado_em": gerado_em,
        "resumo": {
            "recebidos": recebidos,
            "aguardando_revisao": aguardando_revisao,
            "precisam_correcao": precisam_correcao,
            "duplicados_removidos": recebidos - len(resultados),
            "total_resultados": len(resultados)
        },
        "resultados": resultados
    }
}]
