# TECHNICAL SPEC — Capybara AI

> Arquivo físico desta entrega: `technical_spec_capybara_ai.md`  
> Nome canônico do artefato: `technical_spec.md`  
> Status: Versão normativa final para revisão do usuário.  
>
> Este documento deve ser usado em conjunto com:
>
> - `system_spec.md`
> - `implementation_plan.md`
> - `change_log.md`
> - `AGENTS.md`
>
> As referências internas usam os nomes canônicos dos artefatos, sem o sufixo físico desta entrega.

---

## 1. Objetivo técnico

### 1.1 Objetivo deste documento

Este documento define a especificação técnica normativa da V1 do **Capybara AI**, um microframework Python para agentes de IA multimodais, roteamento por capabilities, adapters de providers e integração explícita com MCP.

Ele deve impedir que o implementador:

- invente arquitetura;
- escolha stack por preferência;
- acople core a providers;
- crie APIs implícitas;
- ignore configuração do projeto consumidor;
- simule suporte multimodal;
- execute MCP sem contrato;
- declare suporte real sem evidência;
- adicione dependências não aprovadas;
- implemente apenas fluxo feliz.

### 1.2 Relação com `system_spec.md`

O `system_spec.md` define:

- visão funcional;
- escopo;
- V1;
- atores;
- permissões;
- requisitos funcionais;
- regras críticas;
- fluxos;
- critérios de rejeição.

Este `technical_spec.md` define:

- stack oficial;
- arquitetura técnica;
- módulos;
- contratos;
- dependências;
- padrões;
- proibições técnicas;
- limites da autonomia do implementador;
- regras anti-alucinação;
- critérios técnicos de aceite.

Em caso de conflito:

1. `system_spec.md` prevalece em comportamento, escopo e regras funcionais.
2. `technical_spec.md` prevalece em arquitetura, stack, módulos, contratos e implementação técnica.
3. `implementation_plan.md` prevalece na ordem de execução.
4. `change_log.md` registra mudanças aprovadas.
5. `AGENTS.md` orienta o modo operacional do implementador.

### 1.3 Perfil do implementador posterior

O implementador posterior será um agente Codex ou equivalente.

Ele deve ter autonomia controlada.

Ele pode resolver detalhes mecânicos locais, mas não pode tomar decisões estruturais sem autorização normativa ou registro formal.

### 1.4 Nível de autonomia permitido

O implementador pode:

- organizar arquivos conforme os módulos especificados;
- escolher nomes internos mecânicos desde que respeitem os conceitos normativos;
- implementar testes exigidos;
- criar documentação exigida;
- adaptar código a limitações reais de SDKs oficiais;
- registrar dúvidas;
- propor mudanças no `change_log.md`;
- usar subagentes quando útil.

O implementador não pode:

- alterar escopo da V1;
- trocar stack oficial;
- usar framework agentic pesado como base estrutural;
- acoplar core a SDK externo;
- ativar provider por padrão;
- usar modelo não habilitado;
- inferir capabilities;
- simular streaming;
- fingir structured output;
- executar MCP sem allowlist;
- fazer OCR/parsing/transcrição automática por padrão;
- usar Poetry como dependência obrigatória;
- usar `mcp__codex_apps__github` para GitHub;
- versionar `.env`;
- versionar `.venv/`;
- adicionar dependência sem justificativa e registro.

### 1.5 Criticidade técnica

**Alta.**

Motivos:

- múltiplos providers externos;
- APIs mutáveis;
- integração MCP;
- risco de execução externa;
- gerenciamento de credenciais;
- multimodalidade;
- roteamento automático;
- handoff para implementador por IA.

### 1.6 Intensidade FSDI aplicada

**Alta, com proporcionalidade.**

A especificação deve ser forte contra ambiguidade, mas não deve gerar overengineering.

---

## 2. Stack oficial

| Área | Decisão oficial | Versão / restrição | Justificativa | Status |
|---|---|---|---|---|
| Linguagem | Python | Python 3.11+ | Ecossistema maduro para IA, SDKs e ferramentas | Fechada |
| Tipo de produto | Biblioteca/microframework | Pacote instalável | Deve ser usado em apps diversos, não como serviço central | Fechada |
| Nome público | Capybara AI | Nome de produto | Fechado pelo usuário | Fechada |
| Nome PyPI | `capybara-ai` | Distribuição | Nome pretendido de instalação | Fechada |
| Nome de pacote/import | `capybara_ai` | Pacote Python | Compatível com import Python | Fechada |
| Packaging | `pyproject.toml` | Obrigatório | Padrão moderno de projeto Python | Fechada |
| Ambiente local | `.venv` | Na raiz do projeto | Ambiente isolado e simples | Fechada |
| Instalação dev | `pip install -e ".[dev]"` | Fluxo base | Funciona com Python/pip padrão | Fechada |
| Gerenciador obrigatório | Nenhum além de pip | Poetry proibido como obrigatório; `uv` opcional/futuro | Evitar dependência operacional extra | Fechada |
| Testes | `pytest` | Dependência dev | Padrão consolidado para testes Python | Fechada |
| Lint/format | `ruff` | Dependência dev | Ferramenta rápida e moderna | Fechada |
| Type checking | `mypy` | Dependência dev base | Reforça tipagem estática | Fechada |
| Type checking alternativo | `pyright` | Permitido somente com justificativa | Alternativa possível, não padrão | Provisória controlada |
| Validação de dados | Pydantic v2 ou dataclasses tipadas | Decisão controlada pelo implementador conforme custo | Pode ajudar configs/modelos, mas é dependência estrutural | Provisória controlada |
| Providers | Adapters isolados | SDKs apenas nos adapters | Core provider-agnostic | Fechada |
| MCP | Cliente/conector MCP inicial | Sem servidor obrigatório | Integração externa explícita | Fechada |
| Persistência | Nenhuma persistência obrigatória na V1 | Estado/config em memória e arquivos de configuração | Evitar banco/memória prematuros | Fechada |
| Banco de dados | Nenhum | Fora da V1 | Framework não exige persistência central | Fechada |
| Web framework | Nenhum | Fora da V1 | Não é chatbot web nem API server | Fechada |
| CLI | Opcional/futuro | Não obrigatório na V1 | Evitar escopo extra | Fechada |
| Observabilidade | Metadata estruturada mínima | Sem tracing distribuído obrigatório | Rastreabilidade sem overengineering | Fechada |
| GitHub | `github-mcp` | Obrigatório para operações GitHub, se autorizadas | Regra operacional do projeto | Fechada |
| Conector proibido | `mcp__codex_apps__github` | Proibido | Evitar ferramenta errada | Fechada |

