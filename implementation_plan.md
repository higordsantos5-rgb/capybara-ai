# IMPLEMENTATION PLAN — Capybara AI

> Arquivo físico desta entrega: `implementation_plan_capybara_ai.md`  
> Nome canônico do artefato: `implementation_plan.md`  
> Status: Versão normativa final para revisão do usuário.  
>
> Este documento deve ser usado em conjunto com:
>
> - `system_spec.md`
> - `technical_spec.md`
> - `change_log.md`
> - `AGENTS.md`
>
> As referências internas usam os nomes canônicos dos artefatos, sem o sufixo físico desta entrega.

---

## 1. Estratégia geral

### 1.1 Objetivo do plano

Este documento define a estratégia normativa de implementação da V1 do **Capybara AI**.

A V1 deve entregar a identidade essencial completa do microframework:

- core provider-agnostic;
- capability registry;
- validação automática por capabilities;
- roteamento automático;
- agentes configuráveis;
- contexto multimodal;
- bloqueio de multimodalidade falsa;
- integração com múltiplos providers;
- suporte inicial real a MCP quando tecnicamente viável;
- configuração explícita por projeto;
- documentação, exemplos, testes e preparação para GitHub.

A V1 NÃO deve ser tratada como:

- protótipo fraco;
- MVP descaracterizado;
- wrapper de SDK;
- chatbot web;
- subconjunto mínimo que adia a identidade principal para versões futuras.

A implementação deve ser dividida em fases internas. Todas as fases descritas neste plano pertencem à entrega da V1.

---

## 2. Princípios de implementação

### 2.1 V1 completa em identidade

A V1 deve ser considerada completa quando todos os pilares essenciais do Capybara AI estiverem implementados, testados e documentados.

A V1 pode ter limitações controladas, como:

- adapters experimentais;
- adapters contratuais;
- suporte parcial de streaming por provider;
- suporte parcial de structured output por provider;
- ausência de graph engine;
- ausência de multiagente avançado;
- ausência de memória vetorial;
- ausência de UI;
- ausência de marketplace MCP;
- ausência de observabilidade distribuída avançada.

Essas limitações não podem descaracterizar a identidade central do framework.

---

### 2.2 Implementação faseada não significa V1 parcial

As fases deste plano são uma estratégia de construção interna.

O implementador NÃO deve interpretar fases posteriores como opcionais, futuras ou fora da V1.

A V1 só será considerada pronta quando todas as fases obrigatórias deste plano forem concluídas e validadas.

---

### 2.3 Core provider-agnostic

O núcleo do framework deve permanecer independente de SDKs específicos.

O implementador NÃO deve:

- importar SDK de provider dentro do core;
- acoplar roteamento a provider específico;
- criar regra especial de provider dentro de módulos genéricos;
- tratar OpenAI, Gemini, Anthropic, xAI, DeepSeek ou Meta como comportamento nativo do core.

Providers devem ser integrados por adapters.

---

### 2.4 Capability-first

Toda execução deve ser governada por capabilities.

O implementador deve garantir que:

- capability ausente seja tratada como não suportada;
- o router só selecione modelos compatíveis e elegíveis;
- o provider não seja chamado antes da validação;
- streaming seja capability declarada;
- structured output seja capability declarada;
- multimodalidade dependa de suporte nativo ou pipeline explícito.

---

### 2.5 Separação entre suporte, configuração e runtime

O implementador deve preservar a separação entre:

1. suporte arquitetural do framework;
2. configuração explícita do projeto consumidor;
3. disponibilidade real em runtime.

Um provider pode ser suportado pelo framework e ainda assim não estar ativo em um projeto.

Um modelo pode ser conhecido pelo registry e ainda assim não estar autorizado no projeto.

Um provider/modelo configurado pode ainda não estar disponível em runtime.

O router deve operar apenas sobre modelos elegíveis.

---

### 2.6 MCP explícito e rastreável

O implementador deve permitir integração real com MCP quando tecnicamente viável, mas nenhuma tool MCP pode ser executada sem:

- configuração explícita;
- allowlist;
- escopo declarado;
- permissões declaradas;
- rastreabilidade da chamada.

O framework não deve decidir moralmente o que o desenvolvedor pode fazer com MCP, mas deve exigir clareza operacional.

---

### 2.7 Multimodalidade real ou pipeline explícito

O framework não deve fingir suporte multimodal.

Se o modelo não suporta nativamente imagem, áudio, vídeo, PDF ou outro tipo de contexto, o framework deve:

- bloquear a execução; ou
- exigir pipeline explícito configurado pelo desenvolvedor.

A V1 não deve implementar automaticamente:

- OCR;
- extração de PDF;
- transcrição de áudio;
- análise de vídeo;
- conversão multimodal;
- resumo automático;
- fallback textual invisível.

---

### 2.8 Ambiente local obrigatório

O projeto deve usar:

```text
.venv + pyproject.toml + pip install -e ".[dev]"
```

Regras:

- `.venv` deve existir na raiz do repositório durante desenvolvimento local;
- `.venv/` deve estar no `.gitignore`;
- `pyproject.toml` é obrigatório;
- Python mínimo: 3.11+;
- Poetry não deve ser dependência obrigatória da V1;
- `uv` pode ser mencionado como alternativa opcional futura;
- `.env.example` deve existir;
- `.env` real não deve ser versionado.

---

## 3. Ordem geral de implementação

A implementação da V1 deve seguir esta ordem:

1. Preparação do ambiente e estrutura do projeto.
2. Core provider-agnostic.
3. Capability registry.
4. Contexto multimodal.
5. Contratos de providers e adapters.
6. Configuração explícita por projeto.
7. Roteamento automático.
8. Agentes configuráveis e runner.
9. Integração MCP.
10. Streaming e structured output como contracts/capabilities.
11. Testes unitários, de contrato e integração.
12. Exemplos.
13. README público.
14. Documentação completa em `docs/`.
15. Preparação Git/GitHub.
16. Auditoria final de aderência.

Essa ordem não deve ser alterada sem justificativa registrada no `change_log.md`.

---

## 4. Fases internas da V1

---

# Fase 1 — Preparação do projeto e ambiente

## Objetivo

Criar a base operacional do projeto Python, garantindo ambiente reproduzível, estrutura inicial e preparação para desenvolvimento local.

## Escopo

Inclui:

- criação da estrutura de diretórios;
- criação/verificação de `.venv`;
- criação de `pyproject.toml`;
- configuração de instalação editável;
- configuração de Python 3.11+;
- criação de `.gitignore`;
- criação de `.env.example`;
- organização inicial de `src/`, `tests/`, `docs/` e `examples/`;
- validação de que o projeto pode ser instalado em modo desenvolvimento.

Não inclui:

- implementação de providers reais;
- documentação completa;
- publicação no GitHub.

## Entregáveis

- Estrutura inicial do projeto.
- `.venv` local criado ou instrução clara para criação.
- `pyproject.toml`.
- `.gitignore`.
- `.env.example`.
- Diretórios:
  - `src/`
  - `tests/`
  - `docs/`
  - `examples/`

- Instalação local funcional com:

```bash
pip install -e ".[dev]"
```

## Dependências

Nenhuma fase anterior.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Ambiente novo | Projeto deve permitir criação de `.venv` | Verificação manual ou documentação |
| Python | Projeto exige Python 3.11+ | Revisão do `pyproject.toml` |
| Instalação dev | `pip install -e ".[dev]"` deve funcionar | Execução local |
| `.env` real | Não deve ser versionado | Revisão de `.gitignore` |
| `.env.example` | Deve listar variáveis esperadas sem valores reais | Revisão de arquivo |
| Poetry | Não deve ser obrigatório | Auditoria de dependências |
| Estrutura `src/` | Pacote deve ser importável como `capybara_ai` | Teste de import mínimo |
| Nome PyPI | Distribuição deve usar `capybara-ai` | Revisão do `pyproject.toml` |

## Definição de pronto

A fase está pronta quando:

- o pacote é instalável localmente;
- o ambiente dev pode ser preparado com Python/pip padrão;
- `.venv/` está ignorado;
- `.env.example` existe;
- `.env` real não é versionado;
- `capybara_ai` é importável;
- `capybara-ai` está configurado como nome de distribuição;
- o projeto possui estrutura compatível com testes, docs e exemplos.

---

# Fase 2 — Core provider-agnostic

## Objetivo

Implementar os tipos, contratos e erros fundamentais do framework sem dependência de providers externos.

## Escopo

Inclui:

- tipos centrais;
- erros centrais;
- contratos conceituais;
- representações de provider, modelo, capability, contexto, request, response e execução;
- estruturas mínimas para metadata de execução;
- base para resultados estruturados.

Não inclui:

- SDKs externos;
- adapters reais;
- chamadas a providers;
- MCP real;
- persistência.

## Entregáveis

Módulos conceituais esperados:

- `capybara_ai.core`
- `capybara_ai.core.errors`
- `capybara_ai.core.types`
- `capybara_ai.core.execution`
- `capybara_ai.core.metadata`

## Dependências

Fase 1.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Import do core | Core deve importar sem SDK externo | Teste unitário |
| Erros centrais | Erros devem ser distintos e rastreáveis | Teste unitário |
| Metadata mínima | Execução deve comportar provider, modelo, capabilities e bloqueios | Teste unitário |
| Provider externo | Core não deve depender de SDK externo | Auditoria de imports |
| Estado indefinido | Não deve haver estado criado fora da spec | Revisão de tipos |
| Resultado | Deve suportar sucesso, erro e bloqueio | Teste unitário |

## Definição de pronto

A fase está pronta quando:

- o core é independente;
- os tipos centrais estão definidos;
- os erros estruturais existem;
- não há dependência direta de provider;
- testes unitários cobrem os contratos básicos.

---

# Fase 3 — Capability Registry

## Objetivo

Implementar o registry de capabilities como fonte de verdade para modelos e providers conhecidos.

