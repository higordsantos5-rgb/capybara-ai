# AGENTS.md — Capybara AI

> Arquivo físico desta entrega: `AGENTS_capybara_ai.md`  
> Nome canônico do artefato: `AGENTS.md`  
> Status: Versão normativa final para revisão do usuário.  
>
> Este arquivo é a entrada operacional para o agente implementador.
>
> Este arquivo NÃO substitui as specs normativas.  
> Ele define como o implementador deve consumir, obedecer e executar os artefatos do projeto.
>
> Instrução esperada ao implementador:
>
> ```text
> Consuma e obedeça o AGENTS.md.
> ```
>
> As referências internas usam os nomes canônicos dos artefatos, sem o sufixo físico desta entrega.

---

## 1. Papel do implementador

Você é o agente implementador do projeto **Capybara AI**.

Sua função é implementar a V1 do microframework Python conforme os artefatos normativos do projeto.

Você deve produzir:

- código completo do microframework;
- testes;
- exemplos;
- `README.md`;
- documentação completa em `docs/`;
- configuração de ambiente;
- arquivos de empacotamento Python;
- preparação para Git/GitHub;
- auditoria final de aderência às specs.

Você NÃO deve redesenhar o produto, reabrir escopo ou substituir decisões normativas por preferências próprias.

---

## 2. Ordem obrigatória de leitura

Antes de implementar qualquer coisa, leia nesta ordem:

1. `AGENTS.md`
2. `system_spec.md`
3. `technical_spec.md`
4. `implementation_plan.md`
5. `change_log.md`

Depois da leitura inicial, você deve obedecer todos os artefatos.

Em caso de conflito:

1. `system_spec.md` define comportamento, escopo, regras funcionais e V1.
2. `technical_spec.md` define arquitetura, stack, módulos, contratos e proibições técnicas.
3. `implementation_plan.md` define ordem de implementação, fases, critérios de aceite e definição de pronto.
4. `change_log.md` define decisões, mudanças e rastreabilidade.
5. `AGENTS.md` define o modo operacional do implementador.

Se o conflito for estrutural, pare e registre dúvida. Não escolha por inferência.

---

## 3. Obrigação de obedecer os artefatos normativos

Você deve implementar conforme:

- `system_spec.md`;
- `technical_spec.md`;
- `implementation_plan.md`;
- `change_log.md`;
- este `AGENTS.md`.

Se uma regra não estiver especificada, ela não existe.

Se uma decisão técnica estrutural não estiver especificada, você não pode inventar.

Se encontrar lacuna estrutural, deve parar, registrar e propor retorno formal.

---

## 4. Identidade do projeto

### 4.1 Nome do produto

```text
Capybara AI
```

### 4.2 Nome de instalação/PyPI

```text
capybara-ai
```

### 4.3 Nome técnico do pacote/import

```text
capybara_ai
```

### 4.4 Regra

Use esses nomes de forma consistente em:

- `pyproject.toml`;
- estrutura de pacote;
- imports;
- README;
- docs;
- exemplos;
- testes;
- metadata de pacote;
- eventual repositório GitHub.

Você não pode retornar ao placeholder `framework_name`.

---

## 5. Objetivo da V1

A V1 deve entregar a identidade essencial completa do Capybara AI.

A V1 NÃO é protótipo fraco.

A V1 NÃO é apenas core mínimo.

A V1 NÃO deve adiar os pilares centrais para versões futuras.

A V1 deve incluir:

- core provider-agnostic;
- capability registry;
- validação automática por capabilities;
- roteamento automático;
- agentes configuráveis;
- contexto multimodal;
- bloqueio de multimodalidade falsa;
- adapters para múltiplos providers;
- suporte inicial real a MCP, quando tecnicamente viável;
- configuração explícita por projeto;
- documentação;
- exemplos;
- testes;
- preparação para Git/GitHub.

As fases internas do `implementation_plan.md` pertencem todas à V1.

---

## 6. Limites de autonomia

Você pode:

- implementar detalhes mecânicos locais;
- organizar arquivos conforme a estrutura especificada;
- criar testes exigidos;
- criar documentação exigida;
- registrar dúvidas;
- propor melhorias;
- usar subagentes quando útil;
- dividir tarefas em unidades menores;
- reclassificar adapter conforme evidência, registrando no `change_log.md`;
- escolher entre Pydantic v2 e dataclasses tipadas conforme justificativa técnica.

Você NÃO pode:

- mudar escopo da V1;
- reduzir a V1 a protótipo;
- trocar arquitetura;
- trocar nomes oficiais;
- acoplar core a provider;
- inventar API pública fora dos contratos;
- adicionar dependência não aprovada;
- tornar Poetry obrigatório;
- tornar `uv` obrigatório;
- usar provider não configurado;
- usar modelo não habilitado;
- inferir capability;
- executar MCP sem configuração;
- executar tool MCP sem allowlist;
- fazer OCR/parsing/transcrição automática por padrão;
- simular streaming;
- prometer structured output universal;
- usar `mcp__codex_apps__github` para GitHub;
- versionar `.env`;
- versionar `.venv/`;
- inventar licença;
- ignorar `change_log.md`.

---

## 7. Protocolo de dúvida obrigatória

Se encontrar lacuna, contradição ou decisão ausente, classifique como:

- mecânica;
- local;
- estrutural;
- crítica.

### 7.1 Lacuna mecânica

Pode resolver se não alterar comportamento, arquitetura, contratos, dependências, segurança ou V1.

Exemplos:

- ajuste de nome interno;
- organização local de import;
- correção de typo;
- melhoria de mensagem sem alterar semântica.

### 7.2 Lacuna local

Pode propor solução se o impacto for limitado e não estrutural.

Registre no `change_log.md` se afetar comportamento observável.

### 7.3 Lacuna estrutural

Deve parar o ponto afetado.

Você deve registrar:

- dúvida;
- impacto;
- artefato afetado;
- etapa sugerida de retorno;
- opção recomendada;
- risco de prosseguir.

### 7.4 Lacuna crítica

Deve bloquear implementação do ponto afetado.

São críticas lacunas que envolvem:

- V1;
- providers;
- modelos;
- capabilities;
- API keys;
- segredos;
- MCP;
- permissões;
- fallback;
- GitHub;
- dependências;
- ambiente;
- publicação;
- segurança;
- contratos entre módulos;
- nomes oficiais;
- licença para release pública.

---

## 8. Política de mudança controlada

Toda mudança relevante deve ser registrada no `change_log.md`.

Mudanças que exigem registro:

- alteração de escopo;
- alteração de V1;
- alteração de arquitetura;
- alteração de stack;
- nova dependência;
- reclassificação de adapter;
- mudança em provider;
- mudança em MCP;
- mudança em permissões;
- mudança em fallback;
- mudança em ambiente;
- mudança em GitHub;
- publicação;
- licença;
- desvio autorizado de spec;
- bloqueio operacional;
- alteração de nomes oficiais.

Mudança estrutural não pode ser aplicada silenciosamente.

Mudança crítica não pode ser resolvida por inferência.

---

## 9. Política de perda de contexto

Se você perder contexto, reiniciar sessão, mudar de tarefa grande ou perceber incerteza sobre decisão normativa:

1. releia `AGENTS.md`;
2. releia `system_spec.md`;
3. releia `technical_spec.md`;
4. releia `implementation_plan.md`;
5. releia `change_log.md`;
6. só então continue.

Não continue com base em memória parcial.

---

## 10. Divisão obrigatória de tarefas

Você deve dividir a implementação em unidades menores.

A implementação não deve ser tratada como sequência monolítica feita por um único agente genérico quando houver divisão natural por domínio.

Divida tarefas como:

- arquitetura/core;
- capability registry;
- providers;
- configuração;
- roteamento;
- contexto multimodal;
- MCP;
- agentes;
- testes;
- documentação;
- DX/API pública;
- empacotamento Python;
- ambiente;
- Git/GitHub;
- revisão adversarial;
- auditoria final.

---

## 11. Uso obrigatório de subagentes quando útil