### Regra

Nenhuma tecnologia fora da stack oficial pode ser adicionada, substituída ou assumida sem retorno formal e registro no `change_log.md`.

---

## 3. Justificativa da stack

### 3.1 Decisões aprovadas

| Escolha | Motivo | Impacto | Evidência de adequação |
|---|---|---|---|
| Python 3.11+ | Boa maturidade de tipagem, performance e ecossistema IA | Base do projeto | Compatível com objetivo de microframework Python |
| `pyproject.toml` | Centraliza metadata, build e extras | Empacotamento claro | Padrão moderno Python |
| `.venv` local | Isolamento simples | Ambiente reproduzível | Preferência explícita do usuário |
| `pip install -e ".[dev]"` | Fluxo dev padrão e simples | DX previsível | Evita dependência de Poetry |
| `pytest` | Testes robustos e conhecidos | Qualidade | Ferramenta comum do ecossistema |
| `ruff` | Lint/format rápido | Padronização | Baixo custo operacional |
| `mypy` | Type checking estático | Robustez de contratos | Reforça tipagem forte |
| Provider adapters | Isola SDKs externos | Baixo acoplamento | Necessário para core provider-agnostic |
| Metadata estruturada | Rastreabilidade sem plataforma pesada | Auditoria | Proporcional à V1 |
| MCP cliente/conector | Integração real mínima | Funcionalidade central | Evita servidor obrigatório |
| Sem DB obrigatório | Framework não precisa persistir estado central | Simplicidade | Evita overengineering |
| Sem web framework | Não restringe a web/chatbot | Generalidade | Alinha escopo |

### 3.2 Alternativas rejeitadas

| Alternativa | Motivo da rejeição | Risco evitado |
|---|---|---|
| Poetry obrigatório | Usuário rejeitou como requisito da V1 | Fricção operacional |
| `uv` obrigatório | Pode ser opcional/futuro, mas não base | Fragmentação do fluxo |
| LangChain como base | Contamina aprendizado arquitetural e contratos internos | Acoplamento e perda de controle |
| LlamaIndex como base | Idem; foco forte em dados/RAG | Desvio de escopo |
| FastAPI obrigatório | Transformaria biblioteca em web/API framework | Escopo incorreto |
| Streamlit/UI | Desvia para chatbot/demo | Escopo incorreto |
| Banco obrigatório | Persistência não é pilar da V1 | Overengineering |
| Vector DB | Memória vetorial fora da V1 | Escopo inflado |
| Graph engine | Multiagente avançado fora da V1 | Complexidade excessiva |
| OCR/PDF libs por padrão | Violam regra anti-multimodalidade falsa | Conversão implícita |
| Observabilidade distribuída obrigatória | Peso operacional desproporcional | Overengineering |
| Todos SDKs como dependências obrigatórias | Instalação pesada | Acoplamento e fricção |

### 3.3 Trade-offs aceitos

| Trade-off | Justificativa | Consequência operacional |
|---|---|---|
| V1 completa em identidade, mas faseada | Evita protótipo fraco sem inflar tudo | Todas as fases pertencem à V1 |
| Múltiplos providers com maturidade variável | APIs externas podem limitar integração real | Status `real`, `experimental`, `contract`, `mock` obrigatório |
| MCP inicial real, sem servidor obrigatório | Entrega pilar central sem overengineering | Cliente/conector mínimo é suficiente |
| Pipelines multimodais preparados, mas não automáticos | Permite evolução sem violar capability-first | Dev precisa configurar explicitamente |
| Structured output como capability | Providers variam suporte real | Sem promessa universal |
| Streaming como capability | Providers variam suporte real | Sem simulação falsa |
| Sem persistência obrigatória | Mantém microframework leve | Memória/persistência futura via extensão |

---

## 4. Arquitetura técnica normativa

### 4.1 Estilo arquitetural

A arquitetura oficial deve seguir **Ports and Adapters / Hexagonal Architecture**.

O core define contratos internos.

Adapters integram providers externos, MCPs e SDKs.

### 4.2 Camadas

```text
Application-facing API
    ↓
Agent & Runner Layer
    ↓
Routing & Validation Layer
    ↓
Capability Registry
    ↓
Context & MCP Policy Layer
    ↓
Provider Abstraction Ports
    ↓
Provider Adapters
    ↓
External Providers / MCP Servers
```

### 4.3 Regra de dependência

Dependências devem apontar para dentro.

O core não pode importar:

* OpenAI SDK;
* Gemini SDK;
* Anthropic SDK;
* xAI SDK;
* DeepSeek SDK;
* Meta SDK;
* MCP SDK específico;
* framework web;
* biblioteca OCR/PDF/transcrição por padrão.

Adapters podem importar SDKs específicos, desde que:

* a dependência esteja justificada;
* esteja restrita ao adapter;
* esteja documentada;
* tenha teste de contrato;
* não seja ativada por padrão.

### 4.4 Estratégia de persistência

A V1 não possui persistência obrigatória.

Configuração pode ser representada por objetos, arquivos ou variáveis de ambiente carregadas pelo projeto consumidor, mas o framework não deve exigir banco de dados.

### 4.5 Estratégia de autenticação

Capybara AI não autentica usuários finais.

Credenciais de providers e MCPs pertencem ao projeto consumidor.

O framework deve:

* aceitar credenciais configuradas pelo dev;
* validar ausência de credencial;
* não embutir secrets;
* não logar secrets;
* não criar secrets pelo dev.