## Escopo

Inclui:

- registro de providers conhecidos;
- registro de modelos conhecidos;
- declaração de capabilities;
- status de adapter/modelo;
- consulta de capabilities;
- validação de capability ausente como não suportada;
- suporte a streaming como capability;
- suporte a structured output como capability;
- origem/status da informação de capabilities.

Não inclui:

- descoberta automática online de capabilities;
- atualização automática em runtime;
- inferência por nome de modelo;
- inferência por provider;
- habilitação automática de modelos.

## Entregáveis

Módulos conceituais esperados:

- `capybara_ai.capabilities.registry`
- `capybara_ai.capabilities.model_card`
- `capybara_ai.capabilities.validation`

## Dependências

Fase 2.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Modelo registrado | Deve retornar capabilities declaradas | Teste unitário |
| Capability ausente | Deve ser tratada como não suportada | Teste unitário |
| Modelo desconhecido | Deve gerar erro ou ausência explícita | Teste unitário |
| Streaming | Deve ser capability declarável | Teste unitário |
| Structured output | Deve ser capability declarável | Teste unitário |
| Inferência por nome | Deve ser proibida | Teste negativo |
| Inferência por provider | Deve ser proibida | Teste negativo |
| Provider conhecido | Não deve significar provider ativo | Teste de separação |
| Modelo conhecido | Não deve significar modelo habilitado | Teste de separação |

## Definição de pronto

A fase está pronta quando:

- o registry é fonte explícita de capabilities;
- capabilities não são inferidas;
- modelos conhecidos não viram automaticamente modelos habilitados;
- testes negativos comprovam bloqueios.

---

# Fase 4 — Contexto multimodal

## Objetivo

Implementar a camada de contexto multimodal como abstração central da V1.

## Escopo

Inclui tipos conceituais para:

- texto;
- markdown;
- código;
- imagem;
- PDF;
- áudio;
- vídeo;
- arquivo genérico;
- recurso MCP;
- contexto derivado por pipeline explícito.

Inclui também:

- validação de tipo de contexto;
- identificação de capabilities requeridas por contexto;
- bloqueio de multimodalidade falsa;
- contrato preparado para pipelines explícitos.

Não inclui por padrão:

- OCR;
- extração automática de PDF;
- transcrição automática de áudio;
- análise automática de vídeo;
- conversão automática de arquivo;
- resumo automático de arquivo.

## Entregáveis

Módulos conceituais esperados:

- `capybara_ai.context.items`
- `capybara_ai.context.validation`
- `capybara_ai.context.pipelines`

## Dependências

- Fase 2.
- Fase 3.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Texto | Deve mapear para capability textual | Teste unitário |
| Imagem | Deve exigir capability de imagem | Teste unitário |
| PDF | Deve exigir capability de PDF nativo ou pipeline explícito | Teste unitário |
| Áudio | Deve exigir capability de áudio ou pipeline explícito | Teste unitário |
| Vídeo | Deve exigir capability de vídeo ou pipeline explícito | Teste unitário |
| Arquivo genérico | Deve ser restritivo por padrão | Teste unitário |
| OCR implícito | Deve ser proibido | Teste negativo |
| PDF parsing implícito | Deve ser proibido | Teste negativo |
| Transcrição implícita | Deve ser proibido | Teste negativo |
| Pipeline explícito | Deve ser rastreável quando configurado | Teste unitário/contrato |
| Pipeline como nativo | Deve ser proibido | Teste negativo |

## Definição de pronto

A fase está pronta quando:

- todos os tipos de contexto da V1 existem;
- o framework identifica capabilities requeridas;
- conversões implícitas são bloqueadas;
- pipelines são apenas explícitos e rastreáveis;
- contexto derivado não é tratado como suporte nativo.

---

# Fase 5 — Contratos de providers e adapters

## Objetivo

Implementar a arquitetura de providers, garantindo múltiplos adapters sem acoplamento ao core e sem falso suporte.

## Escopo

Inclui:

- contrato base de provider;
- contrato de adapter;
- status de adapter:
  - `real`
  - `experimental`
  - `contract`
  - `mock`

- provider `Fake/Test` real obrigatório ou mock funcional obrigatório;
- adapter OpenAI real prioritário, se tecnicamente verificável;
- adapters Gemini e Anthropic reais ou experimentais;
- adapters xAI, DeepSeek e Meta experimentais ou contratuais;
- mecanismo de declaração de limitações por adapter;
- critério objetivo para declarar adapter `real`.

Não inclui:

- promessa de suporte completo para todos os providers;
- uso de SDK sem verificação documental;
- adapter real sem teste;
- provider ativo por padrão.

## Entregáveis

Módulos conceituais esperados:

- `capybara_ai.providers.base`
- `capybara_ai.providers.fake`
- `capybara_ai.providers.openai`
- `capybara_ai.providers.gemini`
- `capybara_ai.providers.anthropic`
- `capybara_ai.providers.xai`
- `capybara_ai.providers.deepseek`
- `capybara_ai.providers.meta`

