# CHANGE LOG — Capybara AI

> Arquivo físico desta entrega: `change_log_capybara_ai.md`  
> Nome canônico do artefato: `change_log.md`  
> Status: Versão normativa final para revisão do usuário.  
>
> Este documento deve ser usado em conjunto com:
>
> - `system_spec.md`
> - `technical_spec.md`
> - `implementation_plan.md`
> - `AGENTS.md`
>
> As referências internas usam os nomes canônicos dos artefatos, sem o sufixo físico desta entrega.

---

## 1. Finalidade do change log

Este documento preserva a rastreabilidade das decisões, mudanças estruturais, retornos de etapa e ajustes relevantes ocorridos durante a especificação do **Capybara AI**.

Toda mudança que impacte escopo, V1, arquitetura, providers, MCP, configuração, segurança, ambiente, GitHub, documentação, testes, nome, empacotamento ou autonomia do implementador deve ser registrada aqui.

O implementador deve atualizar este arquivo sempre que houver:

- alteração de escopo;
- mudança estrutural;
- mudança crítica;
- mudança evolutiva;
- reclassificação de adapter;
- mudança de tecnologia;
- alteração de política de configuração;
- decisão sobre licença;
- necessidade de dependência nova;
- bloqueio de implementação;
- desvio autorizado das specs;
- retorno formal para revisão;
- alteração de status de provider;
- alteração de maturidade MCP;
- publicação ou preparação de release.

---

## 2. Tipos de mudança

As mudanças devem ser classificadas como:

| Tipo | Definição |
|---|---|
| Local | Afeta detalhe isolado sem alterar arquitetura, V1 ou contratos |
| Estrutural | Afeta arquitetura, módulos, contratos, configuração, providers, routing, MCP ou ambiente |
| Crítica | Afeta segurança, credenciais, permissões, V1, handoff, GitHub, runtime ou risco de comportamento indevido |
| Evolutiva | Propõe extensão futura fora da V1 ou melhoria planejada |
| Corretiva | Corrige decisão anterior, ambiguidade ou inconsistência |
| Operacional | Afeta processo de implementação, ambiente, Git, GitHub, documentação ou testes |
| Normativa | Afeta regras, critérios de aceite, contratos ou limites do implementador |

---

## 3. Estados de mudança

| Status | Significado |
|---|---|
| Proposta | Mudança registrada, ainda não aprovada |
| Aprovada | Mudança aceita e pronta para incorporação |
| Incorporada | Mudança já refletida nos artefatos normativos |
| Rejeitada | Mudança recusada com justificativa |
| Bloqueada | Mudança depende de decisão, evidência ou acesso externo |
| Adiada | Mudança válida, mas fora da V1 |
| Substituída | Mudança foi superada por decisão posterior |

---

## 4. Regras normativas de gestão de mudança

### 4.1 Mudança não registrada não existe

Qualquer alteração relevante que não esteja registrada neste arquivo não deve ser tratada como autorizada.

---

### 4.2 Mudança estrutural exige retorno formal

Mudanças que afetem arquitetura, contratos, providers, configuração, MCP, permissões, ambiente, GitHub, empacotamento ou V1 exigem retorno formal à etapa FSDI apropriada.

---

### 4.3 Mudança crítica bloqueia implementação até decisão

Mudanças críticas não podem ser resolvidas por inferência do implementador.

O implementador deve:

1. parar o ponto afetado;
2. registrar a mudança;
3. classificar o impacto;
4. indicar artefatos afetados;
5. propor retorno formal;
6. aguardar decisão ou regra explícita.

---

### 4.4 Reclassificação de adapter é mudança rastreável

Se um adapter mudar de status, isso deve ser registrado.

Status possíveis:

- `real`
- `experimental`
- `contract`
- `mock`

Exemplo:

```text
Gemini: experimental → real
```

Essa alteração deve indicar:

- evidência usada;
- documentação oficial consultada;
- dependências adicionadas;
- testes adicionados;
- riscos remanescentes;
- impacto no README;
- impacto em `docs/`;
- impacto no capability registry.

---

### 4.5 Licença definida

A licença do Capybara AI foi definida como MIT em 2026-05-12.

O implementador não deve alterar a licença sem decisão explícita e registro neste arquivo.

Antes de release pública madura, a licença deve estar refletida em:

- `LICENSE`;
- `README.md`;
- `docs/`;
- metadata de pacote quando aplicável.

---

### 4.6 Mudança em GitHub exige regra de conector

