# arXiv curation - AI Safety

Curation of arXiv papers related to AI Safety, categorized and summarized by LLM.

## Overview (2026-01-04)
- **Agentic & Long-Horizon Risks**: This week's papers address agentic and long-horizon risks by introducing a novel framework, ASG-SI, for auditable and governable self-improving agentic LLMs. The key developments lie in its ability to compile improvements into verifiable skill graphs with reconstructible rewards, directly tackling issues like reward hacking and behavioral drift that are critical for controlling advanced AI systems.
- **Alignment**: This week's papers reveal new vulnerabilities and mitigation strategies for AI alignment. One study shows that emoji sequences can exploit safety mechanisms in LLMs, while another introduces GARDO to reinforce diffusion models and prevent reward hacking. Additionally, a new information-theoretic method, DIR, aims to eliminate inductive biases in reward models, thereby improving alignment with human values.
- **Misuse & Security**: This week's papers highlight significant advancements and persistent challenges in LLM security. Researchers are developing novel defensive strategies, such as guardrail models trained on compressed conversations and multimodal frameworks to prevent prompt injection attacks. However, new attack vectors, like multilingual hidden prompt injection and equation-solving based jailbreaks, demonstrate the ongoing arms race and the need for continuous refinement of safety filters across diverse attack scenarios.
- **Evaluation & Benchmarking**: This week's papers in Evaluation & Benchmarking introduce a new benchmark, JMedEthicBench, specifically designed to test the medical safety of Japanese Large Language Models in multi-turn conversations. This development highlights the need for specialized evaluations that capture the unique safety challenges arising from complex, extended dialogue, rather than just single-turn queries.


## Latest Papers (2026-01-04)

### Agentic & Long-Horizon Risks
_This week's papers address agentic and long-horizon risks by introducing a novel framework, ASG-SI, for auditable and governable self-improving agentic LLMs. The key developments lie in its ability to compile improvements into verifiable skill graphs with reconstructible rewards, directly tackling issues like reward hacking and behavioral drift that are critical for controlling advanced AI systems._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2025-12-28 | [Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory](http://arxiv.org/abs/2512.23760v1) | LLM, Reinforcement Learning, Agents, Security | ASG-SI is a framework that makes self-improving agentic LLMs auditable and governable by compiling improvements into verifiable skill graphs with reconstructible rewards, directly addressing security and control challenges like reward hacking and behavioral drift. |