## Dependências

- Fase 2.
- Fase 3.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Fake/Test | Deve funcionar sem API externa | Teste unitário/contrato |
| Provider real | Só pode ser real com integração verificável | Teste de contrato |
| Provider experimental | Deve declarar limitações | Teste de metadata |
| Provider contract | Não deve fingir execução real | Teste negativo |
| Adapter sem credencial | Deve falhar com erro explícito | Teste de configuração |
| SDK externo | Não pode estar no core | Auditoria de imports |
| Adapter existente | Não implica provider ativo | Teste de separação |
| Adapter `real` | Deve cumprir todos os critérios objetivos | Auditoria + teste contrato |
| Segredo | Não pode aparecer em erro/log/metadata | Teste de não vazamento |

## Definição de pronto

A fase está pronta quando:

- o contrato base está definido;
- `Fake/Test` funciona;
- adapters declaram status;
- nenhum adapter finge maturidade;
- core permanece desacoplado;
- testes de contrato existem;
- adapters reais cumprem critérios objetivos.

---

# Fase 6 — Configuração explícita por projeto

## Objetivo

Implementar a camada que separa suporte arquitetural, configuração do projeto e disponibilidade em runtime.

## Escopo

Inclui:

- configuração centralizada do projeto consumidor;
- providers habilitados;
- modelos habilitados;
- API keys por provider;
- limites de tokens/custo quando configurados;
- políticas de fallback;
- políticas de streaming;
- políticas de structured output;
- configuração MCP;
- allowlist de tools;
- status de providers/modelos;
- validação de credenciais ausentes;
- proteção contra vazamento de segredos.

Não inclui:

- API keys embutidas;
- provider ativo por padrão;
- fallback automático sem permissão;
- inferência de modelo autorizado;
- leitura mágica de secrets sem controle do dev.

## Entregáveis

Módulos conceituais esperados:

- `capybara_ai.config.project`
- `capybara_ai.config.providers`
- `capybara_ai.config.models`
- `capybara_ai.config.secrets`
- `capybara_ai.config.policies`

## Dependências

- Fase 2.
- Fase 3.
- Fase 5.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Provider suportado, não configurado | Não deve ser usado | Teste negativo |
| Modelo conhecido, não habilitado | Não deve ser roteável | Teste negativo |
| API key ausente | Deve gerar erro explícito | Teste unitário |
| Fallback ausente | Não deve ocorrer fallback | Teste negativo |
| Credencial em log | Não deve aparecer | Teste de não vazamento |
| Configuração vazia | Nenhum provider deve ficar ativo por padrão | Teste unitário |
| Provider configurado | Só entra no conjunto elegível se válido | Teste unitário |
| Modelo configurado | Só é elegível se também compatível | Teste unitário |
| Secret real | Não deve ser versionado | Auditoria `.gitignore` |

## Definição de pronto

A fase está pronta quando:

- o projeto consumidor controla providers/modelos;
- credenciais são externas ao framework;
- providers não são ativados por existência de adapter;
- segredos são protegidos;
- configuração é centralizada, explícita e testada.

---

# Fase 7 — Roteamento automático

## Objetivo

Implementar o roteador automático baseado em capabilities e elegibilidade operacional.

## Escopo

Inclui:

- derivação de capabilities requeridas;
- filtragem por providers habilitados;
- filtragem por modelos habilitados;
- filtragem por capabilities;
- filtragem por adapter status permitido;
- validação de fallback explícito;
- erro quando nenhum modelo for compatível;
- metadata de decisão de roteamento.

Políticas mínimas:

- `capability_strict`;
- `first_compatible`;
- modelo preferido com fallback explícito, se aprovado na configuração.

Não inclui:

- otimização automática de custo;
- benchmarking;
- seleção por performance histórica;
- fallback oculto;
- uso de provider não configurado.

## Entregáveis

Módulos conceituais esperados:

- `capybara_ai.routing.router`
- `capybara_ai.routing.policies`
- `capybara_ai.routing.eligibility`
- `capybara_ai.routing.errors`

## Dependências

- Fase 3.
- Fase 4.
- Fase 5.
- Fase 6.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Modelo compatível e habilitado | Pode ser selecionado | Teste unitário |
| Modelo compatível, não habilitado | Não pode ser selecionado | Teste negativo |
| Provider suportado, não configurado | Não pode ser usado | Teste negativo |
| Capability ausente | Modelo excluído | Teste unitário |
| Sem modelo compatível | Erro explícito | Teste unitário |
| Fallback não autorizado | Não deve ocorrer | Teste negativo |
| Streaming solicitado | Exige capability streaming | Teste unitário |
| Structured output solicitado | Exige capability structured_output | Teste unitário |
| Imagem enviada | Exige capability de imagem | Teste unitário |
| Adapter contract | Não pode ser usado como real | Teste negativo |

## Definição de pronto

A fase está pronta quando:

- o router opera apenas sobre modelos elegíveis;
- a separação suporte/configuração/runtime está preservada;
- não há fallback implícito;
- decisões de roteamento são rastreáveis.