Qualquer operação de GitHub deve respeitar:

```text id="u2egj9"
usar: github-mcp
não usar: mcp__codex_apps__github
```

Se houver tentativa, necessidade ou sugestão de usar `mcp__codex_apps__github`, isso deve ser registrado como desvio crítico e rejeitado, salvo mudança normativa explícita futura.

---

### 4.7 Mudança em ambiente deve preservar fluxo base

O fluxo base da V1 é:

```text id="fgo6o0"
.venv + pyproject.toml + pip install -e ".[dev]"
```

Mudanças que tornem Poetry obrigatório, `uv` obrigatório ou outro gerenciador obrigatório devem ser tratadas como mudança estrutural e não podem ser aplicadas sem revisão.

---

### 4.8 Mudança em MCP exige análise de permissão

Toda mudança que amplie uso de MCP, tools, escrita, edição ou execução externa deve registrar:

- escopo;
- permissões;
- tipo de operação;
- risco;
- rastreabilidade;
- testes obrigatórios;
- impacto na política de allowlist.

---

### 4.9 Mudança em multimodalidade exige análise anti-falsificação

Toda mudança que envolva OCR, parsing, transcrição, conversão, extração ou transformação multimodal deve registrar:

- se é suporte nativo ou pipeline;
- se o pipeline é explícito;
- como será rastreado;
- quais modelos/providers serão afetados;
- quais testes negativos serão mantidos;
- como evitar multimodalidade falsa.

---

### 4.10 Mudança em dependências exige justificativa

Nenhuma dependência nova pode ser adicionada sem registrar:

- necessidade explícita;
- alternativa considerada;
- impacto de manutenção;
- impacto operacional;
- motivo para não implementar sem dependência;
- fase afetada;
- aprovação ou status provisório.

---

### 4.11 Mudança em nomes oficiais exige revisão

Os nomes oficiais são:

| Uso | Nome |
|---|---|
| Produto | Capybara AI |
| Instalação/PyPI | `capybara-ai` |
| Pacote/import | `capybara_ai` |

Qualquer mudança nesses nomes deve ser registrada como mudança estrutural/operacional e refletida em todos os artefatos, README, docs, exemplos, testes e packaging.

---

### 4.12 Mudança no formato de entrega dos artefatos

A entrega final ao usuário não será mais em `.zip`.

Os artefatos serão entregues um por vez, em mensagens separadas, com nomes físicos sufixados por `_capybara_ai`.

As referências internas dos artefatos continuam canônicas, sem sufixo.

---

## 5. Registro de mudanças

---

## Mudança 001 — Redefinição da V1 como completa em identidade

| Campo | Valor |
|---|---|
| Origem | Usuário |
| Tipo | Estrutural / crítica / corretiva |
| Descrição | A V1 não deve ser tratada como versão parcial, reduzida ou protótipo fraco. A V1 deve entregar a identidade essencial completa do microframework, com implementação organizada em fases internas. |
| Etapa de retorno | Etapa 0 — Classificação; Etapa 1 — Extração de intenção; Etapa 2 — Descoberta guiada |
| Arquivos impactados | `system_spec.md`, `technical_spec.md`, `implementation_plan.md`, `AGENTS.md`, `change_log.md` |
| Impacto na V1 | Alto |
| Decisão | Incorporar todos os pilares essenciais na V1 |
| Status | Incorporada |

### Justificativa

A interpretação anterior de V1 como parcial poderia descaracterizar o projeto e levar o implementador a entregar apenas um núcleo mínimo sem providers, MCP, roteamento ou multimodalidade.

### Regra incorporada

A V1 deve incluir:

- core provider-agnostic;
- capability registry;
- validação automática por capabilities;
- roteamento automático;
- agentes configuráveis;
- contexto multimodal;
- bloqueio de multimodalidade falsa;
- adapters para múltiplos providers;
- suporte inicial real a MCP;
- estrutura extensível;
- documentação, exemplos, testes e preparação para GitHub.

### Consequência operacional

As fases de implementação são fases internas da V1, não versões futuras.

---

## Mudança 002 — Inclusão do AGENTS.md como artefato operacional

| Campo | Valor |
|---|---|
| Origem | Usuário |
| Tipo | Estrutural / operacional |
| Descrição | A entrega final deve incluir `AGENTS.md` como arquivo de entrada operacional para o implementador, permitindo que o prompt inicial ao Codex seja reduzido a: `Consuma e obedeça o AGENTS.md.` |
| Etapa de retorno | Etapa 2 — Descoberta guiada |
| Arquivos impactados | `AGENTS.md`, `implementation_plan.md`, `technical_spec.md`, `system_spec.md` |
| Impacto na V1 | Alto |
| Decisão | Criar `AGENTS.md` como guia operacional, sem substituir as specs normativas |
| Status | Incorporada |

