# SYSTEM SPEC — Capybara AI

> Arquivo físico desta entrega: `system_spec_capybara_ai.md`  
> Nome canônico do artefato: `system_spec.md`  
> Status: Versão normativa final para revisão do usuário.  
>
> Este documento deve ser usado em conjunto com:
>
> - `technical_spec.md`
> - `implementation_plan.md`
> - `change_log.md`
> - `AGENTS.md`
>
> As referências internas usam os nomes canônicos dos artefatos, sem o sufixo físico desta entrega.

---

## 1. Visão geral

### 1.1 Nome do projeto

**Capybara AI**

### 1.2 Nome de instalação pretendido

```text
capybara-ai
```

### 1.3 Nome técnico do pacote/import

```text
capybara_ai
```

### 1.4 Objetivo

Capybara AI é um microframework Python para criação e orquestração de agentes de IA multimodais com abstração de providers, roteamento automático por capabilities, gerenciamento de contexto multimodal e integração explícita com MCP.

O framework deve permitir que desenvolvedores Python integrem agentes, modelos, ferramentas, providers e contexto externo em diferentes tipos de aplicação, sem restringir o uso a chatbots web.

### 1.5 Problema que resolve

Integrações com IA tendem a misturar:

* SDKs específicos de providers;
* regras de modelo espalhadas pelo código;
* fallback implícito;
* uso indevido de multimodalidade;
* configuração insegura de chaves;
* execução de tools externas sem rastreabilidade;
* dificuldade de trocar ou combinar providers;
* ausência de validação prévia das capabilities reais de cada modelo.

Capybara AI resolve esse problema ao fornecer uma arquitetura capability-first, provider-agnostic e configurável por projeto.

### 1.6 Tipo de sistema

Biblioteca/microframework Python, instalável como pacote, utilizável em:

* aplicações web;
* aplicações desktop;
* automações;
* APIs;
* CLIs;
* sistemas internos;
* pipelines;
* ferramentas de desenvolvimento;
* sistemas que integrem agentes de IA.

### 1.7 Plataforma alvo

Python library.

A V1 deve suportar ambiente local Python com:

```text
Python 3.11+
.venv
pyproject.toml
pip install -e ".[dev]"
```

### 1.8 Usuários principais

Desenvolvedores Python intermediários ou avançados que desejam integrar agentes de IA, múltiplos providers, contexto multimodal e MCP em seus próprios projetos.

### 1.9 Criticidade

| Aspecto                  | Criticidade |
| ------------------------ | ----------- |
| Negócio                  | Moderada    |
| Técnica                  | Alta        |
| Segurança de credenciais | Alta        |
| MCP/tools externas       | Alta        |
| Multimodalidade          | Alta        |
| Roteamento               | Alta        |
| Documentação/DX          | Média/alta  |

### 1.10 Classificação do projeto

Capybara AI é classificado como:

* framework técnico;
* sistema exploratório;
* sistema com integrações externas;
* sistema com domínio técnico mutável;
* sistema com risco de alucinação técnica por implementador;
* sistema que exige especificação normativa forte para handoff ao Codex.

### 1.11 Intensidade FSDI aplicada

**Alta, com proporcionalidade.**

O rigor é alto porque:

* o implementador posterior pode ser um agente de IA;
* APIs de providers mudam;
* MCP envolve ações externas;
* multimodalidade pode ser falsificada;
* configuração e credenciais precisam ser explícitas;
* V1 deve ser completa em identidade sem virar overengineering.

---

## 2. Identidade técnica

### 2.1 Definição curta

Capybara AI é um microframework Python capability-first para agentes de IA multimodais, roteamento automático, orquestração de modelos, adapters de providers e integração MCP explícita.

### 2.2 Princípios centrais

1. **Capability-first**
   Toda execução deve ser validada contra as capabilities declaradas do modelo/provider antes de qualquer chamada externa.

2. **Provider-agnostic core**
   O núcleo não deve depender diretamente de SDKs de providers.

3. **Configuração por projeto**
   O framework oferece possibilidades; o desenvolvedor escolhe quais providers, modelos, limites, credenciais e MCPs entram no projeto dele.

4. **Multimodalidade real ou pipeline explícito**
   O framework não deve fingir suporte multimodal.

5. **MCP flexível, mas contratual**
   O framework deve permitir usos legítimos de MCP configurados pelo dev, mas nunca executar tools implicitamente.

6. **V1 completa em identidade**
   A V1 deve entregar os pilares essenciais do microframework, ainda que alguns adapters tenham maturidade experimental ou contratual.

7. **DX como parte do produto**
   README, docs, exemplos, testes e instalação local fazem parte da entrega da V1 pelo implementador.

---

## 3. Escopo

### 3.1 Inclui na V1

A V1 deve incluir:

* core provider-agnostic;
* capability registry;
* validação automática por capabilities;
* roteamento automático;
* agentes configuráveis;
* contexto multimodal;
* bloqueio de multimodalidade falsa;
* adapters para múltiplos providers principais;
* suporte inicial real a MCP quando tecnicamente viável;
* configuração explícita por projeto;
* separação entre suporte arquitetural, configuração e runtime;
* streaming como capability e contrato;
* structured output como capability e contrato;
* pipeline multimodal explícito como contrato preparado;
* provider Fake/Test funcional;
* README produzido pelo implementador;
* documentação completa em `docs/` produzida pelo implementador;
* exemplos produzidos pelo implementador;
* testes;
* ambiente `.venv`;
* `pyproject.toml`;
* instalação editável;
* preparação para Git/GitHub;
* uso de `github-mcp` para operações GitHub, quando autorizadas.