### 4.6 Estratégia de autorização

A autorização relevante da V1 é autorização operacional de:

* providers ativos;
* modelos habilitados;
* fallback permitido;
* MCPs configurados;
* tools allowlisted;
* pipelines explícitos.

Default deve ser deny.

### 4.7 Estratégia de logs/observabilidade

A V1 exige metadata estruturada mínima no resultado de execução.

A V1 não exige:

* tracing distribuído;
* OpenTelemetry obrigatório;
* dashboard;
* logging server;
* backend externo.

A metadata deve ser suficiente para depurar decisões de:

* provider;
* modelo;
* capability;
* roteamento;
* contexto;
* MCP;
* bloqueio;
* erro.

### 4.8 Estratégia de tratamento de erro

Erros devem ser estruturados e específicos.

Erro estrutural não deve virar resposta textual genérica.

Falhas de validação local devem bloquear antes de chamadas externas.

Falhas externas devem preservar causa sem vazar segredo.

### 4.9 Estratégia de rollback

Como a V1 não possui persistência central obrigatória, rollback transacional não é requisito geral.

Para MCP/tools externas que alterem estado externo:

* a tool deve declarar se escreve/edita/executa/muta estado externo;
* o framework deve registrar a chamada;
* o framework não deve inventar rollback;
* rollback só existe se a tool ou configuração declarar contrato explícito.

### 4.10 Estratégia de consistência após falha

Após falha:

* provider não deve ser chamado se validação local falhar;
* fallback só pode ocorrer se explicitamente configurado;
* tool MCP não deve ser reexecutada automaticamente sem política explícita;
* erro deve preservar metadata de bloqueio ou falha;
* estado interno não deve marcar sucesso em execução falha.

---

## 5. Estrutura de módulos

A estrutura recomendada de pacote é:

```text
src/
  capybara_ai/
    __init__.py
    core/
      __init__.py
      types.py
      errors.py
      metadata.py
      execution.py
    config/
      __init__.py
      project.py
      providers.py
      models.py
      secrets.py
      policies.py
    capabilities/
      __init__.py
      registry.py
      model_card.py
      validation.py
    context/
      __init__.py
      items.py
      validation.py
      pipelines.py
    providers/
      __init__.py
      base.py
      fake/
      openai/
      gemini/
      anthropic/
      xai/
      deepseek/
      meta/
    routing/
      __init__.py
      router.py
      policies.py
      eligibility.py
      errors.py
    agents/
      __init__.py
      agent.py
      config.py
      runner.py
      result.py
    mcp/
      __init__.py
      client.py
      config.py
      tools.py
      permissions.py
      trace.py
      errors.py
    testing/
      __init__.py
      fakes.py
```

### Regra

A estrutura exata pode variar mecanicamente, mas os módulos conceituais acima devem existir ou ter equivalentes claros.

O implementador não pode fundir tudo em um módulo monolítico.

---

## 6. Contratos técnicos entre módulos

| Módulo origem | Módulo destino | Contrato permitido                      | Dados trocados                       | Erros previstos                           | Teste obrigatório   |
| ------------- | -------------- | --------------------------------------- | ------------------------------------ | ----------------------------------------- | ------------------- |
| `agents`      | `routing`      | Solicitar modelo elegível               | request, contexto, policy            | `NoEligibleModelError`                    | Teste de roteamento |
| `agents`      | `context`      | Validar contexto                        | context items                        | `InvalidContextError`                     | Teste multimodal    |
| `agents`      | `mcp`          | Executar tool autorizada                | tool request, permissions            | `MCPPermissionError`, `MCPExecutionError` | Teste MCP           |
| `routing`     | `capabilities` | Consultar capabilities                  | model refs, required capabilities    | `MissingCapabilityError`                  | Teste registry      |
| `routing`     | `config`       | Consultar providers/modelos habilitados | project config                       | `ProviderNotConfiguredError`              | Teste config        |
| `routing`     | `providers`    | Selecionar adapter elegível             | provider/model refs                  | `ProviderUnavailableError`                | Teste adapter       |
| `context`     | `capabilities` | Mapear contexto para capabilities       | context item types                   | `UnsupportedModalityError`                | Teste multimodal    |
| `providers`   | `core`         | Retornar resultado normalizado          | request/response metadata            | `ProviderExecutionError`                  | Teste contrato      |
| `mcp`         | `core`         | Retornar trace/resultado MCP            | tool result, trace                   | `MCPExecutionError`                       | Teste MCP           |
| `config`      | `core`         | Fornecer configuração validada          | providers, models, secrets, policies | `ConfigurationError`                      | Teste config        |
| `testing`     | `providers`    | Simular provider                        | fake responses                       | Erros fake controlados                    | Teste fake          |

### Regra

Contrato ausente é contrato inexistente.

O implementador não pode criar comunicação entre módulos por conveniência.

---

## 7. API pública normativa

### 7.1 Princípio

A API pública da V1 deve ser:

* explícita;
* tipada;
* pequena;
* previsível;
* orientada aos conceitos centrais;
* sem estado global oculto;
* sem DSL própria obrigatória;
* sem decorators mágicos obrigatórios.

### 7.2 Conceitos públicos mínimos

A API pública deve expor conceitos equivalentes a:

* `ProjectConfig`;
* `ProviderConfig`;
* `ModelConfig`;
* `CapabilityRegistry`;
* `ModelCard`;
* `ContextItem`;
* `Router`;
* `Agent`;
* `AgentRunner`;
* `MCPToolConfig`;
* `MCPClientConfig`;
* `ExecutionResult`;
* erros estruturados.

Os nomes exatos podem variar apenas por necessidade mecânica, mas a semântica não pode ser alterada.

### 7.3 Proibições da API pública

A API pública não deve:

* exigir DSL própria para uso básico;
* ativar providers automaticamente;
* depender de OpenAI ou outro provider específico;
* permitir execução sem configuração explícita;
* ocultar fallback;
* ocultar MCP;
* ocultar pipeline multimodal;
* permitir chamada direta a provider pulando validação;
* criar estado global implícito para credenciais;
* carregar `.env` real de forma mágica sem controle do dev;
* transformar modelo conhecido em modelo habilitado.