### Justificativa

O implementador precisa de uma entrada operacional enxuta, mas forte, que o obrigue a consumir os artefatos normativos antes de implementar.

### Regra incorporada

O `AGENTS.md` deve conter:

- papel do implementador;
- ordem obrigatória de leitura;
- obrigação de obedecer specs;
- limites de autonomia;
- proibição de improviso;
- regra de dúvidas e desvios;
- política de perda de contexto;
- uso de subagentes;
- divisão de tarefas;
- ambiente `.venv`;
- GitHub via `github-mcp`.

---

## Mudança 003 — MCP flexível com permissões explícitas

| Campo | Valor |
|---|---|
| Origem | Usuário |
| Tipo | Estrutural / crítica |
| Descrição | O framework deve permitir MCPs conforme configuração do desenvolvedor, sem bloquear usos legítimos, mas também sem executar tools implicitamente ou sem contrato. |
| Etapa de retorno | Etapa 2 — Descoberta guiada; Etapa 3 — Validação |
| Arquivos impactados | `system_spec.md`, `technical_spec.md`, `implementation_plan.md`, `AGENTS.md` |
| Impacto na V1 | Alto |
| Decisão | MCP entra na V1 com configuração explícita, allowlist, escopo, permissões e rastreabilidade |
| Status | Incorporada |

### Justificativa

MCP pode conectar agentes a apps, sistemas, ferramentas, arquivos, dados e permissões externas. O framework não deve decidir moralmente o uso, mas deve exigir clareza arquitetural e operacional.

### Regra incorporada

Toda tool MCP deve declarar:

- origem;
- escopo;
- leitura;
- escrita;
- edição;
- execução externa;
- mutação de estado;
- permissões;
- política de erro;
- rastreabilidade.

### Proibições

O framework não deve:

- executar MCP sem configuração;
- executar tool não allowlisted;
- assumir MCP seguro por padrão;
- ocultar escrita, edição ou execução externa;
- executar fallback via MCP sem autorização.

---

## Mudança 004 — Regra anti-multimodalidade falsa

| Campo | Valor |
|---|---|
| Origem | Usuário |
| Tipo | Estrutural / crítica |
| Descrição | O framework não deve fingir suporte multimodal por OCR, parsing, transcrição ou conversão implícita. |
| Etapa de retorno | Etapa 2 — Descoberta guiada; Etapa 3 — Validação |
| Arquivos impactados | `system_spec.md`, `technical_spec.md`, `implementation_plan.md`, `AGENTS.md` |
| Impacto na V1 | Alto |
| Decisão | Multimodalidade exige suporte nativo do modelo ou pipeline explícito configurado pelo dev |
| Status | Incorporada |

### Justificativa

A identidade do framework depende de respeitar capabilities reais dos modelos/providers.

### Regra incorporada

Se o modelo não suporta nativamente o tipo de contexto, o framework deve:

- bloquear; ou
- exigir pipeline explícito configurado pelo desenvolvedor.

### Proibições

A V1 não deve executar automaticamente:

- OCR;
- extração de PDF;
- transcrição de áudio;
- análise de vídeo;
- conversão multimodal;
- envio parcial de contexto;
- fallback textual invisível.

---

## Mudança 023 — Nome definitivo do microframework

| Campo | Valor |
|---|---|
| Origem | Usuário |
| Tipo | Estrutural / operacional / normativa |
| Descrição | O nome definitivo do microframework foi fechado como Capybara AI. |
| Etapa de retorno | Gestão de mudança após crítica adversarial |
| Arquivos impactados | Todos os artefatos, futuro README, futura documentação, packaging, exemplos, testes |
| Impacto na V1 | Alto |
| Decisão | Usar Capybara AI como nome de produto, `capybara-ai` como nome de instalação/PyPI e `capybara_ai` como pacote/import |
| Status | Incorporada |

### Nomes oficiais

| Uso | Nome |
|---|---|
| Produto | Capybara AI |
| Instalação/PyPI | `capybara-ai` |
| Pacote/import | `capybara_ai` |

### Consequência operacional

O implementador deve refletir esses nomes em:

- `pyproject.toml`;
- estrutura `src/capybara_ai/`;
- imports;
- README;
- docs;
- exemplos;
- testes;
- metadata de pacote;
- eventual repositório GitHub.

---

## Mudança 024 — Alteração do formato de entrega final dos artefatos

| Campo | Valor |
|---|---|
| Origem | Usuário |
| Tipo | Operacional / corretiva |
| Descrição | A entrega final não deve mais ser feita em `.zip`. Os cinco artefatos devem ser gerados um arquivo por vez, em mensagens separadas, para revisão e download com mais controle. |
| Etapa de retorno | Gestão de mudança após crítica adversarial |
| Arquivos impactados | Entrega final, todos os artefatos |
| Impacto na V1 | Baixo |
| Decisão | Não gerar `.zip`; gerar um arquivo por resposta; aguardar autorização antes do próximo |
| Status | Incorporada |

### Regra incorporada

A entrega deve seguir:

1. Não gerar `.zip`.
2. Não gerar os cinco arquivos de uma vez.
3. Gerar apenas um arquivo por resposta.
4. Disponibilizar cada arquivo como `.md`.
5. Aguardar autorização antes do próximo.
6. Usar sufixo físico `_capybara_ai`.
7. Manter referências internas canônicas.

### Arquivos físicos da entrega

| Artefato canônico | Arquivo físico |
|---|---|
| `system_spec.md` | `system_spec_capybara_ai.md` |
| `technical_spec.md` | `technical_spec_capybara_ai.md` |
| `implementation_plan.md` | `implementation_plan_capybara_ai.md` |
| `change_log.md` | `change_log_capybara_ai.md` |
| `AGENTS.md` | `AGENTS_capybara_ai.md` |

### Regra de referência interna

Dentro dos arquivos, as referências devem continuar usando:

- `system_spec.md`
- `technical_spec.md`
- `implementation_plan.md`
- `change_log.md`
- `AGENTS.md`

O sufixo `_capybara_ai` é apenas físico/operacional nesta entrega.

---

## Mudança 025 — Lacuna operacional no detalhamento das fases 8 a 16

| Campo | Valor |
|---|---|
| Origem | Implementador |
| Tipo | Operacional / normativa / corretiva |
| Descrição | O `implementation_plan.md` lista as etapas 8 a 16 na ordem geral de implementação, mas detalha apenas as fases 1 a 7 com objetivos, entregáveis, critérios de aceite e definição de pronto. |
| Etapa de retorno | Revisão do `implementation_plan.md` |
| Arquivos impactados | `implementation_plan.md`, auditoria final, planejamento de execução |
| Impacto na V1 | Médio/alto para declaração final de pronto; baixo para iniciar fases já especificadas |
| Decisão | Corrigir formalmente o `implementation_plan.md` antes de continuar a implementação da V1, adicionando as fases 8 a 16 com critérios normativos completos. |
| Status | Incorporada |

### Justificativa

Os contratos de agentes, runner, MCP, streaming, structured output, testes, exemplos, README, docs, Git/GitHub e auditoria final existem em `system_spec.md` e `technical_spec.md`, mas o plano não traz o mesmo nível de detalhe das fases 1 a 7.

### Risco de prosseguir

Declarar a V1 como completamente pronta sem revisar essa lacuna pode enfraquecer a rastreabilidade exigida pelos artefatos normativos.

### Correção incorporada

Em 2026-05-11, por decisão explícita do usuário, o `implementation_plan.md` foi atualizado para incluir:

- Fase 8 — Agentes configuráveis e runner;
- Fase 9 — Integração MCP inicial real;
- Fase 10 — Streaming e structured output;
- Fase 11 — Testes;
- Fase 12 — Exemplos de uso;
- Fase 13 — README público;
- Fase 14 — Documentação completa em `docs/`;
- Fase 15 — Git, GitHub e versionamento;
- Fase 16 — Auditoria final de aderência.

Cada fase passou a conter objetivo, escopo, entregáveis, dependências, critérios de aceite e definição de pronto, preservando `system_spec.md`, `technical_spec.md`, `AGENTS.md` e as decisões já registradas neste `change_log.md`.

---

## Mudança 026 — Git não disponível no PATH do ambiente local

| Campo | Valor |
|---|---|
| Origem | Implementador |
| Tipo | Operacional |
| Descrição | A verificação inicial de Git falhou porque o comando `git` não está disponível no PATH do ambiente atual. |
| Etapa de retorno | Preparação Git/GitHub |
| Arquivos impactados | Preparação Git/GitHub, auditoria final |
| Impacto na V1 | Médio para commits e inicialização de repositório; baixo para implementação local do pacote |
| Decisão | Preparar `.gitignore` e arquivos de projeto; retomar versionamento local após Git ser instalado/configurado. |
| Status | Incorporada |