### Alignment
_This week's papers reveal new vulnerabilities and mitigation strategies for AI alignment. One study shows that emoji sequences can exploit safety mechanisms in LLMs, while another introduces GARDO to reinforce diffusion models and prevent reward hacking. Additionally, a new information-theoretic method, DIR, aims to eliminate inductive biases in reward models, thereby improving alignment with human values._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-02 | [Emoji-Based Jailbreaking of Large Language Models](http://arxiv.org/abs/2601.00936v1) | LLM | This study empirically demonstrates that emoji sequences can be used as adversarial prompts to bypass safety alignment mechanisms in Large Language Models, highlighting vulnerabilities in prompt-level safety pipelines. |
| 2025-12-30 | [GARDO: Reinforcing Diffusion Models without Reward Hacking](http://arxiv.org/abs/2512.24138v1) | Reinforcement Learning | The paper introduces GARDO, a framework that mitigates reward hacking and enhances generation diversity in RL-tuned diffusion models by employing selective, adaptive regularization and diversity-aware reward amplification. |
| 2025-12-29 | [Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance](http://arxiv.org/abs/2512.23461v1) | LLM, Reinforcement Learning | This paper introduces DIR, an information-theoretic debiasing method for reward models that minimizes the influence of inductive biases like response length and sycophancy by optimizing mutual information, thereby enhancing RLHF performance and improving LLM alignment with human values. |

### Evaluation & Benchmarking
_This week's papers in Evaluation & Benchmarking introduce a new benchmark, JMedEthicBench, specifically designed to test the medical safety of Japanese Large Language Models in multi-turn conversations. This development highlights the need for specialized evaluations that capture the unique safety challenges arising from complex, extended dialogue, rather than just single-turn queries._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-04 | [JMedEthicBench: A Multi-Turn Conversational Benchmark for Evaluating Medical Safety in Japanese Large Language Models](http://arxiv.org/abs/2601.01627v1) | LLM, Healthcare | JMedEthicBench is a novel multi-turn conversational benchmark for evaluating the medical safety of Japanese LLMs, revealing vulnerabilities in domain-specific models and highlighting the distinct safety challenges of multi-turn interactions. |

### Misuse & Security
_This week's papers highlight significant advancements and persistent challenges in LLM security. Researchers are developing novel defensive strategies, such as guardrail models trained on compressed conversations and multimodal frameworks to prevent prompt injection attacks. However, new attack vectors, like multilingual hidden prompt injection and equation-solving based jailbreaks, demonstrate the ongoing arms race and the need for continuous refinement of safety filters across diverse attack scenarios._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-04 | [Automated Post-Incident Policy Gap Analysis via Threat-Informed Evidence Mapping using Large Language Models](http://arxiv.org/abs/2601.03287v1) | LLM, Security | This paper presents a novel LLM-based framework that integrates threat-informed evidence mapping and policy gap analysis for automated cybersecurity post-incident reviews, enhancing efficiency and auditability. |
| 2026-01-01 | [Defensive M2S: Training Guardrail Models on Compressed Multi-turn Conversations](http://arxiv.org/abs/2601.00454v1) | LLM | Defensive M2S trains guardrail models on compressed multi-turn conversations, significantly reducing computational costs for safety screening while maintaining high attack detection recall. |
| 2025-12-30 | [Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race?](http://arxiv.org/abs/2512.24044v1) | LLM | This paper presents the first systematic evaluation of jailbreak attacks across the full LLM deployment pipeline, revealing that safety filters are largely effective in detection but require further refinement to optimize protection and user experience. |
| 2025-12-29 | [Multilingual Hidden Prompt Injection Attacks on LLM-Based Academic Reviewing](http://arxiv.org/abs/2512.23684v1) | LLM | This paper reveals that LLM-based academic reviewing systems are highly susceptible to document-level hidden prompt injection attacks, leading to substantial changes in review outcomes, with vulnerability varying significantly across different languages. |
| 2025-12-29 | [Toward Trustworthy Agentic AI: A Multimodal Framework for Preventing Prompt Injection Attacks](http://arxiv.org/abs/2512.23557v1) | LLM, Multimodal, Agents | This paper proposes a Cross-Agent Multimodal Provenance-Aware Defense Framework, utilizing sanitization and validation agents coordinated by a provenance ledger, to effectively prevent multimodal prompt injection attacks in complex agentic AI systems. |
| 2025-12-29 | [EquaCode: A Multi-Strategy Jailbreak Approach for Large Language Models via Equation Solving and Code Completion](http://arxiv.org/abs/2512.23173v1) | LLM | This paper introduces EquaCode, a novel multi-strategy jailbreak approach that leverages equation solving and code completion to successfully bypass safety constraints in large language models, demonstrating significant vulnerabilities. |
| 2025-12-29 | [Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems](http://arxiv.org/abs/2512.23132v1) | LLM, Multimodal, Healthcare, Security | This paper systematically characterizes ML security risks by identifying dominant TTPs, vulnerabilities, and targeted lifecycle stages through a multi-agent RAG system, revealing unreported threats and emphasizing the need for adaptive, ML-specific security frameworks. |
| 2025-12-29 | [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](http://arxiv.org/abs/2512.23128v1) | Agents | This paper introduces TRAP, a benchmark for evaluating prompt injection attacks against web-based agents, demonstrating their susceptibility and revealing systemic vulnerabilities related to persuasion techniques. |