### 3.2 Não inclui na V1

A V1 não deve incluir:

* UI;
* dashboard;
* chatbot web embutido;
* marketplace de providers;
* marketplace MCP;
* memória vetorial acoplada;
* graph engine;
* swarm;
* planner autônomo;
* execução multiagente complexa;
* self-reflection automática;
* workflows visuais;
* observabilidade distribuída avançada;
* otimização automática de custo;
* benchmarking automático;
* servidor MCP próprio obrigatório;
* Poetry como dependência obrigatória;
* `uv` como fluxo base obrigatório;
* OCR automático;
* parsing automático de PDF;
* transcrição automática de áudio;
* análise automática de vídeo;
* fallback textual invisível.

### 3.3 Futuro

Recursos futuros possíveis:

* novos providers;
* novos adapters reais;
* melhorias de DX;
* estabilização de API pública;
* observabilidade avançada;
* memória vetorial opcional;
* graph orchestration;
* multiagente avançado;
* marketplace MCP;
* servidor MCP próprio;
* otimização por custo/latência;
* benchmarks;
* suporte opcional a `uv`;
* integração com frameworks externos sem acoplar o core.

### 3.4 Limites explícitos

Capybara AI é um framework para uso por desenvolvedores em seus próprios projetos.

Capybara AI NÃO é:

* serviço central hospedado pelo autor;
* plataforma fechada;
* proxy de API;
* fornecedor de API keys;
* provedor de modelos;
* chatbot web;
* clone de LangChain/LlamaIndex;
* sistema de memória vetorial;
* runtime autônomo irrestrito de agentes.

---

## 4. Definição da V1

### 4.1 Tipo de V1

A V1 é **completa na identidade essencial**.

A V1 NÃO é parcial no sentido de adiar os pilares centrais para versões futuras.

### 4.2 Justificativa

A identidade do produto depende da presença conjunta de:

* agentes configuráveis;
* capability registry;
* validação automática;
* roteamento;
* contexto multimodal;
* bloqueio de multimodalidade falsa;
* providers/adapters;
* MCP;
* configuração explícita por projeto.

Remover qualquer um desses pilares descaracterizaria o microframework.

### 4.3 Implementação por fases internas

A V1 deve ser implementada em fases internas, mas todas as fases pertencem à entrega da V1.

Fases internas não são versões futuras.

### 4.4 Capacidades essenciais

| Capacidade                        | Status V1                       |
| --------------------------------- | ------------------------------- |
| Core provider-agnostic            | Obrigatório                     |
| Capability registry               | Obrigatório                     |
| Validação por capabilities        | Obrigatório                     |
| Roteamento automático             | Obrigatório                     |
| Agentes configuráveis             | Obrigatório                     |
| Contexto multimodal               | Obrigatório                     |
| Bloqueio de multimodalidade falsa | Obrigatório                     |
| Providers/adapters múltiplos      | Obrigatório                     |
| MCP inicial                       | Obrigatório, com status honesto |
| Configuração por projeto          | Obrigatório                     |
| Streaming como capability         | Obrigatório                     |
| Structured output como capability | Obrigatório                     |
| Pipeline explícito preparado      | Obrigatório                     |
| README/docs/exemplos/testes       | Obrigatório na implementação    |

### 4.5 Capacidades adiadas

* graph engine;
* swarm;
* planner autônomo;
* memória vetorial;
* UI;
* dashboard;
* marketplace;
* observabilidade avançada;
* otimização automática de custo;
* benchmark automático.

### 4.6 Critério objetivo de completude da V1

A V1 será considerada completa quando:

1. o pacote instalar com `pip install -e ".[dev]"`;
2. o core for provider-agnostic;
3. o capability registry funcionar;
4. capability ausente for tratada como não suportada;
5. contexto multimodal for representado;
6. contexto multimodal incompatível for bloqueado;
7. providers tiverem adapters/status declarados;
8. Fake/Test provider funcionar;
9. configuração por projeto controlar providers/modelos/credenciais;
10. router usar apenas modelos elegíveis;
11. agentes configuráveis executarem fluxo validado;
12. MCP inicial existir com allowlist e rastreabilidade ou status técnico justificado;
13. streaming existir como capability/contrato;
14. structured output existir como capability/contrato;
15. pipeline explícito estiver preparado sem automação padrão;
16. testes cobrirem fluxo normal e casos negativos;
17. README existir;
18. `docs/` existir;
19. exemplos existirem;
20. `.env.example` existir;
21. `.env` real não for versionado;
22. `.venv/` estiver no `.gitignore`;
23. Git/GitHub estiver preparado;
24. GitHub usar `github-mcp`, quando aplicável;
25. `mcp__codex_apps__github` não for usado;
26. auditoria final não encontrar violação crítica.

---

## 5. Registro de decisões funcionais — Pressão Decisória