### Justificativa

A V1 exige preparação para Git/GitHub, mas operações locais de Git dependem do binário disponível. Operações GitHub continuam restritas a `github-mcp` quando houver autorização.

### Atualização de validação

Em 2026-05-12, Git foi instalado no ambiente local como `git version 2.54.0.windows.1`. O repositório local foi inicializado com `git init`. O diretório precisou ser registrado como `safe.directory` porque o repo foi criado pela sessão sandbox e depois operado pelo usuário Windows.

---

## Mudança 027 — Python não instalado/registrado para criação de `.venv`

| Campo | Valor |
|---|---|
| Origem | Implementador |
| Tipo | Operacional |
| Descrição | O comando `python` não está disponível no PATH e o launcher `py` respondeu `No installed Pythons found!`, impedindo a criação local da `.venv` e a validação de `pip install -e ".[dev]"` neste ambiente. |
| Etapa de retorno | Fase 1 — Preparação do projeto e ambiente |
| Arquivos impactados | Ambiente local, validação de instalação editável, execução de testes |
| Impacto na V1 | Médio para validação local; baixo para criação dos arquivos de projeto |
| Decisão | Prosseguir com arquivos e contratos da V1; validar `.venv`, instalação editável e testes quando Python 3.11+ estiver instalado/registrado. |
| Status | Incorporada |

### Justificativa

A especificação exige Python 3.11+ e `.venv` local. Sem binário Python disponível, o implementador não pode executar a etapa operacional, mas pode preparar `pyproject.toml`, estrutura do pacote, testes, docs e exemplos para validação posterior.

### Atualização de validação

Em 2026-05-12, Python 3.12.10 foi disponibilizado. A `.venv` foi criada, `pip` foi atualizado e a instalação editável `python -m pip install -e ".[dev]"` foi executada com sucesso.

---

## Mudança 028 — Decisão controlada por dataclasses tipadas

| Campo | Valor |
|---|---|
| Origem | Implementador |
| Tipo | Operacional / técnica |
| Descrição | A implementação adotou `dataclasses` tipadas para contratos runtime em vez de Pydantic v2. |
| Etapa de retorno | Fase 2 — Core provider-agnostic |
| Arquivos impactados | Core, config, capabilities, context, routing, agents, MCP |
| Impacto na V1 | Baixo |
| Decisão | Usar biblioteca padrão para reduzir dependência estrutural e manter core leve. |
| Status | Incorporada |

### Justificativa

As specs permitem Pydantic v2 ou dataclasses tipadas. Como a V1 precisa ser microframework leve, provider-agnostic e sem dependências runtime obrigatórias, `dataclasses` atende os contratos sem adicionar dependência estrutural.

---

## Mudança 029 — SDKs opcionais restritos a adapters/conectores

| Campo | Valor |
|---|---|
| Origem | Implementador |
| Tipo | Operacional / técnica / dependência |
| Descrição | `openai` e `mcp` foram declarados como extras opcionais, não como dependências obrigatórias de runtime. |
| Etapa de retorno | Fases 5 e 9 |
| Arquivos impactados | `pyproject.toml`, providers, MCP, docs |
| Impacto na V1 | Médio |
| Decisão | Manter SDKs externos fora do core e disponíveis apenas via extras `capybara-ai[openai]` e `capybara-ai[mcp]`. |
| Status | Incorporada |

### Justificativa

A documentação oficial atual do OpenAI Responses API foi consultada para o adapter OpenAI. A documentação oficial do Model Context Protocol indica o SDK Python oficial `mcp`, com suporte a clientes e servidores. As dependências são condicionais porque testes e uso básico não devem exigir API keys ou serviços externos por padrão.

### Alternativas consideradas

- Tornar SDKs dependências obrigatórias: rejeitado por aumentar instalação base e acoplar o core.
- Implementar tudo por HTTP manual: rejeitado para V1 porque aumentaria risco de divergência das APIs oficiais.

---

## Mudança 030 — Classificação inicial dos adapters da V1