---

# Fase 8 — Agentes configuráveis e runner

## Objetivo

Implementar agentes configuráveis e execução controlada por capabilities, contexto, providers e MCP.

## Escopo

Inclui:

- agente com nome, instruções, modelo preferido ou política de roteamento;
- providers/modelos permitidos;
- tipos de contexto aceitos;
- tools permitidas;
- MCP tools permitidas;
- limites de execução;
- política de erro;
- runner de agente;
- resultado normalizado;
- erro estruturado;
- integração com router, contexto, provider adapter e MCP permission layer.

Não inclui:

- graph engine;
- swarm;
- planner autônomo;
- self-reflection automática;
- workflows visuais;
- execução multiagente complexa.

## Entregáveis

Módulos conceituais esperados:

- `capybara_ai.agents.agent`
- `capybara_ai.agents.config`
- `capybara_ai.agents.runner`
- `capybara_ai.agents.result`

## Dependências

- Fase 2.
- Fase 3.
- Fase 4.
- Fase 5.
- Fase 6.
- Fase 7.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Agente válido | Executa com modelo elegível | Teste unitário/integração controlada |
| Modelo incompatível | Bloqueia antes do provider | Teste negativo |
| Contexto incompatível | Bloqueia antes do provider | Teste negativo |
| Provider falhando | Retorna erro estruturado | Teste unitário |
| Tool não permitida | Bloqueia execução | Teste negativo |
| Resultado | Inclui metadata mínima | Teste unitário |
| Erro | Não pode virar sucesso textual | Teste negativo |
| Multiagente avançado | Não deve existir na V1 | Auditoria |

## Definição de pronto

A fase está pronta quando:

- agentes são configuráveis sem estado global oculto;
- o runner usa router, contexto, provider adapter e MCP permission layer;
- execuções produzem `ExecutionResult` normalizado;
- erros permanecem estruturados;
- não há graph engine, swarm, planner autônomo ou execução multiagente complexa.

---

# Fase 9 — Integração MCP inicial real

## Objetivo

Implementar suporte inicial real a MCP com configuração explícita, allowlist, permissões e rastreabilidade, quando tecnicamente viável.

## Escopo

Inclui:

- configuração de MCPs por projeto;
- registro de servidores/conectores MCP;
- declaração ou listagem de tools disponíveis;
- allowlist por agente/projeto;
- escopo de operação;
- permissões de leitura, escrita, edição e execução;
- chamada MCP controlada;
- erro MCP estruturado;
- metadata de chamadas MCP.

Não inclui:

- marketplace MCP;
- execução irrestrita;
- tool automática por nome;
- servidor MCP próprio obrigatório;
- permissão implícita;
- uso de conector GitHub proibido.

## Entregáveis

Módulos conceituais esperados:

- `capybara_ai.mcp.client`
- `capybara_ai.mcp.config`
- `capybara_ai.mcp.tools`
- `capybara_ai.mcp.permissions`
- `capybara_ai.mcp.trace`
- `capybara_ai.mcp.errors`

## Dependências

- Fase 2.
- Fase 6.
- Fase 8.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| MCP não configurado | Não pode ser usado | Teste negativo |
| Tool não allowlisted | Bloqueia execução | Teste negativo |
| Tool de leitura | Declara leitura | Teste unitário |
| Tool de escrita | Declara escrita | Teste unitário |
| Tool de edição | Declara edição | Teste unitário |
| Tool de execução externa | Declara execução externa | Teste unitário |
| Mutação externa | Declara `mutates_external_state` | Teste unitário |
| Falha MCP | Retorna erro estruturado | Teste unitário |
| Chamada MCP | É rastreável | Teste unitário |
| Permissão ausente | Aplica default deny | Teste negativo |
| Segredo MCP | Não vaza em log, erro ou metadata | Teste de não vazamento |
| GitHub | Quando usado, deve usar `github-mcp` | Auditoria |
| Conector proibido | `mcp__codex_apps__github` não deve ser usado | Auditoria |

## Definição de pronto

A fase está pronta quando:

- MCP só executa com configuração explícita;
- allowlist, escopo e permissões são validados antes de execução;
- chamadas MCP produzem trace/metadata;
- falhas MCP retornam erro estruturado;
- segredos MCP não aparecem em logs, erros ou metadata;
- GitHub permanece restrito a `github-mcp`, quando aplicável.

---

# Fase 10 — Streaming e structured output

## Objetivo

Consolidar streaming e structured output como capabilities e contratos arquiteturais da V1.

## Escopo

Inclui:

- capability `streaming`;
- capability `structured_output`;
- validação de solicitação contra capability;
- contrato interno preparado para streaming;
- contrato interno preparado para saída estruturada;
- suporte real apenas em adapters que comprovem capacidade;
- erro explícito quando não suportado.

Não inclui:

- streaming simulado;
- JSON perfeito prometido universalmente;
- parsing artificial para fingir structured output;
- fallback silencioso para resposta textual.

## Entregáveis