### 7.4 Critério de aceite

A API pública será rejeitada se:

* o usuário conseguir chamar provider sem passar por configuração/validação;
* o router puder usar modelo não habilitado;
* o uso básico depender de DSL;
* providers forem ativados por import;
* secrets forem lidos ou logados implicitamente;
* uma chamada multimodal incompatível chegar ao provider.

---

## 8. Proibições do módulo — Contratos negativos

### 8.1 `core`

O módulo `core` NÃO DEVE:

* importar SDK de provider;
* importar MCP SDK específico;
* conhecer OpenAI/Gemini/Anthropic/xAI/DeepSeek/Meta;
* ler `.env`;
* fazer IO externo;
* executar provider;
* executar MCP;
* inferir capabilities;
* conter fallback;
* conter regra específica de adapter.

### 8.2 `config`

O módulo `config` NÃO DEVE:

* ativar provider por padrão;
* habilitar modelo por estar no registry;
* inventar API key;
* usar credenciais do autor;
* logar secrets;
* aceitar configuração ambígua;
* tratar ausência de credencial como warning;
* aplicar fallback não declarado.

### 8.3 `capabilities`

O módulo `capabilities` NÃO DEVE:

* inferir capability por nome do modelo;
* inferir capability por provider;
* tratar capability ausente como “talvez suportada”;
* atualizar capabilities automaticamente em runtime sem configuração;
* declarar streaming universal;
* declarar structured output universal;
* confundir pipeline com suporte nativo.

### 8.4 `context`

O módulo `context` NÃO DEVE:

* fazer OCR automático;
* fazer parsing automático de PDF;
* transcrever áudio automaticamente;
* analisar vídeo automaticamente;
* resumir arquivo automaticamente;
* converter arquivo sem pipeline explícito;
* enviar contexto parcial sem rastreabilidade;
* tratar contexto derivado como nativo.

### 8.5 `providers`

O módulo `providers` NÃO DEVE:

* ativar adapter por import;
* declarar adapter `real` sem cumprir critérios;
* esconder erro externo;
* vazar segredo;
* simular streaming;
* simular structured output;
* aceitar modalidade sem suporte real;
* alterar semântica da resposta sem documentação;
* expor SDK externo como API pública do core.

### 8.6 `routing`

O módulo `routing` NÃO DEVE:

* considerar provider não configurado;
* considerar modelo não habilitado;
* aplicar fallback sem permissão;
* ignorar capabilities;
* escolher modelo por conveniência;
* chamar provider diretamente;
* tentar execução para “ver se funciona”;
* rotear para adapter `contract` como se fosse `real`.

### 8.7 `agents`

O módulo `agents` NÃO DEVE:

* burlar router;
* burlar validação de contexto;
* executar tool MCP sem allowlist;
* assumir permissões;
* criar planner autônomo;
* implementar graph engine;
* implementar swarm;
* implementar self-reflection automática;
* transformar erro em sucesso textual.

### 8.8 `mcp`

O módulo `mcp` NÃO DEVE:

* executar tool não configurada;
* executar tool não allowlisted;
* assumir MCP seguro por padrão;
* ocultar leitura/escrita/execução externa;
* executar tool globalmente para todos os agentes;
* inferir permissão por nome;
* fazer auto-discovery sem configuração;
* inventar rollback;
* logar credenciais.

### 8.9 `testing`

O módulo `testing` NÃO DEVE:

* depender de API key real por padrão;
* mascarar falhas reais de contrato;
* simular provider real sem status claro;
* fazer testes externos obrigatórios na suíte base.

---

## 9. Configuração por projeto

### 9.1 Regra central

O framework oferece possibilidades.

O desenvolvedor consumidor escolhe quais possibilidades entram no projeto dele.

### 9.2 Configuração deve controlar

* providers habilitados;
* modelos habilitados;
* API keys;
* limites;
* políticas de fallback;
* políticas de streaming;
* políticas de structured output;
* MCPs configurados;
* tools allowlisted;
* pipelines explícitos;
* status de adapter permitido;
* preferências de roteamento.

### 9.3 Estados obrigatórios de provider

Cada provider deve poder ser distinguido em:

| Estado      | Significado                            |
| ----------- | -------------------------------------- |
| Suportado   | Existe adapter/contrato no framework   |
| Habilitado  | Dev ativou no projeto                  |
| Configurado | Credenciais/parâmetros mínimos existem |
| Elegível    | Permitido pela política atual          |
| Disponível  | Pode ser usado agora                   |

### 9.4 Estados obrigatórios de modelo

Cada modelo deve poder ser distinguido em:

| Estado     | Significado                 |
| ---------- | --------------------------- |
| Conhecido  | Existe no registry          |
| Habilitado | Dev autorizou               |
| Compatível | Atende capabilities         |
| Elegível   | Passa por políticas/limites |
| Disponível | Pode ser usado agora        |

### 9.5 Proibição

O implementador não pode colapsar esses estados em booleanos simplistas.

### 9.6 Secrets

Secrets devem:

* vir do projeto consumidor;
* ser configuráveis por provider/MCP;
* não ser versionados;
* não aparecer em metadata;
* não aparecer em logs;
* não aparecer em exceções;
* não aparecer em docs com valor real.

---

## 10. Capability Registry

### 10.1 Responsabilidade

O capability registry é a fonte de verdade interna sobre capabilities conhecidas de modelos/providers.

### 10.2 Capabilities mínimas da V1

| Capability          | Significado                                     |
| ------------------- | ----------------------------------------------- |
| `text_input`        | Aceita entrada textual                          |
| `image_input`       | Aceita imagem nativamente                       |
| `audio_input`       | Aceita áudio nativamente                        |
| `video_input`       | Aceita vídeo nativamente                        |
| `pdf_input`         | Aceita PDF nativamente                          |
| `file_input`        | Aceita arquivo genérico conforme contrato       |
| `tool_calling`      | Suporta chamada de tools                        |
| `mcp_compatible`    | Pode participar de fluxo com MCP/tools          |
| `streaming`         | Suporta streaming real                          |
| `structured_output` | Suporta saída estruturada real                  |
| `long_context`      | Suporta contexto longo acima de limite definido |
| `reasoning`         | Possui capacidade/mode de raciocínio declarado  |
| `native_multimodal` | Suporta multimodalidade nativa                  |

