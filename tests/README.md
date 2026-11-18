# Testes da automação Reencontro

Os testes usam relatos fictícios. Para reproduzir a triagem, importe o fluxo
[Demonstração da automação](../n8n/reencontro_demonstracao_automacao.json),
clique em **Execute** e abra **Painel da triagem → Tabela**.

| Cenário | O que conferir | Resultado esperado |
| --- | --- | --- |
| Relato válido | Protocolo `REL-101` | Aguardando revisão humana. |
| Descrição em branco | Protocolo `REL-102` | Precisa de correção por falta de descrição. |
| Código de caso desconhecido | Protocolo `REL-103` | Precisa de correção porque o código do caso não consta na base. |
| Protocolo duplicado | Contagens do lote | Quatro relatos recebidos, um duplicado removido e três resultados. |
| Integração com o painel | Baixe o JSON no nó **Exportar resultados JSON** e selecione-o no painel publicado. | O painel exibe o ID da execução, as contagens e os relatos classificados. |

## Evidências

- **Execução 41** · Triagem do lote fictício no n8n.
- **Execução 209** · Resultado exibido no [painel de triagem](../assets/painel-triagem.png).
- **Execução 127** · Registro de uma falha controlada pelo fluxo de erros.