| Decisão                            | Status     | Implementação hoje                            | Impacto | Risco                             | Condição de fechamento                  | Fallback                     |
| ---------------------------------- | ---------- | --------------------------------------------- | ------- | --------------------------------- | --------------------------------------- | ---------------------------- |
| Nome do projeto: Capybara AI       | Fechada    | Usar Capybara AI nos artefatos e docs         | Alto    | Inconsistência de naming          | Fechada pelo usuário                    | Não aplicável                |
| Nome PyPI: `capybara-ai`           | Fechada    | Configurar distribuição com esse nome         | Alto    | Pacote inválido/inconsistente     | Fechada pelo usuário                    | Não aplicável                |
| Import/package: `capybara_ai`      | Fechada    | Usar `capybara_ai` em imports                 | Alto    | Import quebrado                   | Fechada pelo usuário                    | Não aplicável                |
| V1 completa em identidade          | Fechada    | Implementar todos os pilares essenciais       | Alto    | Escopo inflado ou reduzido        | Fechada                                 | Não aplicável                |
| Fases internas pertencem à V1      | Fechada    | Planejar fases sem adiar pilares              | Alto    | Codex tratar fases como opcionais | Fechada                                 | Não aplicável                |
| Core provider-agnostic             | Fechada    | Core sem SDK externo                          | Alto    | Acoplamento estrutural            | Fechada                                 | Não aplicável                |
| Capability registry obrigatório    | Fechada    | Registry como fonte de verdade                | Alto    | Roteamento incorreto              | Fechada                                 | Não aplicável                |
| Capability ausente = não suportada | Fechada    | Bloquear recurso ausente                      | Alto    | Execução incompatível             | Fechada                                 | Não aplicável                |
| Configuração por projeto           | Fechada    | Dev habilita providers/modelos/API keys       | Alto    | Uso indevido                      | Fechada                                 | Não aplicável                |
| Provider suportado não é ativo     | Fechada    | Router só usa provider habilitado/configurado | Alto    | Provider indevido                 | Fechada                                 | Não aplicável                |
| Modelo conhecido não é habilitado  | Fechada    | Router só usa modelo autorizado               | Alto    | Custo/uso indevido                | Fechada                                 | Não aplicável                |
| MCP exige configuração explícita   | Fechada    | Default deny                                  | Alto    | Tool externa indevida             | Fechada                                 | Não aplicável                |
| GitHub via `github-mcp`            | Fechada    | Usar apenas `github-mcp` para GitHub          | Alto    | Conector errado                   | Fechada                                 | Não aplicável                |
| Entrega final sem `.zip`           | Fechada    | Um arquivo por resposta                       | Médio   | Sobrescrita/confusão              | Fechada                                 | Não aplicável                |
| Licença                            | Provisória | Deixar como pendente nos docs se não definida | Médio   | Publicação incompleta             | Definir antes de release pública madura | Registrar bloqueio/pendência |

### 5.1 Limite de provisório

As decisões provisórias restantes não afetam a arquitetura central.

Decisões provisórias conhecidas:

* licença;
* maturidade final real de cada adapter após verificação documental;
* detalhes mecânicos de API pública, dentro do contrato mínimo.

Essas decisões são aceitáveis desde que sejam registradas e não abram liberdade estrutural indevida.

---

## 6. Top 5 riscos da V1

| Risco                                     | Tipo        | Impacto                     | Mitigação                                | Onde validar                 |
| ----------------------------------------- | ----------- | --------------------------- | ---------------------------------------- | ---------------------------- |
| V1 ficar grande demais                    | Escopo      | Overengineering             | Cortes explícitos e fases internas       | `implementation_plan.md`     |
| V1 ser reduzida demais                    | Produto     | Identidade descaracterizada | Todos os pilares essenciais obrigatórios | Auditoria final              |
| Provider suportado ser tratado como ativo | Arquitetura | Uso indevido/custo/erro     | Separar suporte, configuração e runtime  | Testes de routing/config     |
| MCP executar tool sem permissão           | Segurança   | Ação externa indevida       | Default deny, allowlist, metadata        | Testes MCP                   |
| Multimodalidade falsa                     | Arquitetura | Violação central            | Bloqueio ou pipeline explícito           | Testes multimodais negativos |

---

## 7. Atores

| Ator                     | Permissões gerais                                                  | Responsabilidades                               | Restrições                                    |
| ------------------------ | ------------------------------------------------------------------ | ----------------------------------------------- | --------------------------------------------- |
| Desenvolvedor consumidor | Configura providers, modelos, credenciais, policies, MCPs e agents | Usar o framework no próprio projeto             | Deve fornecer próprias API keys e permissões  |
| Framework                | Valida, roteia, executa contratos e normaliza resultados           | Facilitar integração e impedir uso incompatível | Não decide providers/modelos pelo dev         |
| Provider externo         | Executa chamadas de IA                                             | Responder conforme sua API                      | Só pode ser usado se configurado e elegível   |
| MCP externo              | Fornece tools/contexto/execução externa                            | Executar operações autorizadas                  | Só pode executar se configurado e allowlisted |
| Agente configurado       | Executa tarefa dentro de limites                                   | Usar modelo/contexto/tools permitidos           | Não pode acessar recurso não autorizado       |
| Implementador/Codex      | Implementa a V1 conforme specs                                     | Criar código, docs, testes e ambiente           | Não pode improvisar fora das specs            |

---

## 8. Matriz de permissões

