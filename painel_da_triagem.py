# Bloco do n8n: Painel da triagem
# Executado pelo nó Code do n8n, que fornece as entradas do fluxo.

dados = _items[0]["json"]
resumo = dados["resumo"]

def linha(tipo, protocolo="", caso="", situacao="", motivo=""):
    return {"json": {
        "Tipo": tipo,
        "Protocolo": protocolo,
        "Caso": caso,
        "Situação": situacao,
        "Detalhe": motivo
    }}

totais = (
    f'{resumo["recebidos"]} recebidos | '
    f'{resumo["aguardando_revisao"]} para revisão | '
    f'{resumo["precisam_correcao"]} para correção | '
    f'{resumo["duplicados_removidos"]} duplicados removidos | '
    f'{resumo["total_resultados"]} resultados'
)
linhas = [linha(
    "Resumo",
    situacao=f'Execução {dados["execucao_id"]}',
    motivo=totais
)]

for relato in dados["resultados"]:
    linhas.append(linha(
        "Relato",
        protocolo=relato.get("protocolo") or "—",
        caso=relato.get("codigo_caso") or "—",
        situacao=relato["status"],
        motivo=relato.get("motivo") or ""
    ))

if not dados["resultados"]:
    linhas.append(linha("Aviso", situacao="Lote vazio",
                        motivo=dados.get("mensagem", "Sem relatos para exibir.")))

return linhas