Módulos conceituais afetados:

- `capybara_ai.capabilities`
- `capybara_ai.core.execution`
- `capybara_ai.providers`
- `capybara_ai.routing`
- `capybara_ai.agents`

## Dependências

- Fase 2.
- Fase 3.
- Fase 5.
- Fase 7.
- Fase 8.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Streaming suportado | Pode executar apenas em adapter real compatível | Teste de contrato |
| Streaming não suportado | Gera erro explícito | Teste negativo |
| Structured output suportado | Pode executar apenas em adapter real compatível | Teste de contrato |
| Structured output não suportado | Gera erro explícito | Teste negativo |
| Streaming simulado | Proibido | Teste negativo/auditoria |
| JSON genérico falso | Proibido | Teste negativo/auditoria |
| Parsing artificial para fingir structured output | Proibido | Teste negativo/auditoria |

## Definição de pronto

A fase está pronta quando:

- `streaming` e `structured_output` existem como capabilities explícitas;
- solicitações desses recursos são validadas antes de provider;
- adapters sem suporte real retornam erro explícito;
- nenhuma camada simula streaming ou structured output.

---

# Fase 11 — Testes

## Objetivo

Criar cobertura suficiente para impedir regressões, fluxo feliz isolado e violações das specs.

## Escopo

Inclui:

- testes unitários;
- testes de contrato;
- testes de integração controlada;
- testes negativos;
- testes de permissões;
- testes de configuração;
- testes de routing;
- testes de multimodalidade;
- testes de MCP;
- testes de não vazamento de segredo;
- testes de packaging/import;
- testes de docs/exemplos quando aplicável.

Não inclui:

- dependência obrigatória de serviços externos para toda a suíte;
- testes que exijam API keys reais por padrão;
- testes frágeis baseados em disponibilidade externa.

## Entregáveis

- Suíte `tests/` cobrindo os pilares da V1.
- Testes negativos obrigatórios.
- Testes de contrato para adapters.
- Testes de packaging/import.

## Dependências

- Fase 1.
- Fase 2.
- Fase 3.
- Fase 4.
- Fase 5.
- Fase 6.
- Fase 7.
- Fase 8.
- Fase 9.
- Fase 10.

## Critérios de aceite obrigatórios

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Provider suportado não configurado | Não pode ser usado | Teste negativo |
| Modelo conhecido não habilitado | Não pode ser roteado | Teste negativo |
| Capability ausente | Bloqueia execução | Teste negativo |
| Imagem/PDF/áudio/vídeo incompatível | Bloqueia execução | Teste negativo |
| OCR automático | Não ocorre | Teste negativo |
| PDF parsing automático | Não ocorre | Teste negativo |
| Transcrição automática | Não ocorre | Teste negativo |
| Fallback não autorizado | Não ocorre | Teste negativo |
| MCP não configurado | Não executa | Teste negativo |
| Tool não allowlisted | Não executa | Teste negativo |
| Segredo | Não aparece em logs, erros ou metadata | Teste de não vazamento |
| Adapter `contract` | Não executa como real | Teste negativo |
| Streaming | Não é simulado | Teste negativo |
| Structured output | Não é prometido sem capability | Teste negativo |
| `.env` real | Não é versionado | Auditoria |
| `.venv/` | Está no `.gitignore` | Auditoria |
| `capybara_ai` | É importável | Teste de packaging/import |
| `capybara-ai` | Está configurado no packaging | Teste/auditoria |
| GitHub | Usa `github-mcp`, quando aplicável | Auditoria |

## Definição de pronto

A fase está pronta quando:

- `pytest` executa a suíte local sem API key real por padrão;
- testes cobrem fluxo feliz, contratos e casos negativos;
- violações críticas das specs são testadas ou auditadas;
- exemplos executáveis são validados quando aplicável.

---

# Fase 12 — Exemplos de uso

## Objetivo

Criar exemplos mínimos, úteis e executáveis que demonstrem a identidade da V1.

## Escopo

Inclui exemplos para:

- agente textual simples;
- roteamento por capabilities;
- contexto multimodal bloqueado quando incompatível;
- provider Fake/Test;
- configuração de provider real;
- MCP tool allowlisted;
- erro de provider/modelo não configurado;
- structured output quando suportado;
- streaming quando suportado.

Não inclui:

- demo web;
- chatbot frontend;
- workflow visual;
- aplicação enterprise.

## Entregáveis

- Arquivos em `examples/`.
- Exemplos que rodem com provider Fake/Test sem API key.
- Exemplos de provider real marcados como dependentes de configuração do dev.

## Dependências

- Fase 1.
- Fase 8.
- Fase 9.
- Fase 10.
- Fase 11.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Exemplo básico | É compreensível e executável | Execução/revisão |
| Fake/Test provider | Roda sem API key | Teste de exemplo |
| Provider real | Deixa claro uso de `.env` configurado pelo dev | Revisão |
| MCP | Mostra allowlist | Revisão/teste controlado |
| Multimodal | Demonstra bloqueio correto | Teste de exemplo |
| Erro | Mostra erro estruturado | Teste de exemplo |
| Specs | Exemplos não contradizem specs | Revisão |

