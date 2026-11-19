# RPA REENCONTRO-SP
Automação de triagem de relatos do Reencontro — FIAP CitizenTech.

O Reencontro é uma CitizenTech de apoio à busca de pessoas desaparecidas, desenvolvida para a Global Solution FIAP 2026.2. A automação reduz a conferência manual de relatos ao identificar campos incompletos, códigos de caso fora da base e protocolos repetidos. Os relatos válidos ficam aguardando revisão humana.

#Integrantes

Irana Kemelly Pereira RM-98593

Lucas Vinicius Candido RM-98480

Mariana Melo RM-98121


 #Arquitetura

Entrada no n8n. O fluxo carrega relatos fictícios com protocolo, código do caso e descrição, além de uma base de 100 códigos fictícios.

Triagem no n8n e em Python. O fluxo verifica os campos e o código do caso, remove protocolos repetidos entre os relatos válidos do lote e registra a situação e o motivo de cada decisão. A versão de demonstração também remove espaços extras dos campos.

Saídas em JSON. O fluxo gera resultado_reencontra.json e log_auditoria_reencontra.json. Um fluxo separado registra falhas técnicas.

Painel na Vercel. A pessoa responsável seleciona o arquivo de resultado. O JavaScript lê o JSON no navegador e exibe o ID da execução, as contagens e os relatos classificados.

O ambiente local usa Docker para executar o n8n e um executor Python externo da mesma versão. O painel usa HTML, CSS e JavaScript.

#Como executar

Inicie o n8n e o executor Python no Docker. Abra o n8n em http://localhost:5678 se estiver usando a porta padrão.

No editor, use ⋯ → Import from File para importar reencontro_triagem_organizada.json ou reencontro_demonstracao_automacao.json.

Clique em Execute e confira o bloco Painel da triagem → Saída → Tabela. O lote de exemplo tem quatro relatos recebidos, um para revisão, dois para correção e um duplicado removido, totalizando três resultados.

Abra Exportar resultados JSON → Saída → Binário → Download. No painel publicado, clique em Escolher arquivo e selecione o resultado_reencontra.json gerado nessa execução.

Para testar o registro de falhas em outra instalação, importe também o fluxo Registro de falhas e selecione-o nas configurações do fluxo principal, no campo Error Workflow.

#Evidências e privacidade

A execução 209 demonstrou a integração por arquivo com o painel. A execução 41 demonstrou a limpeza e as decisões da triagem. A falha controlada da execução 127 foi registrada pelo fluxo de erros. Use apenas dados fictícios nas demonstrações e mantenha credenciais e dados pessoais fora do repositório público.

## Fluxos da automação no n8n

- [Triagem organizada](n8n/reencontro_triagem_organizada.json) — fluxo principal de validação e classificação dos relatos.
- [Demonstração da automação](n8n/reencontro_demonstracao_automacao.json) — fluxo de demonstração da limpeza e classificação dos relatos.

Para executar um fluxo, baixe o arquivo JSON, importe-o no editor do n8n e clique em **Execute**. No nó **Painel da triagem**, abra a aba **Tabela** para conferir o resultado.

#Links

Painel de triagem na Vercel[ https://reencontro-citizentech-navy.vercel.app/]

Site principal do Reencontro: [https://reencontro-site.vercel.app/]

Vídeo demonstrativo: [https://youtu.be/ZFaiuGo3y5Y]