| Campo | Valor |
|---|---|
| Origem | Implementador |
| Tipo | Operacional / técnica / provider |
| Descrição | A implementação inicial declarou status explícito para todos os providers da V1. |
| Etapa de retorno | Fase 5 — Contratos de providers e adapters |
| Arquivos impactados | Providers, capability registry, README, docs, testes |
| Impacto na V1 | Alto |
| Decisão | Fake/Test como `mock`; OpenAI como `real` com SDK opcional e credencial do consumidor; Gemini e Anthropic como `experimental`; xAI, DeepSeek e Meta como `contract`. |
| Status | Incorporada |

### Justificativa

Fake/Test é funcional local e não chama serviços externos. OpenAI foi implementado em adapter isolado com base na documentação oficial atual da Responses API consultada em 2026-05-11 e depende do extra opcional `capybara-ai[openai]`. Gemini e Anthropic permanecem experimentais sem runtime SDK na instalação base. xAI, DeepSeek e Meta são contratos e não executam como providers reais.

### Riscos remanescentes

Adapters reais adicionais exigem consulta oficial atual, dependências opcionais, testes de contrato, documentação e reclassificação registrada antes de serem marcados como `real`.

---

## Mudança 031 — Validação local da V1 após correções de qualidade

| Campo | Valor |
|---|---|
| Origem | Implementador |
| Tipo | Operacional / qualidade / auditoria |
| Descrição | Após instalação local de Python/Git, a suíte de validação foi executada e os problemas de Ruff/Mypy foram corrigidos. |
| Etapa de retorno | Fases 11, 15 e 16 |
| Arquivos impactados | Código, testes, docs, Git local |
| Impacto na V1 | Alto |
| Decisão | Considerar validação local técnica aprovada. Licença ainda não havia sido definida nesta validação e foi resolvida posteriormente pela Mudança 032. |
| Status | Incorporada |

### Resultados

- Python: `Python 3.12.10`.
- Git: `git version 2.54.0.windows.1`.
- `.venv`: criada.
- Instalação editável: `python -m pip install -e ".[dev]"` concluída com sucesso.
- `pytest`: `12 passed`.
- `ruff check .`: aprovado.
- `ruff format --check .`: aprovado.
- `mypy src`: aprovado, sem issues em 52 arquivos.

### Pendências na data da validação

- Operações remotas GitHub não foram executadas; se autorizadas, devem usar `github-mcp`.

---

## Mudança 032 — Licença MIT definida

| Campo | Valor |
|---|---|
| Origem | Usuário |
| Tipo | Normativa / operacional / licença |
| Descrição | A licença do Capybara AI foi definida como MIT. |
| Etapa de retorno | Fase 13, Fase 14, Fase 15 e Fase 16 |
| Arquivos impactados | `LICENSE`, `README.md`, `docs/`, `pyproject.toml`, `change_log.md`, `docs/audit.md` |
| Impacto na V1 | Alto |
| Decisão | Criar `LICENSE` com a licença MIT e refletir a decisão na documentação e metadata do pacote. |
| Status | Incorporada |

### Resultado

- `LICENSE` criado com a licença MIT.
- `README.md` atualizado para declarar MIT.
- `docs/` atualizado para remover bloqueio atual de licença.
- `pyproject.toml` atualizado com `license = "MIT"` e classificador MIT.
- `docs/audit.md` atualizado para registrar a validação de licença.

### Regra preservada

GitHub deve continuar usando `github-mcp` quando autorizado. O conector `mcp__codex_apps__github` continua proibido.

---

## Mudança 033 — Repositório GitHub criado via `github-mcp`

| Campo | Valor |
|---|---|
| Origem | Usuário / Implementador |
| Tipo | Operacional / GitHub / publicação |
| Descrição | O repositório GitHub remoto foi criado usando exclusivamente `github-mcp`; o envio completo do conteúdo permanece pendente de uma forma autorizada que preserve as regras operacionais. |
| Etapa de retorno | Fase 15 — Git, GitHub e versionamento |
| Arquivos impactados | Repositório remoto GitHub, `change_log.md` |
| Impacto na V1 | Alto |
| Decisão | Criar o repositório em `https://github.com/higordsantos5-rgb/capybara-ai` via `github-mcp`. |
| Status | Incorporada |

### Resultado

- Repositório remoto criado via `github-mcp`: `higordsantos5-rgb/capybara-ai`.
- URL: `https://github.com/higordsantos5-rgb/capybara-ai`.
- Ferramenta usada: `github-mcp`.
- Conector proibido `mcp__codex_apps__github` não foi usado.
- `.env` e `.venv/` permanecem protegidos por `.gitignore` e não devem ser publicados.

### Pendência operacional