## Definição de pronto

A fase está pronta quando:

- exemplos demonstram os pilares centrais da V1;
- exemplos sem serviço externo rodam localmente;
- exemplos com providers reais não exigem API key por padrão;
- exemplos não prometem suporte falso.

---

# Fase 13 — README público

## Objetivo

Criar `README.md` como cartão de visita público do Capybara AI.

## Escopo

O README deve explicar:

- o que é Capybara AI;
- qual problema resolve;
- principais recursos;
- instalação;
- exemplo rápido de uso;
- visão geral da arquitetura;
- providers suportados;
- status dos adapters;
- suporte a MCP;
- suporte multimodal;
- capability registry;
- roteamento automático;
- configuração por projeto;
- API keys do dev;
- status da V1;
- limitações;
- exemplos;
- licença, se aplicável.

## Entregáveis

- `README.md` na raiz do projeto.

## Dependências

- Fase 1.
- Fase 8.
- Fase 9.
- Fase 10.
- Fase 12.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Novo usuário | Entende o propósito do framework | Revisão |
| API keys | Ficam claramente como responsabilidade do dev | Revisão |
| Providers | Distinguem suporte, configuração ativa e runtime | Revisão |
| Status da V1 | É realista | Revisão |
| Exemplo rápido | É funcional | Teste/revisão |
| Naming oficial | Usa `Capybara AI`, `capybara-ai` e `capybara_ai` corretamente | Auditoria |
| Suporte falso | README não promete | Revisão |
| Licença | README não inventa licença | Revisão |

## Definição de pronto

A fase está pronta quando:

- `README.md` existe;
- o README apresenta uso básico e arquitetura com precisão;
- limitações e status de adapters são claros;
- licença permanece pendente se não tiver sido definida.

---

# Fase 14 — Documentação completa em `docs/`

## Objetivo

Criar documentação completa de uso e extensão do microframework.

## Escopo

A documentação deve cobrir:

- instalação;
- configuração;
- conceitos centrais;
- agents;
- providers;
- adapter status;
- capability registry;
- roteamento automático;
- contexto multimodal;
- pipelines explícitos;
- MCP;
- tools;
- permissões;
- erros;
- exemplos;
- comandos;
- APIs públicas;
- funções relevantes;
- classes relevantes;
- possibilidades de uso;
- limitações;
- comportamento proibido;
- boas práticas;
- troubleshooting;
- como adicionar providers;
- como adicionar tipos de contexto;
- como criar integrações MCP;
- como testar o framework;
- ambiente `.venv`;
- `.env.example`;
- Git/GitHub readiness.

## Entregáveis

- Documentação em `docs/`.
- Guias de uso.
- Guias de extensão.
- Documentação de limitações e comportamentos proibidos.

## Dependências

- Fase 1.
- Fase 8.
- Fase 9.
- Fase 10.
- Fase 12.
- Fase 13.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Ambiente | Docs explicam `.venv` e `pip install -e ".[dev]"` | Revisão |
| Providers | Docs separam suportado, configurado e disponível em runtime | Revisão |
| API keys | Docs deixam claro que são do dev | Revisão |
| MCP | Docs explicam allowlist e permissões | Revisão |
| Multimodal | Docs explicam bloqueios e pipelines explícitos | Revisão |
| Extensão | Docs explicam novos providers/contextos | Revisão |
| Testes | Docs explicam como rodar testes | Revisão |
| Proibições | Docs listam comportamentos proibidos | Revisão |
| Naming | Docs usam nomes oficiais corretamente | Auditoria |
| Licença | Docs não inventam licença | Revisão |
| Suporte falso | Docs não prometem suporte que adapters não possuem | Revisão |

## Definição de pronto

A fase está pronta quando:

- `docs/` existe e cobre uso, extensão e limitações;
- documentação não contradiz as specs;
- documentação não inventa licença;
- documentação distingue arquitetura, configuração e runtime.

---

# Fase 15 — Git, GitHub e versionamento

## Objetivo

Preparar o projeto para versionamento e publicação no GitHub, respeitando as regras operacionais especificadas.

## Escopo

Inclui:

- verificação de Git local;
- inicialização de repositório se Git estiver disponível;
- `.gitignore` adequado para Python;
- commits organizados quando Git local estiver disponível;
- preparação para GitHub;
- uso do conector MCP correto para GitHub;
- revisão de arquivos sensíveis.

Não inclui:

- publicação sem autorização;
- publicação sem licença definida, se release pública madura exigir;
- uso de conector proibido.

## Regra GitHub

Use:

```text
github-mcp
```

Não use:

```text
mcp__codex_apps__github
```

## Sobre Git ausente no ambiente atual

A ausência de `git` no PATH impede operações locais como `git init`, commits locais e validação local do repositório.

Mas isso não impede operações remotas via `github-mcp`, desde que exista acesso/autorização disponível.