### 10.3 Regras

* Capability ausente equivale a não suportada.
* Capability não pode ser inferida por nome.
* Capability não pode ser inferida por provider.
* Capability deve ser validada antes da chamada.
* Capability pode variar por modelo, não apenas por provider.
* Capability pode variar por versão de modelo.
* Registry pode conhecer modelos que o projeto não habilitou.
* Modelo conhecido não é modelo elegível.

### 10.4 Model card mínimo

Cada model card deve conter, conceitualmente:

* provider;
* model id;
* nome humano, se houver;
* capabilities;
* limitações;
* status da informação;
* origem da informação;
* observações;
* se é habilitado pelo projeto;
* metadata de versão/data quando aplicável.

---

## 11. Contexto multimodal

### 11.1 Tipos de contexto da V1

A V1 deve representar:

* texto;
* markdown;
* código;
* imagem;
* PDF;
* áudio;
* vídeo;
* arquivo genérico;
* recurso MCP;
* contexto derivado por pipeline explícito.

### 11.2 Mapeamento para capabilities

| Contexto          | Capability requerida                              |
| ----------------- | ------------------------------------------------- |
| Texto             | `text_input`                                      |
| Markdown          | `text_input`                                      |
| Código            | `text_input`                                      |
| Imagem            | `image_input`                                     |
| PDF               | `pdf_input`                                       |
| Áudio             | `audio_input`                                     |
| Vídeo             | `video_input`                                     |
| Arquivo genérico  | `file_input` ou política explícita                |
| Tool/recurso MCP  | `mcp_compatible` e tool permission                |
| Contexto derivado | Depende da saída do pipeline, com rastreabilidade |

### 11.3 Pipeline multimodal explícito

Pipeline multimodal explícito deve declarar:

* entrada;
* saída;
* transformação;
* origem;
* ferramenta/modelo usado, se houver;
* se houve leitura;
* se houve extração;
* se houve transcrição;
* se houve conversão;
* se houve resumo;
* capabilities resultantes;
* limitações;
* responsabilidade do dev.

### 11.4 Regra crítica

Pipeline explícito não equivale a suporte nativo do modelo.

### 11.5 Proibições

A V1 não deve executar automaticamente:

* OCR;
* parsing de PDF;
* extração de texto;
* transcrição de áudio;
* análise de vídeo;
* conversão de arquivo;
* resumo de documento;
* fallback textual.

---

## 12. Providers e adapters

### 12.1 Providers da V1

| Provider  | Status esperado                                |
| --------- | ---------------------------------------------- |
| Fake/Test | Real obrigatório ou mock funcional obrigatório |
| OpenAI    | Real prioritário                               |
| Gemini    | Real ou experimental                           |
| Anthropic | Real ou experimental                           |
| xAI       | Experimental ou contratual                     |
| DeepSeek  | Experimental ou contratual                     |
| Meta      | Experimental ou contratual                     |

### 12.2 Status permitidos

| Status         | Regra                                          |
| -------------- | ---------------------------------------------- |
| `real`         | Integração funcional, verificada e testada     |
| `experimental` | Integração inicial, limitações documentadas    |
| `contract`     | Contrato preparado, sem execução real completa |
| `mock`         | Simulação controlada para testes               |

### 12.3 Critério objetivo para adapter `real`

Um adapter só pode declarar status `real` se cumprir todos os critérios:

1. documentação oficial atual do provider foi consultada;
2. dependência usada está registrada e justificada;
3. configuração de credenciais está documentada;
4. erros de credencial ausente são explícitos;
5. capabilities suportadas estão declaradas;
6. limitações estão documentadas;
7. há teste de contrato;
8. há exemplo ou documentação de uso;
9. o adapter não exige ativação por padrão;
10. o adapter não vaza segredos;
11. o adapter não finge streaming ou structured output;
12. o adapter não aceita modalidade sem suporte real.

### 12.4 Reclassificação obrigatória

Se qualquer critério não for cumprido, o adapter deve ser classificado como:

* `experimental`;
* `contract`;
* `mock`.

### 12.5 Fake/Test provider

O Fake/Test provider deve:

* funcionar sem API externa;
* permitir testes de routing;
* permitir testes de capabilities;
* permitir testes de agent runner;
* permitir testes de erro;
* não fingir provider real;
* ser claramente documentado como fake/test.

---

## 13. Routing

### 13.1 Responsabilidade

O router seleciona modelos elegíveis com base em:

* configuração do projeto;
* providers habilitados;
* modelos habilitados;
* capabilities requeridas;
* status do adapter;
* limites e policies;
* disponibilidade runtime;
* fallback autorizado.

### 13.2 Pipeline mínimo de elegibilidade

O router deve filtrar:

1. providers suportados;
2. providers habilitados no projeto;
3. providers configurados;
4. adapters com status permitido;
5. modelos conhecidos;
6. modelos habilitados;
7. modelos compatíveis com capabilities;
8. modelos permitidos por limites/policies;
9. modelos disponíveis em runtime.

### 13.3 Políticas mínimas da V1

A V1 deve suportar, no mínimo:

* `capability_strict`;
* `first_compatible`;
* modelo preferido com fallback explícito, se configurado.

### 13.4 Proibições

O router não deve:

* ativar provider;
* habilitar modelo;
* inferir capability;
* testar provider externo para descobrir suporte;
* aplicar fallback sem permissão;
* rotear para provider não configurado;
* rotear para modelo não habilitado;
* ignorar status de adapter.

---

## 14. Agents e runner

### 14.1 Agente configurável

Um agente deve declarar:

* nome;
* instruções;
* modelo preferido ou policy de routing;
* providers permitidos, quando aplicável;
* modelos permitidos, quando aplicável;
* tipos de contexto aceitos;
* tools permitidas;
* MCP tools permitidas;
* limites de execução;
* política de erro;
* metadata requerida.

### 14.2 Runner

O runner deve:

1. receber agente e input;
2. validar configuração;
3. validar contexto;
4. derivar capabilities;
5. chamar router;
6. validar tools/MCP;
7. chamar adapter;
8. retornar `ExecutionResult`;
9. preservar metadata;
10. retornar erros estruturados.

### 14.3 Fora da V1

A V1 não deve implementar:

* graph engine;
* swarm;
* planner autônomo;
* execução multiagente complexa;
* self-reflection automática;
* workflows visuais.

---

## 15. MCP

### 15.1 Escopo MCP da V1

A V1 deve implementar suporte inicial real a MCP como cliente/conector quando tecnicamente viável.

A V1 não exige servidor MCP próprio.

### 15.2 O módulo MCP deve permitir

* configurar MCPs por projeto;
* declarar ou listar tools disponíveis;
* associar tools a agentes;
* aplicar allowlist;
* declarar escopo;
* declarar permissões;
* executar tool autorizada;
* retornar erro estruturado;
* registrar trace/metadata.

### 15.3 Permissões mínimas de tool MCP

Cada tool MCP deve declarar, conceitualmente:

* nome;
* origem;
* escopo;
* `read`;
* `write`;
* `edit`;
* `execute`;
* `mutates_external_state`;
* permissões requeridas;
* política de erro;
* rastreabilidade.

### 15.4 Default deny

Nenhuma tool MCP deve executar se não estiver explicitamente allowlisted.

### 15.5 Fallback controlado

Se MCP real não puder ser implementado por bloqueio técnico verificável, o implementador deve:

1. registrar bloqueio no `change_log.md`;
2. explicar a causa técnica;
3. manter contrato MCP preparado;
4. marcar suporte como `contract` ou `experimental`;
5. não documentar como real;
6. não fingir execução.

### 15.6 GitHub

Para operações GitHub, usar:

```text
github-mcp
```

Não usar:

```text
mcp__codex_apps__github
```

O uso de `mcp__codex_apps__github` para GitHub é violação crítica.

---

## 16. ExecutionResult e metadata

### 16.1 Resultado obrigatório

Toda execução deve produzir resultado estruturado ou erro estruturado.

### 16.2 Metadata mínima

Todo resultado deve permitir identificar:

* agente executor;
* provider selecionado;
* modelo selecionado;
* providers/modelos considerados ou descartados, quando aplicável;
* motivo de descarte;
* capabilities requeridas;
* capabilities atendidas;
* itens de contexto utilizados;
* validações aplicadas;
* bloqueios ocorridos;
* fallback aplicado, se autorizado;
* tools MCP chamadas;
* permissões MCP usadas;
* indicação de leitura/escrita/edição/execução externa;
* erro estruturado, quando houver.

### 16.3 Segredos proibidos em metadata

Metadata, logs e erros não devem expor:

* API keys;
* tokens;
* secrets;
* valores de `.env`;
* headers sensíveis;
* credenciais MCP;
* credenciais GitHub.

### 16.4 Observabilidade

A V1 exige metadata estruturada mínima.

A V1 não exige:

* tracing distribuído;
* dashboard;
* backend de observabilidade;
* logging framework pesado.

---

## 17. Erros técnicos obrigatórios

A implementação deve ter erros estruturados equivalentes a:

| Erro                         | Quando ocorre                          |
| ---------------------------- | -------------------------------------- |
| `ConfigurationError`         | Configuração inválida                  |
| `MissingCredentialError`     | Credencial ausente                     |
| `ProviderNotConfiguredError` | Provider não habilitado/configurado    |
| `ModelNotEnabledError`       | Modelo conhecido mas não habilitado    |
| `MissingCapabilityError`     | Capability necessária ausente          |
| `UnsupportedModalityError`   | Contexto multimodal não suportado      |
| `NoEligibleModelError`       | Nenhum modelo elegível                 |
| `RoutingPolicyError`         | Policy inválida ou impossível          |
| `ProviderExecutionError`     | Falha externa do provider              |
| `AdapterStatusError`         | Uso incompatível com status do adapter |
| `InvalidContextError`        | Contexto malformado                    |
| `MCPConfigurationError`      | MCP não configurado                    |
| `MCPPermissionError`         | Tool não allowlisted/permissão ausente |
| `MCPExecutionError`          | Falha na execução MCP                  |
| `PipelineRequiredError`      | Pipeline explícito necessário          |
| `SecretExposureError`        | Tentativa/risco de expor segredo       |
| `DependencyPolicyError`      | Dependência não aprovada               |

Os nomes exatos podem variar, mas a semântica deve existir.

---

## 18. Política de dependências

A IA implementadora NÃO DEVE adicionar dependência sem:

* necessidade explícita;
* justificativa;
* alternativa considerada;
* impacto de manutenção;
* impacto operacional;
* aprovação ou registro formal.

### 18.1 Dependências base aprovadas

| Dependência       | Necessidade                 | Alternativas consideradas      | Impacto de manutenção | Impacto operacional        | Status                |
| ----------------- | --------------------------- | ------------------------------ | --------------------- | -------------------------- | --------------------- |
| `pytest`          | Testes                      | unittest                       | Baixo                 | Dev only                   | Aprovada              |
| `ruff`            | Lint/format                 | black+flake8/isort             | Baixo                 | Dev only                   | Aprovada              |
| `mypy`            | Type checking               | pyright                        | Médio/baixo           | Dev only                   | Aprovada              |
| SDKs de providers | Adapters reais              | HTTP manual / contract adapter | Variável              | Optional/provider-specific | Condicional           |
| SDK/cliente MCP   | Integração MCP real         | Contract adapter               | Variável              | Optional/feature-specific  | Condicional           |
| Pydantic v2       | Validação de config/modelos | dataclasses                    | Médio                 | Runtime se adotado         | Provisória controlada |

### 18.2 Dependências proibidas por padrão

