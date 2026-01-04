# arXiv curation - AI Safety

Daily curation of arXiv papers related to AI Safety, categorized and summarized by LLM.

## Overview (2025-12-30)
- **Agentic & Long-Horizon Risks**: This week's papers introduce Audited Skill-Graph Self-Improvement (ASG-SI) as a method to enhance the safety and governance of agentic LLMs. ASG-SI enables iterative self-improvement by compiling agent capabilities into an auditable skill graph, further bolstered by verifiable rewards and reusable components to ensure transparency and control.
- **Alignment**: This week's papers address alignment challenges by focusing on improving reward models. One key development is the introduction of DIR, an information-theoretic guidance method, which aims to eliminate inductive biases in reward models used in RLHF. This approach is shown to lead to better alignment with human preferences and improved generalization capabilities.
- **Misuse & Security**: This week's papers highlight significant advancements in understanding and defending against prompt injection attacks, which can manipulate LLMs and web agents. Developments include multilingual attack vectors demonstrating risks in sensitive workflows, novel defense frameworks employing multimodal sanitization and output validation, and a benchmark for evaluating agent susceptibility to task redirection. Furthermore, a new jailbreaking approach using equation solving and code completion underscores the ongoing security challenges in bypassing LLM safety constraints.


## Latest Papers (2025-12-30)

### Agentic & Long-Horizon Risks
_This week's papers introduce Audited Skill-Graph Self-Improvement (ASG-SI) as a method to enhance the safety and governance of agentic LLMs. ASG-SI enables iterative self-improvement by compiling agent capabilities into an auditable skill graph, further bolstered by verifiable rewards and reusable components to ensure transparency and control._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2025-12-28 | [Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory](http://arxiv.org/abs/2512.23760v1) | LLM, Reinforcement Learning, Agents, Security | This paper proposes Audited Skill-Graph Self-Improvement (ASG-SI) to address security and governance challenges in agentic LLMs by making self-improvement iterative compilation into an auditable skill graph with verifiable rewards and reusable capabilities. |

### Alignment
_This week's papers address alignment challenges by focusing on improving reward models. One key development is the introduction of DIR, an information-theoretic guidance method, which aims to eliminate inductive biases in reward models used in RLHF. This approach is shown to lead to better alignment with human preferences and improved generalization capabilities._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2025-12-30 | [GARDO: Reinforcing Diffusion Models without Reward Hacking](http://arxiv.org/abs/2512.24138v1) | Reinforcement Learning | This paper proposes GARDO, a framework that improves the alignment of diffusion models by reinforcing them without reward hacking, enhancing sample efficiency and generation diversity. |
| 2025-12-29 | [Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance](http://arxiv.org/abs/2512.23461v1) | LLM, Reinforcement Learning | This paper introduces a novel information-theoretic method, DIR, to mitigate inductive biases in reward models used for RLHF, leading to improved alignment with human preferences and enhanced generalization. |

### Misuse & Security
_This week's papers highlight significant advancements in understanding and defending against prompt injection attacks, which can manipulate LLMs and web agents. Developments include multilingual attack vectors demonstrating risks in sensitive workflows, novel defense frameworks employing multimodal sanitization and output validation, and a benchmark for evaluating agent susceptibility to task redirection. Furthermore, a new jailbreaking approach using equation solving and code completion underscores the ongoing security challenges in bypassing LLM safety constraints._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2025-12-30 | [Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race?](http://arxiv.org/abs/2512.24044v1) | LLM | This paper systematically evaluates the effectiveness of jailbreak attacks against LLM safety filters, revealing that while filters can detect most attacks, there's a need to optimize their performance for better recall and precision. |
| 2025-12-29 | [Multilingual Hidden Prompt Injection Attacks on LLM-Based Academic Reviewing](http://arxiv.org/abs/2512.23684v1) | LLM | This paper demonstrates a significant security vulnerability in LLM applications, specifically prompt injection attacks that can manipulate academic review outcomes across different languages, highlighting risks in the deployment of LLMs in sensitive workflows. |
| 2025-12-29 | [Toward Trustworthy Agentic AI: A Multimodal Framework for Preventing Prompt Injection Attacks](http://arxiv.org/abs/2512.23557v1) | LLM, Multimodal, Agents | This paper proposes a multimodal framework to defend against prompt injection attacks in agentic AI systems, enhancing security and trustworthiness by sanitizing prompts and validating outputs across agents. |
| 2025-12-29 | [EquaCode: A Multi-Strategy Jailbreak Approach for Large Language Models via Equation Solving and Code Completion](http://arxiv.org/abs/2512.23173v1) | LLM | This paper introduces EquaCode, a novel multi-strategy jailbreak approach for LLMs that leverages equation solving and code completion to bypass safety constraints and elicit harmful responses, highlighting a significant security vulnerability. |
| 2025-12-29 | [Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems](http://arxiv.org/abs/2512.23132v1) | LLM, Multimodal, Healthcare, Security | This paper addresses critical security risks and vulnerabilities in AI-based systems, particularly foundation models, by developing a multi-agent framework to identify and characterize emerging threats, thereby contributing to the robustness and security of AI applications. |
| 2025-12-29 | [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](http://arxiv.org/abs/2512.23128v1) | Agents | This paper introduces a benchmark and framework for evaluating the susceptibility of web agents to prompt injection attacks, revealing systemic vulnerabilities that can be exploited to redirect agent behavior. |