Se houver autorização via `github-mcp`, o implementador pode:

- criar repositório no GitHub;
- criar/escrever arquivos diretamente no repositório remoto;
- atualizar arquivos;
- organizar a estrutura inicial do projeto;
- preparar conteúdo remoto mesmo sem Git local.

O implementador deve registrar no `change_log.md` que Git local não estava disponível e que operações GitHub, se feitas, ocorreram via `github-mcp`.

## Entregáveis

- `.gitignore`.
- Repositório local inicializado, se Git estiver disponível.
- Commits locais, se Git estiver disponível e autorizado.
- Preparação remota via `github-mcp`, se autorizada.
- Auditoria de arquivos sensíveis.

## Dependências

- Fase 1.
- Fase 11.
- Fase 13.
- Fase 14.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| `.gitignore` | Ignora `.venv/`, `.env`, caches e builds | Auditoria |
| `.env` real | Não é versionado | Auditoria |
| Commits locais | São feitos apenas se Git local estiver disponível | Auditoria |
| GitHub | Operações usam `github-mcp` | Auditoria |
| Conector proibido | `mcp__codex_apps__github` não é usado | Auditoria |
| Publicação | Só ocorre com autorização | Auditoria |
| Naming | Nomes oficiais são usados corretamente | Auditoria |
| Licença | Não é inventada | Auditoria |

## Definição de pronto

A fase está pronta quando:

- arquivos sensíveis estão protegidos;
- Git local foi usado apenas se disponível;
- GitHub remoto foi usado apenas com autorização e via `github-mcp`;
- não há uso do conector proibido;
- release pública madura permanece bloqueada se licença não estiver definida.

---

# Fase 16 — Auditoria final de aderência

## Objetivo

Validar que a implementação aderiu às specs, não improvisou fora dos contratos e entregou a V1 completa em identidade.

## Escopo

Inclui revisão contra:

- `system_spec.md`;
- `technical_spec.md`;
- `implementation_plan.md`;
- `change_log.md`;
- `AGENTS.md`.

Também revisar:

- testes;
- docs;
- README;
- exemplos;
- ambiente;
- Git/GitHub;
- providers;
- MCP;
- multimodalidade;
- segurança de segredos;
- dependências;
- naming.

## Entregáveis

- Auditoria final de aderência.
- Lista de pendências, se houver.
- Confirmação explícita de bloqueios restantes, se houver.

## Dependências

- Fase 1.
- Fase 2.
- Fase 3.
- Fase 4.
- Fase 5.
- Fase 6.
- Fase 7.
- Fase 8.
- Fase 9.
- Fase 10.
- Fase 11.
- Fase 12.
- Fase 13.
- Fase 14.
- Fase 15.

## Critérios de aceite

| Cenário | Comportamento esperado | Teste obrigatório |
|---|---|---|
| Pilares V1 | Todos foram entregues | Auditoria |
| Core | Não acopla SDK externo | Auditoria imports |
| Providers | Têm status declarado | Auditoria/teste |
| Configuração | Controla providers, modelos e credenciais | Teste/auditoria |
| Router | Só usa modelos elegíveis | Teste/auditoria |
| MCP | Só executa tools autorizadas | Teste/auditoria |
| Multimodalidade | Não usa conversão implícita | Teste/auditoria |
| Streaming | Não é simulado | Teste/auditoria |
| Structured output | Não é prometido universalmente | Teste/auditoria |
| `.venv/` | Está no `.gitignore` | Auditoria |
| `.env` real | Não é versionado | Auditoria |
| README | Existe | Auditoria |
| `docs/` | Existe | Auditoria |
| Exemplos | Existem | Auditoria |
| Testes | Cobrem casos positivos e negativos | Auditoria |
| GitHub | Usa `github-mcp`, se aplicável | Auditoria |
| Conector proibido | `mcp__codex_apps__github` não foi usado | Auditoria |
| Subagentes | Foram usados quando aplicável ou a não utilização foi justificada | Auditoria |
| Naming | Nomes oficiais estão corretos | Auditoria |
| Licença | Não foi inventada | Auditoria |
| Dependências | Nenhuma dependência não aprovada foi adicionada | Auditoria |
| Violações críticas | Nenhuma permanece aberta | Auditoria |

## Definição de pronto

A fase está pronta quando:

- a auditoria final confirma aderência aos cinco artefatos normativos;
- testes e auditorias obrigatórias foram executados ou pendências foram explicitamente registradas;
- nenhuma violação crítica permanece aberta;
- a V1 só é declarada pronta se todos os critérios normativos estiverem satisfeitos.

---

## 5. Observações sobre entrega física dos artefatos

Nesta entrega ao usuário, o arquivo físico recebe sufixo para evitar sobrescrita:

```text
implementation_plan_capybara_ai.md
```

Dentro do conteúdo normativo, as referências permanecem canônicas:

```text
system_spec.md
technical_spec.md
implementation_plan.md
change_log.md
AGENTS.md
```

Essa regra é operacional da entrega, não altera a identidade normativa dos artefatos.