| Ação                                    | Desenvolvedor consumidor  | Framework         | Agente        | Provider externo | MCP/tool externa | Implementador                |
| --------------------------------------- | ------------------------- | ----------------- | ------------- | ---------------- | ---------------- | ---------------------------- |
| Configurar API key                      | Permitido                 | Negado            | Negado        | Negado           | Negado           | Apenas estruturar suporte    |
| Usar API key do autor                   | Negado                    | Negado            | Negado        | Negado           | Negado           | Negado                       |
| Ativar provider                         | Permitido                 | Negado por padrão | Negado        | Negado           | Negado           | Apenas implementar mecanismo |
| Escolher modelo permitido               | Permitido                 | Negado por padrão | Condicional   | Negado           | Negado           | Apenas implementar mecanismo |
| Roteamento automático                   | Configura política        | Executa           | Usa resultado | Negado           | Negado           | Implementa                   |
| Executar provider não configurado       | Negado                    | Negado            | Negado        | Negado           | Negado           | Negado                       |
| Executar model conhecido não habilitado | Negado                    | Negado            | Negado        | Negado           | Negado           | Negado                       |
| Executar tool MCP allowlisted           | Configura                 | Condicional       | Condicional   | Negado           | Condicional      | Implementa                   |
| Executar tool MCP não allowlisted       | Negado                    | Negado            | Negado        | Negado           | Negado           | Negado                       |
| Definir fallback                        | Permitido                 | Negado por padrão | Negado        | Negado           | Negado           | Implementa                   |
| Aplicar fallback sem permissão          | Negado                    | Negado            | Negado        | Negado           | Negado           | Negado                       |
| Fazer OCR/parsing automático            | Negado por padrão         | Negado            | Negado        | Negado           | Negado           | Negado                       |
| Criar pipeline explícito                | Permitido                 | Condicional       | Condicional   | Condicional      | Condicional      | Implementa se especificado   |
| Publicar no GitHub                      | Permitido com autorização | Negado            | Negado        | Negado           | Negado           | Permitido com autorização    |
| Usar `github-mcp`                       | Permitido                 | Não aplicável     | Não aplicável | Não aplicável    | Não aplicável    | Obrigatório para GitHub      |
| Usar `mcp__codex_apps__github`          | Negado                    | Negado            | Negado        | Negado           | Negado           | Negado                       |

### Regra

Toda ação sensível é negada por padrão se não estiver explicitamente autorizada.

---

## 9. Invariantes globais

1. O framework não usa API keys próprias do autor.
2. O desenvolvedor consumidor fornece suas próprias credenciais.
3. Provider suportado pelo framework não é provider ativo no projeto.
4. Modelo conhecido no registry não é modelo habilitado.
5. Router só pode selecionar modelos elegíveis.
6. Capability ausente equivale a capability não suportada.
7. MCP só executa tools configuradas e allowlisted.
8. Tool MCP deve declarar permissões.
9. Multimodalidade incompatível deve bloquear ou exigir pipeline explícito.
10. Pipeline explícito não equivale a suporte nativo.
11. Streaming não deve ser simulado.
12. Structured output não deve ser prometido universalmente.
13. Core não pode depender de SDK externo.
14. `.env` real não pode ser versionado.
15. `.venv/` deve estar no `.gitignore`.
16. GitHub deve usar `github-mcp`, quando aplicável.
17. `mcp__codex_apps__github` é proibido para GitHub.
18. README/docs não podem prometer suporte falso.
19. Implementador deve usar subagentes quando útil.
20. Mudanças estruturais devem ser registradas no `change_log.md`.

---

## 10. Separação entre suporte arquitetural, configuração do projeto e runtime

### 10.1 Suporte arquitetural

É o que Capybara AI sabe representar, validar ou adaptar.

Exemplo:

* adapter existe;
* capability conhecida;
* módulo MCP existe;
* tipo multimodal é representável.

Suporte arquitetural não implica ativação.

### 10.2 Configuração do projeto

É o que o desenvolvedor consumidor habilitou explicitamente.

Inclui:

* providers ativos;
* modelos permitidos;
* API keys;
* limites;
* fallback;
* MCPs;
* tools;
* escopos;
* permissões.

### 10.3 Disponibilidade em runtime

É o que está efetivamente utilizável na execução atual.

Depende de:

* provider configurado;
* credencial válida;
* adapter funcional;
* modelo habilitado;
* capability compatível;
* política do projeto;
* disponibilidade externa;
* limites não excedidos;
* MCP/tool operacional.

### 10.4 Regra crítica

O router só pode operar sobre providers/modelos que sejam:

* suportados;
* habilitados;
* configurados;
* autorizados;
* compatíveis;
* elegíveis;
* disponíveis em runtime.

---

## 11. Estados de providers e modelos

### 11.1 Estados de provider

| Estado      | Significado                              |
| ----------- | ---------------------------------------- |
| Suportado   | Existe adapter/contrato no framework     |
| Habilitado  | Dev ativou no projeto                    |
| Configurado | Credenciais/parâmetros mínimos presentes |
| Elegível    | Permitido pela política atual            |
| Disponível  | Pode ser usado na execução               |

### 11.2 Estados de modelo

| Estado     | Significado                    |
| ---------- | ------------------------------ |
| Conhecido  | Existe no registry             |
| Habilitado | Dev autorizou no projeto       |
| Compatível | Atende capabilities requeridas |
| Elegível   | Passa por políticas e limites  |
| Disponível | Pode ser usado agora           |

### 11.3 Proibição

O implementador não pode reduzir esses estados a um único booleano.

---

## 12. Providers da V1