| Dependência/categoria           | Motivo                              |
| ------------------------------- | ----------------------------------- |
| LangChain como base estrutural  | Contamina arquitetura               |
| LlamaIndex como base estrutural | Desvia escopo                       |
| Poetry obrigatório              | Rejeitado pelo usuário              |
| `uv` obrigatório                | Apenas opcional/futuro              |
| OCR/PDF parsing libs por padrão | Viola multimodalidade real          |
| Vector DB                       | Fora da V1                          |
| FastAPI obrigatório             | Não é web framework                 |
| Streamlit/UI                    | Fora da V1                          |
| OpenTelemetry obrigatório       | Observabilidade avançada fora da V1 |

### 18.3 Extras opcionais

O implementador pode organizar dependências extras por provider, desde que documentado.

Exemplo conceitual:

```text
capybara-ai[openai]
capybara-ai[gemini]
capybara-ai[anthropic]
capybara-ai[mcp]
capybara-ai[dev]
```

Os nomes exatos podem variar, mas a ideia de extras opcionais por provider é permitida.

---

## 19. Padrões obrigatórios

### 19.1 Convenções de código

* Python 3.11+.
* Type hints obrigatórios em API pública.
* Erros estruturados.
* Funções/classes públicas documentadas.
* Sem estado global oculto.
* Sem side effects em import.

### 19.2 Convenções de módulos

* Core não importa adapters.
* Adapters dependem de contratos do core.
* Routing depende de config/capabilities, não de SDK.
* Agents usam runner/router, não provider direto.
* MCP é isolado.

### 19.3 Regras de nomes

* Produto: `Capybara AI`.
* Distribuição: `capybara-ai`.
* Pacote/import: `capybara_ai`.
* Artefatos canônicos:

  * `system_spec.md`
  * `technical_spec.md`
  * `implementation_plan.md`
  * `change_log.md`
  * `AGENTS.md`

### 19.4 Regras de configuração

* Configuração centralizada.
* Nenhum provider ativo por padrão.
* Nenhum modelo habilitado por estar no registry.
* Secrets pertencem ao projeto consumidor.
* `.env.example` deve existir.
* `.env` não deve ser versionado.

### 19.5 Regras de testes

* Testes não devem exigir API key real por padrão.
* Fake/Test provider deve cobrir fluxo base.
* Testes negativos são obrigatórios.
* Testes de contrato para adapters são obrigatórios.
* Testes de não vazamento de segredo são obrigatórios.

### 19.6 Regras de documentação

* README deve ser cartão de visita público.
* `docs/` deve ser documentação completa.
* Docs devem distinguir suporte, configuração e runtime.
* Docs devem declarar status de adapters.
* Docs não podem prometer suporte falso.

---

## 20. Decisões técnicas estáveis, provisórias e bloqueadas

| Decisão                   | Status                          | Implementação hoje                  | Impacto | Risco                     | Condição de fechamento                | Fallback                  |
| ------------------------- | ------------------------------- | ----------------------------------- | ------- | ------------------------- | ------------------------------------- | ------------------------- |
| Python 3.11+              | Fechada                         | Configurar `requires-python >=3.11` | Alto    | Incompatibilidade         | Fechada                               | Não aplicável             |
| `capybara-ai`             | Fechada                         | Nome da distribuição                | Alto    | Naming incorreto          | Fechada                               | Não aplicável             |
| `capybara_ai`             | Fechada                         | Nome do pacote                      | Alto    | Import quebrado           | Fechada                               | Não aplicável             |
| `.venv` local             | Fechada                         | Criar/verificar `.venv`             | Alto    | Ambiente inconsistente    | Fechada                               | Não aplicável             |
| `pyproject.toml`          | Fechada                         | Usar como config de projeto         | Alto    | Packaging ruim            | Fechada                               | Não aplicável             |
| `pip install -e ".[dev]"` | Fechada                         | Fluxo base                          | Alto    | DX ruim                   | Fechada                               | Não aplicável             |
| `pytest`                  | Fechada                         | Testes                              | Médio   | Falta de suíte            | Fechada                               | Não aplicável             |
| `ruff`                    | Fechada                         | Lint/format                         | Médio   | Estilo inconsistente      | Fechada                               | Não aplicável             |
| `mypy`                    | Fechada                         | Type checking base                  | Médio   | Tipagem fraca             | Fechada                               | Pyright mediante registro |
| Pydantic v2               | Provisória controlada           | Usar se justificar dependência      | Médio   | Dependência desnecessária | Decisão do implementador com registro | Dataclasses               |
| MCP real                  | Fechada com fallback controlado | Cliente/conector inicial            | Alto    | Interface falsa           | Bloqueio técnico documentado          | `experimental`/`contract` |
| Providers reais           | Provisória por adapter          | Verificar docs oficiais             | Alto    | Falso suporte             | Testes de contrato                    | `experimental`/`contract` |
| Licença                   | Provisória                      | Não tratar como definida            | Médio   | Publicação incompleta     | Definir antes de release madura       | Registrar pendência       |

### Limite de provisório

As decisões provisórias são controladas e não excedem limite aceitável porque não afetam a arquitetura central sem fallback.

---

## 21. Riscos específicos para IA implementadora

A IA implementadora NÃO DEVE:

* inventar APIs, métodos ou bibliotecas;
* inferir regras não especificadas;
* simplificar validações críticas;
* implementar apenas fluxo feliz;
* alterar contratos entre módulos;
* criar estados não definidos;
* tratar erro silenciosamente;
* adicionar dependências não aprovadas;
* assumir permissões implícitas;
* ignorar regras de consistência;
* criar abstrações não justificadas;
* mudar comportamento por conveniência;
* acoplar core a provider;
* ativar provider por import;
* usar modelo conhecido como habilitado;
* fingir multimodalidade;
* executar MCP sem allowlist;
* usar `mcp__codex_apps__github`.

---

## 22. Erros prováveis do implementador

