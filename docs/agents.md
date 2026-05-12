# Agents And Runner

Agents declare:

- name;
- instructions;
- preferred model;
- allowed providers/models;
- accepted context types;
- allowed tools and MCP tools;
- execution limits;
- error policy.

The runner validates context, MCP requests, routing eligibility, provider
configuration, and adapter execution. Errors remain structured and do not become
successful textual responses.

V1 does not include graph engine, swarm, autonomous planner, self-reflection,
visual workflows, or complex multiagent orchestration.