O push direto por Git preservaria o histórico local, mas foi bloqueado pela política porque a publicação remota deve ocorrer via `github-mcp`. O envio integral de todos os arquivos ao remoto deve ser concluído apenas por caminho autorizado.

---

## Mudança 034 — Ajuste de metadata de licença para build Python

| Campo | Valor |
|---|---|
| Origem | Implementador |
| Tipo | Operacional / empacotamento |
| Descrição | O build com setuptools atual rejeitou o classificador `License :: OSI Approved :: MIT License` quando `license = "MIT"` já estava definido. |
| Etapa de retorno | Preparação de publicação Python |
| Arquivos impactados | `pyproject.toml`, `change_log.md` |
| Impacto na V1 | Baixo |
| Decisão | Remover o classificador de licença e manter a expressão `license = "MIT"`, alinhada ao comportamento atual do setuptools/PEP 639. |
| Status | Incorporada |

### Resultado

O metadata de licença permanece MIT e o empacotamento passa a usar a forma aceita pelo backend de build atual.

---

## Mudança 035 — Checklist local de empacotamento Python

| Campo | Valor |
|---|---|
| Origem | Implementador |
| Tipo | Operacional / empacotamento / publicação |
| Descrição | O checklist local de preparação para publicação Python foi executado sem publicar no PyPI real. |
| Etapa de retorno | Preparação de publicação Python |
| Arquivos impactados | `pyproject.toml`, `src/capybara_ai/__init__.py`, `tests/test_core_flow.py`, `dist/` local não versionado |
| Impacto na V1 | Alto |
| Decisão | Preparar artefatos locais para TestPyPI/PyPI sem upload real até autorização explícita e GitHub completo. |
| Status | Incorporada |

### Resultados

- `pytest`: `13 passed`.
- `ruff check .`: aprovado.
- `ruff format --check .`: aprovado.
- `mypy src`: aprovado, sem issues em 52 arquivos.
- `python -m pip install --upgrade build twine`: concluído.
- `python -m build`: gerou `capybara_ai-0.1.0.tar.gz` e `capybara_ai-0.1.0-py3-none-any.whl`.
- `python -m twine check dist/*`: aprovado para wheel e sdist.
- Instalação do wheel em ambiente limpo `test-capybara-install`: concluída.
- `python -c "import capybara_ai; print(capybara_ai.__version__)"`: retornou `0.1.0`.

### Pendências antes de publicação real

- Concluir publicação integral do conteúdo no GitHub por caminho autorizado.
- Preparar TestPyPI antes de PyPI real.
- Preferir Trusted Publishing via GitHub Actions para PyPI real.
- Não publicar no PyPI real sem autorização explícita.

---

## Mudança 036 — Public documentation and DX polish before GitHub publication

| Campo | Valor |
|---|---|
| Origem | Usuário |
| Tipo | Operacional / documental / DX |
| Descrição | A documentação pública foi reescrita e reorganizada para ser mais clara, amigável e orientada ao usuário final antes da publicação GitHub completa. |
| Etapa de retorno | Fase 13, Fase 14 e Fase 16 |
| Arquivos impactados | `README.md`, `docs/`, `examples/`, `change_log.md`, `docs/audit.md` |
| Impacto na V1 | Médio |
| Decisão | Melhorar README, criar documentação pública em camadas e adicionar exemplos práticos sem alterar artefatos normativos internos. |
| Status | Incorporada |

### Resultado

- README reescrito como vitrine pública do framework.
- `docs/` reorganizado com camadas `getting-started/`, `guides/`, `reference/` e `internal/`.
- Quickstart humano criado em `docs/getting-started/quickstart.md`.
- Exemplos adicionados para roteamento por capabilities, bloqueio multimodal, MCP allowlisted/denied e erro estruturado.
- `docs/audit.md` atualizado para registrar o polimento público/DX.

### Regra preservada

Os artefatos normativos internos `system_spec.md`, `technical_spec.md`, `implementation_plan.md`, `change_log.md`, `AGENTS.md` e `docs/audit.md` não tiveram suas regras normativas alteradas. O polimento mudou apresentação pública e onboarding.

---

## Mudança 037 — Site público de documentação com deploy Vercel