| Área              | Erro provável                        | Consequência          | Regra preventiva        | Teste obrigatório   |
| ----------------- | ------------------------------------ | --------------------- | ----------------------- | ------------------- |
| Stack             | Tornar Poetry obrigatório            | Viola decisão         | pip padrão              | Auditoria           |
| Core              | Importar SDK externo                 | Acoplamento           | Core provider-agnostic  | Auditoria imports   |
| Providers         | Ativar todos por padrão              | Uso indevido          | Config explícita        | Teste negativo      |
| Providers         | Marcar adapter como real sem prova   | Falso suporte         | Critério de real        | Teste contrato      |
| Modelos           | Usar modelo conhecido não habilitado | Custo/erro            | Estados separados       | Teste negativo      |
| Capabilities      | Inferir por nome                     | Roteamento incorreto  | Ausente = não suportada | Teste unitário      |
| Routing           | Fallback implícito                   | Privacidade/custo     | Fallback explícito      | Teste negativo      |
| MCP               | Tool sem allowlist                   | Ação externa indevida | Default deny            | Teste negativo      |
| MCP               | Ocultar escrita                      | Risco operacional     | Permissões obrigatórias | Teste metadata      |
| Multimodal        | OCR automático                       | Violação central      | Proibição               | Teste negativo      |
| Streaming         | Simular chunks                       | Falso suporte         | Capability real         | Teste negativo      |
| Structured output | Prometer JSON universal              | Falso suporte         | Capability real         | Teste negativo      |
| Secrets           | Logar API key                        | Vazamento             | Redação de segredos     | Teste não vazamento |
| Docs              | Prometer suporte amplo               | Falsa expectativa     | Status por adapter      | Revisão             |
| GitHub            | Usar conector proibido               | Violação              | `github-mcp`            | Auditoria           |

---

## 23. Regra anti-alucinação técnica

Nenhuma API, biblioteca, framework, comando, recurso de cloud, método de SDK ou integração pode ser usado fora da especificação ou sem verificação oficial quando aplicável.

O implementador deve consultar documentação oficial atual antes de implementar adapters reais.

Se a documentação atual não puder ser verificada, o adapter não pode ser `real`.

---

## 24. Protocolo de dúvida obrigatória

Se houver lacuna estrutural:

1. parar implementação do ponto afetado;
2. registrar a dúvida;
3. classificar como mecânica, local, estrutural ou crítica;
4. indicar impacto;
5. indicar artefato afetado;
6. propor retorno formal;
7. aguardar decisão ou registrar fallback autorizado.

### Exemplos de lacuna crítica

* SDK oficial não possui método esperado;
* provider mudou API;
* MCP não funciona como previsto;
* dependência nova necessária;
* API pública exigiria desvio de contrato;
* nome/licença ausente antes de publicação;
* GitHub sem autorização;
* tool MCP com escopo inseguro;
* pipeline multimodal desejado sem contrato.

---

## 25. Simulação mental técnica — resultado incorporado

A simulação detectou cinco lacunas e elas foram corrigidas nesta spec:

| Lacuna                           | Correção incorporada                                    |
| -------------------------------- | ------------------------------------------------------- |
| API pública mínima pouco fechada | API explícita, tipada, sem DSL mágica                   |
| MCP mínimo real ambíguo          | Cliente/conector real, sem servidor obrigatório         |
| Metadata/logging ambíguo         | Metadata estruturada mínima, sem observabilidade pesada |
| Pipeline multimodal ambíguo      | Pipeline não equivale a suporte nativo                  |
| Adapter real ambíguo             | Critérios objetivos para status `real`                  |

---

## 26. Critérios técnicos de rejeição

A implementação deve ser rejeitada se:

* violar `system_spec.md`;
* violar esta `technical_spec.md`;
* omitir pilar essencial da V1;
* core importar SDK externo;
* provider estiver ativo por padrão;
* modelo conhecido for usado sem habilitação;
* capability for inferida;
* contexto multimodal incompatível chegar ao provider;
* pipeline automático ocorrer por padrão;
* MCP executar sem allowlist;
* segredo aparecer em log/erro/metadata;
* adapter `real` não cumprir critérios;
* streaming for simulado;
* structured output for fingido;
* Poetry for obrigatório;
* `uv` for obrigatório;
* `mcp__codex_apps__github` for usado;
* `.env` for versionado;
* `.venv/` for versionado;
* README/docs prometerem suporte falso;
* testes negativos forem omitidos.

---

## 27. Checklist de aderência técnica obrigatória

Antes de declarar implementação pronta, verificar:

* [ ] Python 3.11+ configurado.
* [ ] Nome da distribuição é `capybara-ai`.
* [ ] Pacote/import é `capybara_ai`.
* [ ] `.venv/` está no `.gitignore`.
* [ ] `.env` está no `.gitignore`.
* [ ] `.env.example` existe.
* [ ] `pyproject.toml` existe.
* [ ] `pip install -e ".[dev]"` funciona.
* [ ] `pytest` configurado.
* [ ] `ruff` configurado.
* [ ] `mypy` configurado ou substituição registrada.
* [ ] Core não importa SDK externo.
* [ ] Capability registry existe.
* [ ] Contexto multimodal existe.
* [ ] Multimodalidade falsa é bloqueada.
* [ ] Configuração por projeto existe.
* [ ] Providers/modelos têm estados separados.
* [ ] Router usa apenas modelos elegíveis.
* [ ] Fake/Test provider funciona.
* [ ] Adapters declaram status.
* [ ] Adapter `real` cumpre critérios.
* [ ] MCP tem allowlist.
* [ ] MCP tem metadata.
* [ ] Streaming é capability.
* [ ] Structured output é capability.
* [ ] Pipeline explícito é rastreável.
* [ ] Segredos não vazam.
* [ ] README existe.
* [ ] `docs/` existe.
* [ ] Exemplos existem.
* [ ] Testes negativos existem.
* [ ] GitHub usa `github-mcp`, se aplicável.
* [ ] `mcp__codex_apps__github` não foi usado.

---

## 28. Observações sobre entrega física dos artefatos

Nesta entrega ao usuário, o arquivo físico recebe sufixo para evitar sobrescrita:

```text
technical_spec_capybara_ai.md
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