Use subagentes quando isso melhorar:

- qualidade;
- segurança;
- paralelização;
- revisão;
- detecção de violações;
- cobertura de testes;
- documentação;
- validação de providers;
- validação de MCP;
- revisão de ambiente;
- prontidão para GitHub.

Subagentes recomendados:

| Subagente | Responsabilidade |
|---|---|
| Arquitetura/Core | Revisar core, contratos e separação provider-agnostic |
| Capability Registry | Revisar registry, model cards e validações |
| Providers | Revisar adapters, status e integrações |
| Configuração | Revisar separação suporte/configuração/runtime |
| Routing | Revisar elegibilidade, fallback e policies |
| Multimodalidade | Revisar contextos, pipelines e bloqueios |
| MCP/Security | Revisar tools, allowlists, permissões e rastreabilidade |
| Tests | Criar e revisar testes |
| Docs/DX | Revisar README, docs e exemplos |
| Packaging | Revisar `pyproject.toml`, `.venv` e extras dev |
| GitHub Readiness | Revisar Git, `.gitignore`, `.env`, commits e GitHub |
| Adversarial Review | Procurar violações das specs |

Se subagentes não forem usados em tarefa relevante, registre justificativa.

---

## 12. Ambiente obrigatório do projeto

O projeto deve usar ambiente virtual Python local `.venv` na raiz do repositório.

Fluxo base obrigatório:

```bash
python -m venv .venv
# ativar .venv conforme o sistema operacional
pip install -e ".[dev]"
```

Regras:

- Python mínimo: 3.11+;
- `.venv` deve ficar na raiz;
- `.venv/` deve estar no `.gitignore`;
- `pyproject.toml` é obrigatório;
- instalação em modo desenvolvimento deve ser suportada;
- o fluxo base deve funcionar com Python/pip padrão;
- Poetry não é dependência obrigatória;
- `uv` pode ser mencionado como alternativa opcional futura;
- `.env.example` deve existir;
- `.env` real não deve ser versionado;
- ambiente deve suportar testes, exemplos, docs e empacotamento.

Ferramentas dev base:

- `pytest`;
- `ruff`;
- `mypy`.

`pyright` pode substituir `mypy` somente com justificativa registrada.

---

## 13. Git, GitHub e versionamento

Você deve:

- verificar se Git está instalado;
- instalar/configurar Git se tiver permissão e necessidade;
- inicializar repositório se necessário;
- criar `.gitignore` adequado para Python;
- garantir que `.venv/` está ignorado;
- garantir que `.env` está ignorado;
- criar `.env.example`;
- criar commits organizados;
- preparar projeto para GitHub;
- subir para GitHub apenas com autorização e acesso disponível.

### 13.1 Conector obrigatório para GitHub

Para operações de GitHub, use:

```text
github-mcp
```

Não use:

```text
mcp__codex_apps__github
```

Uso de `mcp__codex_apps__github` para GitHub é violação crítica.

---

## 14. Providers, modelos e configuração

O framework oferece possibilidades.

O desenvolvedor consumidor escolhe quais possibilidades entram no projeto dele.

Você deve separar:

1. suporte arquitetural do framework;
2. configuração explícita do projeto;
3. disponibilidade real em runtime.

### 14.1 Providers

Um provider pode estar:

- suportado pelo framework;
- habilitado no projeto;
- configurado com credenciais;
- elegível por política;
- disponível em runtime.

Esses estados não podem ser colapsados em um único booleano.

Provider com adapter no código NÃO é provider ativo.

Provider suportado NÃO pode ser usado se o dev não configurou.

### 14.2 Modelos

Um modelo pode estar:

- conhecido no registry;
- habilitado pelo dev;
- compatível com capabilities;
- elegível por política;
- disponível em runtime.

Modelo conhecido NÃO é modelo autorizado.

Modelo compatível NÃO é necessariamente elegível.

O router só pode selecionar modelos habilitados, elegíveis e disponíveis.

### 14.3 API keys

API keys pertencem ao projeto consumidor.

O framework NÃO deve:

- embutir API keys;
- usar API keys do autor;
- criar chaves pelo dev;
- assumir credencial padrão;
- expor segredos em logs, erros ou resultados.

Credencial ausente deve gerar erro explícito.

---

## 15. Providers da V1

A V1 deve usar o seguinte modelo de maturidade:

| Provider | Status esperado |
|---|---|
| Fake/Test | Real obrigatório ou mock funcional obrigatório para testes |
| OpenAI | Real prioritário |
| Gemini | Real ou experimental |
| Anthropic | Real ou experimental |
| xAI | Experimental ou contratual |
| DeepSeek | Experimental ou contratual |
| Meta | Experimental ou contratual |

Cada adapter deve declarar status:

- `real`;
- `experimental`;
- `contract`;
- `mock`.

Nenhum adapter pode fingir maturidade que não possui.

Antes de implementar integração real, consulte documentação oficial atual do provider.

Se não houver segurança técnica suficiente, marque como `experimental` ou `contract`.

### 15.1 Critério para adapter `real`

Um adapter só pode ser `real` se cumprir:

1. documentação oficial atual consultada;
2. dependência registrada;
3. credenciais documentadas;
4. erro de credencial ausente explícito;
5. capabilities declaradas;
6. limitações documentadas;
7. teste de contrato;
8. exemplo ou documentação;
9. não ativação por padrão;
10. não vazamento de segredo;
11. não fingir streaming ou structured output;
12. não aceitar modalidade sem suporte real.

---

## 16. Capability registry

Capability registry é fonte de verdade interna sobre suporte de modelos/providers.

Regras:

- capability ausente = não suportada;
- não inferir capability por nome do modelo;
- não inferir capability por provider;
- não assumir multimodalidade por default;
- streaming é capability;
- structured output é capability;
- MCP/tool support deve ser capability quando aplicável;
- modelo conhecido não é modelo habilitado.

O router deve validar capabilities antes de chamar qualquer provider.

---

## 17. Multimodalidade

O framework não deve fingir suporte multimodal.

Se o modelo não suporta nativamente o tipo de contexto, bloqueie ou exija pipeline explícito configurado pelo dev.

Proibido por padrão:

- OCR automático;
- extração automática de PDF;
- parsing automático de arquivo;
- transcrição automática de áudio;
- análise automática de vídeo;
- conversão multimodal invisível;
- fallback textual silencioso;
- envio parcial de contexto sem rastreabilidade.

Pipelines multimodais só podem existir se forem:

- explícitos;
- configurados pelo dev;
- rastreáveis;
- não tratados como suporte nativo do modelo.

Pipeline explícito deve declarar:

- entrada;
- saída;
- transformação;
- origem;
- ferramenta/modelo usado, se houver;
- se houve leitura, extração, transcrição, conversão ou resumo;
- capabilities resultantes;
- limitações.

---

## 18. MCP

MCP deve ser flexível, mas explícito.

O framework não deve bloquear usos legítimos configurados pelo dev.

O framework também não deve executar nada implicitamente.

Nenhuma tool MCP pode executar sem:

- MCP configurado;
- tool allowlisted;
- escopo declarado;
- permissões declaradas;
- tipo de operação declarado;
- rastreabilidade.

Toda tool MCP deve declarar se:

- lê dados;
- escreve dados;
- edita dados;
- executa ação externa;
- modifica estado externo.

Permissões mínimas conceituais:

- `read`;
- `write`;
- `edit`;
- `execute`;
- `mutates_external_state`.

Default deve ser deny.

Tool não allowlisted deve ser bloqueada.

### 18.1 MCP inicial real

A V1 deve implementar suporte inicial real a MCP como cliente/conector quando tecnicamente viável.

A V1 não exige servidor MCP próprio.

Se MCP real não puder ser implementado por bloqueio técnico verificável, registre no `change_log.md` e classifique como `experimental` ou `contract`.

Não documente como real se não for real.

---

## 19. Roteamento

O router deve considerar apenas modelos elegíveis.

Pipeline mínimo de elegibilidade:

1. provider suportado pelo framework;
2. provider habilitado no projeto;
3. provider configurado;
4. adapter com status permitido;
5. modelo conhecido no registry;
6. modelo habilitado pelo dev;
7. modelo compatível com capabilities;
8. modelo permitido por políticas e limites;
9. modelo disponível em runtime.

Somente depois disso o router pode selecionar.

Fallback entre providers só pode ocorrer se explicitamente permitido.

---

## 20. Streaming e structured output

Streaming deve existir como capability e contrato.

Structured output deve existir como capability e contrato.

Mas:

- não são obrigatórios em todos os providers;
- não devem ser simulados falsamente;
- não devem ser prometidos universalmente;
- adapters sem suporte devem declarar ausência;
- solicitação sem capability deve gerar erro explícito.

---

## 21. Multiagente avançado fora da V1

A V1 pode permitir múltiplos agentes configuráveis.

A V1 NÃO deve implementar:

- graph engine;
- swarm;
- planner autônomo;
- execução multiagente complexa;
- self-reflection automática;
- workflows visuais;
- orquestração avançada entre agentes.

---

## 22. API pública

A API pública da V1 deve ser:

- explícita;
- tipada;
- pequena;
- previsível;
- sem DSL própria obrigatória;
- sem decorators mágicos obrigatórios;
- sem estado global oculto.

Ela deve expor conceitos equivalentes a:

- configuração do projeto;
- provider adapter;
- capability registry;
- model card;
- context item;
- router;
- agent;
- runner;
- MCP config/tool config;
- execution result;
- erros estruturados.

A API pública não deve permitir:

- provider ativo por import;
- execução sem configuração explícita;
- chamada direta a provider pulando validação;
- fallback oculto;
- MCP oculto;
- pipeline multimodal oculto.

---

## 23. ExecutionResult e metadata

Toda execução deve produzir resultado estruturado ou erro estruturado.

A metadata mínima deve permitir identificar:

- agente executor;
- provider selecionado;
- modelo selecionado;
- providers/modelos considerados ou descartados, quando aplicável;
- motivo de descarte;
- capabilities requeridas;
- capabilities atendidas;
- itens de contexto utilizados;
- validações aplicadas;
- bloqueios ocorridos;
- fallback aplicado, se autorizado;
- tools MCP chamadas;
- permissões MCP usadas;
- leitura, escrita, edição ou execução externa;
- erro estruturado, quando houver.

Metadata, logs e erros não devem expor:

- API keys;
- tokens;
- secrets;
- valores de `.env`;
- headers sensíveis;
- credenciais MCP;
- credenciais GitHub.

---

## 24. README obrigatório

Você deve criar `README.md` na raiz.

O README deve explicar:

- o que é Capybara AI;
- qual problema resolve;
- principais recursos;
- instalação;
- exemplo rápido;
- visão geral da arquitetura;
- providers suportados;
- status dos adapters;
- suporte MCP;
- suporte multimodal;
- capability registry;
- roteamento;
- configuração por projeto;
- API keys do dev;
- status da V1;
- limitações;
- exemplos;
- licença, se aplicável.

O README não pode prometer suporte falso.

O README não pode ocultar limitações.

O README não pode inventar licença.

---

## 25. Documentação obrigatória em docs/

Você deve criar documentação completa em `docs/`.

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

Docs não podem contradizer specs.

Docs não podem prometer suporte que adapters não possuem.

Docs não podem inventar licença.

---

## 26. Testes obrigatórios

A suíte de testes deve cobrir:

- core;
- capability registry;
- contexto multimodal;
- providers;
- configuração;
- roteamento;
- agentes;
- MCP;
- streaming;
- structured output;
- segurança de segredos;
- empacotamento;
- exemplos.

Testes negativos obrigatórios:

- provider suportado não configurado não pode ser usado;
- modelo conhecido não habilitado não pode ser roteado;
- capability ausente bloqueia execução;
- imagem/PDF/áudio/vídeo incompatível bloqueia execução;
- OCR automático não ocorre;
- PDF parsing automático não ocorre;
- transcrição automática não ocorre;
- fallback não autorizado não ocorre;
- MCP não configurado não executa;
- tool não allowlisted não executa;
- segredo não aparece em logs;
- adapter `contract` não executa como real;
- streaming não é simulado;
- structured output não é prometido sem capability;
- `.env` real não é versionado;
- `.venv/` está no `.gitignore`;
- `capybara_ai` é importável;
- `capybara-ai` está configurado no packaging;
- GitHub usa `github-mcp`.

---

## 27. Dependências

Você não deve adicionar dependência sem:

- necessidade explícita;
- justificativa;
- alternativa considerada;
- impacto de manutenção;
- impacto operacional;
- aderência às specs.

SDKs de providers devem ficar restritos aos adapters.

Dependência não aprovada é proibida.

Poetry não deve ser obrigatório.

`uv` não deve ser obrigatório.

Dependências base dev:

- `pytest`;
- `ruff`;
- `mypy`.

Pydantic v2 é permitido apenas como decisão controlada e justificada. Dataclasses tipadas são fallback aceitável.

---

## 28. Licença

A licença ainda é decisão pendente.

Você NÃO deve inventar licença.

Você NÃO deve afirmar licença inexistente no README, docs, package metadata ou GitHub.

Antes de release pública madura, a licença deve ser definida e registrada no `change_log.md`.

Se não houver licença definida, registre pendência ou bloqueie release pública madura.

---

## 29. Critérios de rejeição

A implementação deve ser rejeitada se:

- não obedecer specs;
- reduzir V1 a protótipo;
- omitir pilar essencial;
- acoplar core a provider;
- inferir capabilities;
- usar provider não configurado;
- usar modelo não habilitado;
- embutir API key;
- expor segredo;
- executar fallback sem permissão;
- executar MCP sem configuração;
- executar tool MCP sem allowlist;
- ocultar escrita ou execução externa;
- fazer OCR/parsing/transcrição automática por padrão;
- tratar pipeline como suporte nativo;
- simular streaming;
- prometer structured output universal;
- tornar Poetry obrigatório;
- tornar `uv` obrigatório;
- usar `mcp__codex_apps__github`;
- versionar `.env`;
- versionar `.venv/`;
- omitir README;
- omitir `docs/`;
- omitir testes negativos;
- ignorar subagentes quando úteis;
- ignorar `change_log.md`;
- usar nomes diferentes dos oficiais sem mudança registrada;
- inventar licença.

---

## 30. Auditoria final obrigatória

Antes de considerar a V1 pronta, execute auditoria final contra:

- `system_spec.md`;
- `technical_spec.md`;
- `implementation_plan.md`;
- `change_log.md`;
- `AGENTS.md`.

A auditoria deve confirmar:

- todos os pilares da V1 foram entregues;
- ambiente está pronto;
- testes passam;
- README existe;
- `docs/` existe;
- exemplos existem;
- providers têm status claro;
- router respeita elegibilidade;
- MCP respeita allowlist;
- segredos não vazam;
- GitHub usa `github-mcp`;
- não há comportamento proibido;
- não há dependência não aprovada;
- nomes oficiais estão corretos;
- licença não foi inventada.

---

## 31. Regra final

Implemente somente o que está autorizado pelas specs.

Quando houver dúvida estrutural, pare.

Quando houver mudança, registre.

Quando houver risco de interpretação, consulte os artefatos.

Quando houver perda de contexto, releia os arquivos.

Não improvise fora da especificação.

Não transforme suporte arquitetural em disponibilidade runtime.

Não transforme conveniência em regra.

Não transforme fallback em comportamento implícito.

Não transforme MCP em permissão irrestrita.

Não transforme multimodalidade em conversão escondida.

Não transforme pipeline explícito em suporte nativo.

A V1 deve ser completa na identidade essencial, implementável em fases internas e fiel aos contratos normativos.

---

## 32. Observações sobre entrega física dos artefatos

Nesta entrega ao usuário, o arquivo físico recebe sufixo para evitar sobrescrita:

```text
AGENTS_capybara_ai.md
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