| Provider  | Status esperado na V1                          |
| --------- | ---------------------------------------------- |
| Fake/Test | Real obrigatório ou mock funcional obrigatório |
| OpenAI    | Real prioritário                               |
| Gemini    | Real ou experimental                           |
| Anthropic | Real ou experimental                           |
| xAI       | Experimental ou contratual                     |
| DeepSeek  | Experimental ou contratual                     |
| Meta      | Experimental ou contratual                     |

### 12.1 Status permitidos de adapter

| Status         | Significado                                      |
| -------------- | ------------------------------------------------ |
| `real`         | Integração funcional, verificada e testada       |
| `experimental` | Integração inicial com limitações                |
| `contract`     | Contrato preparado sem promessa de execução real |
| `mock`         | Simulação controlada para testes                 |

### 12.2 Critério para adapter `real`

Um adapter só pode declarar status `real` se:

1. documentação oficial atual foi consultada;
2. dependência está registrada;
3. credenciais estão documentadas;
4. erro de credencial ausente é explícito;
5. capabilities suportadas estão declaradas;
6. limitações estão documentadas;
7. há teste de contrato;
8. há exemplo ou documentação de uso;
9. não é ativado por padrão;
10. não vaza segredos;
11. não finge streaming ou structured output;
12. não aceita modalidade sem suporte real.

---

## 13. Requisitos funcionais

### RF01 — Registrar capabilities de modelos

O framework deve permitir registrar capabilities por provider/modelo.

| Cenário                         | Comportamento esperado                        | Teste obrigatório  |
| ------------------------------- | --------------------------------------------- | ------------------ |
| Fluxo normal                    | Modelo registrado com capabilities declaradas | Teste unitário     |
| Capability ausente              | Tratada como não suportada                    | Teste unitário     |
| Modelo desconhecido             | Erro ou ausência explícita                    | Teste unitário     |
| Inferência por nome             | Proibida                                      | Teste negativo     |
| Modelo conhecido não habilitado | Não pode ser roteado                          | Teste negativo     |
| Regressão mínima                | Mudança no registry não quebra validação      | Teste de regressão |

---

### RF02 — Validar contexto multimodal

O framework deve validar se o modelo escolhido suporta os tipos de contexto enviados.

| Cenário                        | Comportamento esperado             | Teste obrigatório |
| ------------------------------ | ---------------------------------- | ----------------- |
| Texto para modelo textual      | Permitido                          | Teste unitário    |
| Imagem para modelo sem visão   | Bloqueado                          | Teste negativo    |
| PDF para modelo sem PDF nativo | Bloqueado salvo pipeline explícito | Teste negativo    |
| Áudio para modelo sem áudio    | Bloqueado salvo pipeline explícito | Teste negativo    |
| Vídeo para modelo sem vídeo    | Bloqueado salvo pipeline explícito | Teste negativo    |
| OCR implícito                  | Proibido                           | Teste negativo    |
| Parsing PDF implícito          | Proibido                           | Teste negativo    |
| Consistência após erro         | Provider não deve ser chamado      | Teste unitário    |

---

### RF03 — Roteamento automático por capabilities

O framework deve selecionar modelos elegíveis com base em capabilities e configuração do projeto.

| Cenário                            | Comportamento esperado             | Teste obrigatório |
| ---------------------------------- | ---------------------------------- | ----------------- |
| Modelo habilitado e compatível     | Pode ser selecionado               | Teste unitário    |
| Modelo conhecido não habilitado    | Não pode ser selecionado           | Teste negativo    |
| Provider suportado não configurado | Não pode ser usado                 | Teste negativo    |
| Sem modelo compatível              | Erro explícito                     | Teste unitário    |
| Fallback não autorizado            | Não ocorre                         | Teste negativo    |
| Streaming solicitado               | Exige capability streaming         | Teste unitário    |
| Structured output solicitado       | Exige capability structured output | Teste unitário    |

---

### RF04 — Configurar providers/modelos por projeto

O framework deve centralizar configuração do projeto consumidor.

| Cenário                  | Comportamento esperado       | Teste obrigatório      |
| ------------------------ | ---------------------------- | ---------------------- |
| Provider configurado     | Pode entrar na elegibilidade | Teste unitário         |
| Provider não configurado | Não entra na elegibilidade   | Teste negativo         |
| API key ausente          | Erro explícito               | Teste unitário         |
| Credencial em log        | Não deve aparecer            | Teste de não vazamento |
| Modelo não autorizado    | Não pode ser usado           | Teste negativo         |
| Configuração vazia       | Nenhum provider ativo        | Teste unitário         |

---

### RF05 — Executar agente configurável

O framework deve permitir executar agente com instruções, contexto, modelo/política e tools permitidas.

| Cenário               | Comportamento esperado        | Teste obrigatório |
| --------------------- | ----------------------------- | ----------------- |
| Execução válida       | Retorna resultado normalizado | Teste integrado   |
| Modelo incompatível   | Bloqueia antes do provider    | Teste negativo    |
| Contexto incompatível | Bloqueia antes do provider    | Teste negativo    |
| Provider falha        | Erro estruturado              | Teste unitário    |
| Tool não permitida    | Bloqueia execução             | Teste negativo    |
| Resultado             | Inclui metadata mínima        | Teste unitário    |

---

### RF06 — Integrar MCP com allowlist e rastreabilidade

O framework deve oferecer suporte inicial real a MCP como cliente/conector quando tecnicamente viável.

