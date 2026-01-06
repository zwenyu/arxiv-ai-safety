# arXiv curation - AI Safety

Curation of arXiv papers related to AI Safety, categorized and summarized by LLM.

## Overview (2026-01-02)
- **Agentic & Long-Horizon Risks**: This week's papers highlight a new framework, ASG-SI, designed to enhance the safety and control of self-improving agentic LLMs. It directly addresses security challenges like reward hacking and behavioral drift by making LLM improvements auditable and governable through verifiable skill graphs with reconstructible rewards.
- **Alignment**: This week's papers highlight a significant development in improving LLM alignment by addressing inductive biases in reward models. A new method, DIR, utilizes information-theoretic guidance to minimize the influence of biases like response length and sycophancy, thereby enhancing RLHF performance and better aligning LLMs with human values.
- **Misuse & Security**: This week's papers reveal widespread vulnerabilities to prompt injection and jailbreaking techniques across various AI systems, from LLM-based academic reviewing to web-based agents. Researchers introduced methods like multilingual hidden prompt injection and the multi-strategy EquaCode jailbreak, while also proposing defense frameworks for multimodal prompt injection in complex agentic AI systems and characterizing broader ML security risks.


## Latest Papers (2026-01-02)

### Agentic & Long-Horizon Risks
_This week's papers highlight a new framework, ASG-SI, designed to enhance the safety and control of self-improving agentic LLMs. It directly addresses security challenges like reward hacking and behavioral drift by making LLM improvements auditable and governable through verifiable skill graphs with reconstructible rewards._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2025-12-28 | [Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory](http://arxiv.org/abs/2512.23760v1) | LLM, Reinforcement Learning, Agents, Security | ASG-SI is a framework that makes self-improving agentic LLMs auditable and governable by compiling improvements into verifiable skill graphs with reconstructible rewards, directly addressing security and control challenges like reward hacking and behavioral drift. |

### Alignment
_This week's papers highlight a significant development in improving LLM alignment by addressing inductive biases in reward models. A new method, DIR, utilizes information-theoretic guidance to minimize the influence of biases like response length and sycophancy, thereby enhancing RLHF performance and better aligning LLMs with human values._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-02 | [Emoji-Based Jailbreaking of Large Language Models](http://arxiv.org/abs/2601.00936v1) | LLM | This study empirically demonstrates that emoji sequences can be used as adversarial prompts to bypass safety alignment mechanisms in Large Language Models, highlighting vulnerabilities in prompt-level safety pipelines. |
| 2025-12-30 | [GARDO: Reinforcing Diffusion Models without Reward Hacking](http://arxiv.org/abs/2512.24138v1) | Reinforcement Learning | The paper introduces GARDO, a framework that mitigates reward hacking and enhances generation diversity in RL-tuned diffusion models by employing selective, adaptive regularization and diversity-aware reward amplification. |
| 2025-12-29 | [Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance](http://arxiv.org/abs/2512.23461v1) | LLM, Reinforcement Learning | This paper introduces DIR, an information-theoretic debiasing method for reward models that minimizes the influence of inductive biases like response length and sycophancy by optimizing mutual information, thereby enhancing RLHF performance and improving LLM alignment with human values. |

### Misuse & Security
_This week's papers reveal widespread vulnerabilities to prompt injection and jailbreaking techniques across various AI systems, from LLM-based academic reviewing to web-based agents. Researchers introduced methods like multilingual hidden prompt injection and the multi-strategy EquaCode jailbreak, while also proposing defense frameworks for multimodal prompt injection in complex agentic AI systems and characterizing broader ML security risks._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-01 | [Defensive M2S: Training Guardrail Models on Compressed Multi-turn Conversations](http://arxiv.org/abs/2601.00454v1) | LLM | Defensive M2S trains guardrail models on compressed multi-turn conversations, significantly reducing computational costs for safety screening while maintaining high attack detection recall. |
| 2025-12-30 | [Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race?](http://arxiv.org/abs/2512.24044v1) | LLM | This paper presents the first systematic evaluation of jailbreak attacks across the full LLM deployment pipeline, revealing that safety filters are largely effective in detection but require further refinement to optimize protection and user experience. |
| 2025-12-29 | [Multilingual Hidden Prompt Injection Attacks on LLM-Based Academic Reviewing](http://arxiv.org/abs/2512.23684v1) | LLM | This paper reveals that LLM-based academic reviewing systems are highly susceptible to document-level hidden prompt injection attacks, leading to substantial changes in review outcomes, with vulnerability varying significantly across different languages. |
| 2025-12-29 | [Toward Trustworthy Agentic AI: A Multimodal Framework for Preventing Prompt Injection Attacks](http://arxiv.org/abs/2512.23557v1) | LLM, Multimodal, Agents | This paper proposes a Cross-Agent Multimodal Provenance-Aware Defense Framework, utilizing sanitization and validation agents coordinated by a provenance ledger, to effectively prevent multimodal prompt injection attacks in complex agentic AI systems. |
| 2025-12-29 | [EquaCode: A Multi-Strategy Jailbreak Approach for Large Language Models via Equation Solving and Code Completion](http://arxiv.org/abs/2512.23173v1) | LLM | This paper introduces EquaCode, a novel multi-strategy jailbreak approach that leverages equation solving and code completion to successfully bypass safety constraints in large language models, demonstrating significant vulnerabilities. |
| 2025-12-29 | [Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems](http://arxiv.org/abs/2512.23132v1) | LLM, Multimodal, Healthcare, Security | This paper systematically characterizes ML security risks by identifying dominant TTPs, vulnerabilities, and targeted lifecycle stages through a multi-agent RAG system, revealing unreported threats and emphasizing the need for adaptive, ML-specific security frameworks. |
| 2025-12-29 | [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](http://arxiv.org/abs/2512.23128v1) | Agents | This paper introduces TRAP, a benchmark for evaluating prompt injection attacks against web-based agents, demonstrating their susceptibility and revealing systemic vulnerabilities related to persuasion techniques. |