| Campo | Valor |
|---|---|
| Origem | Usuário |
| Tipo | Operacional / documental / deploy |
| Descrição | Foi adicionada uma camada web separada em `site/` para publicar README e `docs/**/*.md` como site público de documentação. |
| Etapa de retorno | Documentação pública e publicação |
| Arquivos impactados | `site/`, `vercel.json`, `.vercelignore`, `.gitignore`, `change_log.md` |
| Impacto na V1 | Baixo no pacote Python; alto para documentação pública |
| Decisão | Usar Next.js + TypeScript + App Router como camada web isolada, mantendo o pacote Python preservado. Deploy deve ocorrer via Vercel MCP, sem GitHub como requisito desta tarefa. |
| Status | Incorporada |

### Justificativa

O site precisa transformar `README.md` e `docs/**/*.md` em rotas públicas, com landing page, navegação, conversão de links Markdown e deploy direto na Vercel. A camada web foi isolada em `site/` para não misturar empacotamento Python com frontend.

### Dependências web adicionadas

- `next`, `react`, `react-dom`;
- `react-markdown`, `remark-gfm`;
- `typescript`, `eslint`, `eslint-config-next` e tipos React/Node para desenvolvimento.

### Alternativas consideradas

- Site estático manual: rejeitado porque dificultaria rotas automáticas e manutenção a partir de `docs/**/*.md`.
- GitHub Pages ou deploy por GitHub: rejeitado nesta tarefa porque o requisito é deploy direto via Vercel MCP sem GitHub obrigatório.

### Regras preservadas

- O pacote Python e sua API não foram alterados.
- `README.md` e `docs/**/*.md` continuam como fonte de conteúdo.
- `.env`, `.venv/`, `node_modules/` e `.next/` continuam ignorados.
- `.vercelignore` limita o upload Vercel a `site/`, `README.md`, `docs/`, `LICENSE`, `package.json` e `vercel.json`.
- O status do pacote permanece honesto: V1 validada localmente e release PyPI em preparação.
- GitHub não é requisito desta tarefa e o conector proibido `mcp__codex_apps__github` não foi usado.

### Bloqueio de deploy

Em 2026-05-12, a primeira tentativa de deploy via Vercel MCP foi recusada por risco de publicar conteúdo amplo do workspace. Após adicionar `.vercelignore` com allowlist de arquivos públicos, nova tentativa via Vercel MCP não publicou o projeto e retornou instrução para usar `vercel deploy` pela CLI ou integração Git.

Como a tarefa exige deploy exclusivamente via Vercel MCP e não GitHub como requisito, a publicação fica bloqueada até autorização para um caminho alternativo ou disponibilidade de deploy direto no conector.

### Publicação final autorizada

Em 2026-05-12, o usuário autorizou explicitamente o caminho alternativo indicado pelo próprio conector Vercel: `vercel deploy` via Vercel CLI.

Execução realizada:

- `npx vercel link --yes --project capybara-ai`;
- `npx vercel deploy --prod --yes`.

Resultado:

- projeto Vercel criado/vinculado: `capybara-ai`;
- deployment final em estado `Ready`;
- URL pública final: `https://capybara-ai-xi.vercel.app`;
- build remoto executou `cd site && npm install` e `cd site && npm run build`;
- build remoto gerou 35 páginas estáticas;
- `npm audit` remoto reportou `found 0 vulnerabilities`;
- rotas públicas verificadas por HTTP com status `200`: `/`, `/docs`, `/docs/installation`, `/docs/getting-started/quickstart`, `/docs/guides/capability-routing`, `/docs/reference/errors`, `/docs/internal/release-audit`.

Observações:

- o deploy final não dependeu de GitHub;
- a Vercel CLI tentou detectar/conectar automaticamente o repositório GitHub durante o link inicial, mas essa conexão falhou e não foi usada como requisito de publicação;
- nenhum token Vercel foi salvo no repositório;
- `.vercel/` foi adicionada ao `.gitignore`;
- foi adicionado `package.json` mínimo na raiz apenas para detecção do Next.js pela Vercel, mantendo a aplicação real e dependências principais em `site/`.

---

## 11. Status deste change log

Este `change_log.md` incorpora:

- descoberta inicial;
- mudanças estruturais;
- ajustes pós-simulação;
- crítica adversarial;
- fechamento do nome Capybara AI;
- alteração do formato de entrega;
- decisão de Python 3.11+;
- decisão de ferramentas dev base;
- licença MIT definida.

O arquivo físico desta entrega é:

```text id="hj261v"
change_log_capybara_ai.md
```

Dentro do conteúdo normativo, as referências permanecem canônicas:

```text id="q5dvjh"
system_spec.md
technical_spec.md
implementation_plan.md
change_log.md
AGENTS.md
```

Essa regra é operacional da entrega, não altera a identidade normativa dos artefatos.