| Cenário              | Comportamento esperado         | Teste obrigatório          |
| -------------------- | ------------------------------ | -------------------------- |
| MCP configurado      | Pode ser usado se autorizado   | Teste integrado/controlado |
| MCP não configurado  | Não pode ser usado             | Teste negativo             |
| Tool allowlisted     | Pode executar dentro do escopo | Teste unitário/integrado   |
| Tool não allowlisted | Bloqueada                      | Teste negativo             |
| Tool de escrita      | Deve declarar escrita          | Teste unitário             |
| Tool de execução     | Deve declarar execução externa | Teste unitário             |
| Falha MCP            | Erro estruturado               | Teste unitário             |
| Trace MCP            | Chamada rastreável             | Teste unitário             |

---

### RF07 — Suportar streaming como capability

| Cenário                  | Comportamento esperado                 | Teste obrigatório      |
| ------------------------ | -------------------------------------- | ---------------------- |
| Modelo com streaming     | Adapter pode executar se suportar real | Teste de contrato      |
| Modelo sem streaming     | Erro explícito                         | Teste negativo         |
| Streaming simulado       | Proibido                               | Revisão/teste negativo |
| Provider não configurado | Não usar streaming                     | Teste negativo         |

---

### RF08 — Suportar structured output como capability

| Cenário                                | Comportamento esperado        | Teste obrigatório |
| -------------------------------------- | ----------------------------- | ----------------- |
| Modelo com structured output           | Pode usar se adapter suportar | Teste de contrato |
| Modelo sem structured output           | Erro explícito                | Teste negativo    |
| JSON universal falso                   | Proibido                      | Teste negativo    |
| Parsing artificial para fingir suporte | Proibido                      | Teste negativo    |

---

### RF09 — Preparar pipeline multimodal explícito

| Cenário                  | Comportamento esperado            | Teste obrigatório       |
| ------------------------ | --------------------------------- | ----------------------- |
| Pipeline não configurado | Multimodal incompatível bloqueia  | Teste negativo          |
| Pipeline configurado     | Transformação rastreável          | Teste unitário/contrato |
| Pipeline automático      | Proibido                          | Teste negativo          |
| Resultado derivado       | Não é tratado como suporte nativo | Teste unitário          |

---

### RF10 — Preparar README, docs, exemplos e GitHub readiness

O implementador deve produzir README, documentação, exemplos, testes e preparação para Git/GitHub.

| Cenário           | Comportamento esperado                                         | Teste obrigatório |
| ----------------- | -------------------------------------------------------------- | ----------------- |
| README            | Explica propósito, instalação, providers, MCP, multimodalidade | Revisão           |
| `docs/`           | Cobre uso e extensão                                           | Revisão           |
| Exemplos          | Demonstram pilares da V1                                       | Teste/revisão     |
| `.env.example`    | Existe sem segredos reais                                      | Revisão           |
| `.env` real       | Não versionado                                                 | Auditoria         |
| GitHub            | Usa `github-mcp` se autorizado                                 | Auditoria         |
| Conector proibido | `mcp__codex_apps__github` não usado                            | Auditoria         |

---

## 14. Requisitos não funcionais

### Segurança

* Segredos não podem aparecer em logs, erros, metadata ou docs.
* `.env` real não pode ser versionado.
* MCP deve ser default deny.
* Tool externa exige allowlist.

### Manutenção

* Core deve ser desacoplado.
* Adapters devem ser isolados.
* Dependências devem ser justificadas.
* API pública deve ser explícita e tipada.

### DX

* Instalação local deve ser clara.
* README deve ser útil.
* `docs/` deve cobrir uso e extensão.
* Exemplos devem funcionar.

### Performance

* V1 não precisa otimização avançada.
* Roteamento deve evitar chamadas externas desnecessárias quando validação local falhar.

### Observabilidade

* V1 exige metadata estruturada mínima.
* Não exige observabilidade distribuída avançada.

### Compatibilidade

* Python 3.11+.
* Fluxo base com Python/pip padrão.
* Poetry não obrigatório.
* `uv` opcional/futuro.

---

## 15. Regras de negócio/técnicas críticas

| Regra                              | Exceção            | Consequência operacional   | Invariante              | Teste obrigatório |
| ---------------------------------- | ------------------ | -------------------------- | ----------------------- | ----------------- |
| Provider suportado não é ativo     | Nenhuma            | Não usar sem configuração  | Configuração explícita  | Teste negativo    |
| Modelo conhecido não é habilitado  | Nenhuma            | Não rotear                 | Autorização do dev      | Teste negativo    |
| Capability ausente = não suportada | Nenhuma            | Bloquear execução          | Capability-first        | Teste unitário    |
| MCP default deny                   | Tool allowlisted   | Bloquear tool              | Permissão explícita     | Teste negativo    |
| Multimodalidade falsa proibida     | Pipeline explícito | Bloquear contexto          | Sem conversão implícita | Teste negativo    |
| Streaming não simulado             | Suporte real       | Erro explícito             | Capability real         | Teste negativo    |
| Structured output não universal    | Suporte real       | Erro explícito             | Capability real         | Teste negativo    |
| API key é do dev                   | Nenhuma            | Erro se ausente            | Sem chave do autor      | Teste de config   |
| GitHub via `github-mcp`            | Nenhuma            | Rejeitar conector proibido | Ferramenta correta      | Auditoria         |
| `.env` não versionado              | Nenhuma            | Rejeitar implementação     | Segredo seguro          | Auditoria         |

---

## 16. Fluxos principais

### Fluxo 1 — Execução de agente com modelo roteado

1. Dev configura providers/modelos.
2. Dev registra capabilities ou usa registry disponível.
3. Dev configura agente.
4. Dev envia contexto.
5. Framework deriva capabilities requeridas.
6. Router filtra modelos elegíveis.
7. Router seleciona modelo.
8. Runner valida contexto/tools/MCP.
9. Adapter executa provider.
10. Resultado retorna com metadata.

### Pós-condições

* Provider só foi chamado se elegível.
* Modelo selecionado estava autorizado.
* Metadata registra decisão.
* Erros são estruturados.

---

### Fluxo 2 — Bloqueio de contexto multimodal incompatível

1. Dev envia imagem/PDF/áudio/vídeo.
2. Framework identifica capability necessária.
3. Modelo não possui capability nativa.
4. Não há pipeline explícito.
5. Execução é bloqueada antes do provider.

### Pós-condições

* Nenhuma chamada externa é feita.
* Erro explica capability ausente.
* Metadata registra bloqueio.

---

### Fluxo 3 — Tool MCP allowlisted

1. Dev configura MCP.
2. Dev declara tool.
3. Dev allowlista tool para agente.
4. Agente solicita execução.
5. Framework valida escopo e permissões.
6. Tool executa.
7. Resultado registra operação.

### Pós-condições

* Tool executada era autorizada.
* Leitura/escrita/execução externa ficam rastreadas.
* Erro é estruturado se falhar.

---

### Fluxo 4 — Provider suportado, mas não configurado

1. Framework possui adapter.
2. Dev não habilitou provider no projeto.
3. Router avalia modelos.
4. Provider é excluído da elegibilidade.

### Pós-condições

* Provider não é chamado.
* Nenhuma API key é assumida.
* Metadata pode indicar descarte.

---

## 17. Fluxos excepcionais

| Exceção                         | Origem       | Comportamento esperado                      | Estado final                          | Teste obrigatório          |
| ------------------------------- | ------------ | ------------------------------------------- | ------------------------------------- | -------------------------- |
| API key ausente                 | Configuração | Erro explícito                              | Execução bloqueada                    | Teste unitário             |
| Provider indisponível           | Externo      | Erro estruturado; fallback só se autorizado | Execução falha ou fallback autorizado | Teste integrado/controlado |
| Modelo incompatível             | Capabilities | Bloqueio antes do provider                  | Execução bloqueada                    | Teste negativo             |
| Tool MCP não allowlisted        | MCP          | Bloqueio                                    | Execução bloqueada                    | Teste negativo             |
| Pipeline ausente                | Multimodal   | Bloqueio                                    | Execução bloqueada                    | Teste negativo             |
| Adapter experimental falha      | Provider     | Erro estruturado                            | Sem reclassificação automática        | Teste de contrato          |
| Segredo em log                  | Segurança    | Implementação rejeitada                     | Correção obrigatória                  | Auditoria                  |
| GitHub sem autorização          | Operacional  | Não publicar                                | Bloqueio operacional                  | Revisão                    |
| `mcp__codex_apps__github` usado | Operacional  | Rejeitar                                    | Correção obrigatória                  | Auditoria                  |

---

## 18. Modelo de domínio

### 18.1 Entidades

| Entidade        | Descrição                          | Campos conceituais                                     | Regras                         | Estados                                     |
| --------------- | ---------------------------------- | ------------------------------------------------------ | ------------------------------ | ------------------------------------------- |
| ProjectConfig   | Configuração do projeto consumidor | providers, models, credentials, limits, policies, MCPs | Centralizada e explícita       | válida/inválida                             |
| Provider        | Provider de IA                     | nome, adapter, status                                  | Não ativo por padrão           | suportado/habilitado/configurado/disponível |
| Adapter         | Integração com provider            | provider, status, capabilities, limitações             | Status obrigatório             | real/experimental/contract/mock             |
| ModelCard       | Modelo conhecido                   | provider, model_id, capabilities                       | Conhecido não é habilitado     | conhecido/habilitado/compatível/elegível    |
| Capability      | Capacidade declarada               | nome, modalidade, restrições                           | Ausente = não suportada        | suportada/não suportada                     |
| ContextItem     | Item de contexto                   | tipo, origem, metadata                                 | Sem conversão implícita        | válido/inválido/derivado                    |
| Agent           | Agente configurável                | nome, instruções, modelo/política, tools               | Usa apenas recursos permitidos | configurado/executando/falhou/concluído     |
| Router          | Selecionador de modelo             | policy, filtros, resultado                             | Só modelos elegíveis           | sucesso/sem modelo                          |
| MCPTool         | Tool externa                       | nome, escopo, permissões                               | Default deny                   | allowlisted/bloqueada                       |
| ExecutionResult | Resultado                          | output, metadata, erro                                 | Deve ser rastreável            | sucesso/erro/bloqueado                      |
| Pipeline        | Transformação explícita            | entrada, saída, transformação                          | Não é suporte nativo           | configurado/não configurado                 |

### 18.2 Relações

| Origem          | Relação    | Destino     | Cardinalidade | Regra                     |
| --------------- | ---------- | ----------- | ------------- | ------------------------- |
| ProjectConfig   | habilita   | Provider    | 0..N          | Nenhum ativo por padrão   |
| ProjectConfig   | habilita   | ModelCard   | 0..N          | Conhecido não basta       |
| Provider        | possui     | Adapter     | 1..N          | Status obrigatório        |
| ModelCard       | declara    | Capability  | 0..N          | Ausente = não suportada   |
| Agent           | usa        | Router      | 0..1          | Ou modelo fixo validado   |
| Agent           | usa        | MCPTool     | 0..N          | Somente allowlisted       |
| ContextItem     | exige      | Capability  | 1..N          | Validar antes do provider |
| Pipeline        | transforma | ContextItem | 1..N          | Deve ser explícito        |
| ExecutionResult | registra   | Metadata    | 1             | Obrigatório               |

---

## 19. Metadata mínima de execução

Todo resultado de execução deve permitir identificar:

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
* fallback aplicado, se explicitamente autorizado;
* tools MCP chamadas;
* permissões MCP usadas;
* leitura, escrita, edição ou execução externa;
* erro estruturado, quando houver.

A metadata não deve expor:

* API keys;
* tokens;
* secrets;
* valores de `.env`;
* headers sensíveis;
* credenciais MCP;
* credenciais GitHub.

---

## 20. Erros prováveis do implementador

| Área              | Erro provável                        | Consequência             | Regra preventiva              | Teste obrigatório       |
| ----------------- | ------------------------------------ | ------------------------ | ----------------------------- | ----------------------- |
| V1                | Reduzir a core mínimo                | Produto descaracterizado | Todos os pilares obrigatórios | Auditoria de completude |
| Providers         | Ativar todos por padrão              | Uso indevido             | Configuração explícita        | Teste negativo          |
| Modelos           | Usar modelo conhecido não habilitado | Custo/erro               | Router usa elegíveis          | Teste negativo          |
| Core              | Importar SDK externo                 | Acoplamento              | Core provider-agnostic        | Auditoria imports       |
| Capabilities      | Inferir por nome                     | Roteamento incorreto     | Ausente = não suportada       | Teste unitário          |
| MCP               | Executar tool sem allowlist          | Ação externa indevida    | Default deny                  | Teste negativo          |
| Multimodal        | OCR automático                       | Violação central         | Pipeline explícito apenas     | Teste negativo          |
| Streaming         | Simular chunks                       | Falso suporte            | Capability real               | Teste negativo          |
| Structured output | Prometer JSON universal              | Falso suporte            | Capability real               | Teste negativo          |
| Ambiente          | Usar Poetry obrigatório              | Viola decisão            | pip padrão                    | Auditoria               |
| GitHub            | Usar conector proibido               | Violação operacional     | `github-mcp` obrigatório      | Auditoria               |
| Docs              | Prometer suporte falso               | Confusão pública         | Status por adapter            | Revisão docs            |

---

## 21. Simulação mental de implementação — resumo incorporado

A simulação mental detectou e incorporou os seguintes ajustes:

1. API pública deve ser explícita, tipada, pequena e sem DSL mágica.
2. MCP inicial real deve ser cliente/conector, sem servidor obrigatório.
3. Metadata estruturada mínima é obrigatória, sem observabilidade pesada.
4. Pipeline multimodal explícito não equivale a suporte nativo.
5. Adapter `real` exige critérios objetivos.
6. Python mínimo: 3.11+.
7. Ferramentas dev base: `pytest`, `ruff`, `mypy`.
8. Licença permanece pendente antes de release pública madura.

---

## 22. Critérios de rejeição

A implementação deve ser rejeitada se:

* contrariar esta system spec;
* reduzir a V1 a protótipo fraco;
* omitir pilar essencial;
* acoplar core a provider;
* inferir capability;
* ativar provider sem configuração;
* usar modelo não habilitado;
* embutir API key;
* expor segredo;
* executar fallback sem permissão;
* executar MCP sem configuração;
* executar tool MCP sem allowlist;
* ocultar escrita/execução externa;
* executar OCR/parsing/transcrição automática por padrão;
* tratar pipeline como suporte nativo;
* simular streaming;
* prometer structured output universal;
* usar Poetry como requisito obrigatório;
* usar `mcp__codex_apps__github`;
* versionar `.env`;
* versionar `.venv/`;
* omitir README;
* omitir `docs/`;
* omitir testes negativos;
* ignorar subagentes quando úteis;
* ignorar `change_log.md`;
* publicar sem autorização;
* contradizer nomes oficiais `Capybara AI`, `capybara-ai` e `capybara_ai`.

---

## 23. Gate de risco da System Spec

A especificação não pode avançar para implementação se houver:

* decisão crítica aberta sobre V1;
* provider/modelo ativo por inferência;
* API key implícita;
* MCP sem allowlist;
* tool externa sem rastreabilidade;
* multimodalidade falsa permitida;
* ausência de critério para adapter real;
* ausência de testes negativos;
* ambiente Python indefinido;
* GitHub sem regra de conector;
* conflito entre nomes do projeto/pacote/import;
* licença sendo tratada como definida sem decisão.

### Status do gate

A system spec está apta a orientar os demais artefatos, desde que:

* `technical_spec.md` detalhe os contratos técnicos;
* `implementation_plan.md` detalhe fases e testes;
* `change_log.md` registre a mudança de nome e formato de entrega;
* `AGENTS.md` oriente o implementador operacionalmente.

---

## 24. Observações sobre entrega física dos artefatos

Nesta entrega ao usuário, o arquivo físico recebe sufixo para evitar sobrescrita:

```text
system_spec_capybara_ai.md
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