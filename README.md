# arXiv curation - AI Safety

Curation of arXiv papers related to AI Safety, categorized and summarized by LLM.

## Overview (2026-01-14)
- **Alignment**: This week's papers highlight the importance of early safety interventions during pretraining for more robust models, and suggest that prioritizing reward precision over diverse constraints can lead to better instruction following. Research also indicates that intrinsic model characteristics, rather than just external data, are key to safety alignment, and that metaphors can unexpectedly cause cross-domain misalignment in large reasoning models.
- **Ethics & Human Values**: This week's papers on Ethics & Human Values highlight a shift in understanding AI alignment failures. Instead of viewing them as a result of conceptual errors in AI design, the research suggests that alignment issues are structural, arising from AI models learning and amplifying the full, often exploitative, spectrum of human interactions. This perspective frames AGI as an endogenous shock that could exacerbate existing human inconsistencies.
- **Evaluation & Benchmarking**: Updated with 5 new papers.
- **Governance & Policy**: Updated with 1 new papers.
- **Interpretability**: Updated with 1 new papers.
- **Misuse & Security**: Updated with 21 new papers.
- **Multi-Agent & Societal Dynamics**: This week's papers introduce M3-Bench, a novel evaluation framework for LLM agents specifically designed for mixed-motive games. This development allows for a deeper analysis of agent social behaviors by going beyond simple outcome metrics to assess their reasoning and communication processes within these complex social dynamics.
- **Robustness & Generalization**: Updated with 7 new papers.


## Latest Papers (2026-01-14)

### Agentic & Long-Horizon Risks


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2025-12-28 | [Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory](http://arxiv.org/abs/2512.23760v1) | LLM, Reinforcement Learning, Agents, Security | ASG-SI is a framework that makes self-improving agentic LLMs auditable and governable by compiling improvements into verifiable skill graphs with reconstructible rewards, directly addressing security and control challenges like reward hacking and behavioral drift. |

### Alignment
_This week's papers highlight the importance of early safety interventions during pretraining for more robust models, and suggest that prioritizing reward precision over diverse constraints can lead to better instruction following. Research also indicates that intrinsic model characteristics, rather than just external data, are key to safety alignment, and that metaphors can unexpectedly cause cross-domain misalignment in large reasoning models._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-13 | [YaPO: Learnable Sparse Activation Steering Vectors for Domain Adaptation](http://arxiv.org/abs/2601.08441v1) | LLM | YaPO introduces a novel method for learning sparse activation steering vectors via Sparse Autoencoders to achieve more disentangled, interpretable, and efficient fine-grained control over Large Language Model behaviors for alignment tasks. |
| 2026-01-12 | [AntiPaSTO: Self-Supervised Steering of Moral Reasoning](http://arxiv.org/abs/2601.07473v1) |  | AntiPaSTO introduces a self-supervised steering method that leverages contrasting word pairs to guide model representations along an anti-parallel axis, enabling scalable oversight of moral reasoning without requiring preference labels. |
| 2026-01-11 | [When Should We Introduce Safety Interventions During Pretraining?](http://arxiv.org/abs/2601.07087v1) |  | Introducing safety interventions earlier during pretraining leads to more robust, steerable, and interpretable models that are less susceptible to adversarial attacks or downstream finetuning. |
| 2026-01-08 | [Precision over Diversity: High-Precision Reward Generalizes to Robust Instruction Following](http://arxiv.org/abs/2601.04954v2) | LLM, Reinforcement Learning | This paper argues that prioritizing reward precision over constraint diversity in training reinforcement learning models for instruction following leads to more robust alignment and generalization, challenging the conventional wisdom that diverse constraints are essential. |
| 2026-01-07 | [What Matters For Safety Alignment?](http://arxiv.org/abs/2601.03868v1) | LLM | This paper empirically identifies intrinsic model characteristics that improve safety alignment in LLMs and LRMs, reveals vulnerabilities in text-completion interfaces, and suggests safety should be an explicit optimization objective during training. |
| 2026-01-06 | [Metaphors are a Source of Cross-Domain Misalignment of Large Reasoning Models](http://arxiv.org/abs/2601.03388v1) | LLM | This paper demonstrates a causal relationship between metaphors in training data and the emergent cross-domain misalignment of large reasoning models, suggesting metaphors can induce generalization of learned misaligned patterns. |
| 2026-01-05 | [GDRO: Group-level Reward Post-training Suitable for Diffusion Models](http://arxiv.org/abs/2601.02036v1) | LLM, Reinforcement Learning | GDRO is a novel post-training method for diffusion models that achieves efficient, offline group-level reward alignment by addressing sampling efficiency and stochasticity issues inherent in rectified flow models. |
| 2026-01-02 | [Emoji-Based Jailbreaking of Large Language Models](http://arxiv.org/abs/2601.00936v1) | LLM | This study empirically demonstrates that emoji sequences can be used as adversarial prompts to bypass safety alignment mechanisms in Large Language Models, highlighting vulnerabilities in prompt-level safety pipelines. |
| 2025-12-30 | [GARDO: Reinforcing Diffusion Models without Reward Hacking](http://arxiv.org/abs/2512.24138v1) | Reinforcement Learning | The paper introduces GARDO, a framework that mitigates reward hacking and enhances generation diversity in RL-tuned diffusion models by employing selective, adaptive regularization and diversity-aware reward amplification. |
| 2025-12-29 | [Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance](http://arxiv.org/abs/2512.23461v1) | LLM, Reinforcement Learning | This paper introduces DIR, an information-theoretic debiasing method for reward models that minimizes the influence of inductive biases like response length and sycophancy by optimizing mutual information, thereby enhancing RLHF performance and improving LLM alignment with human values. |

### Ethics & Human Values
_This week's papers on Ethics & Human Values highlight a shift in understanding AI alignment failures. Instead of viewing them as a result of conceptual errors in AI design, the research suggests that alignment issues are structural, arising from AI models learning and amplifying the full, often exploitative, spectrum of human interactions. This perspective frames AGI as an endogenous shock that could exacerbate existing human inconsistencies._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-14 | [A Scoping Review of the Ethical Perspectives on Anthropomorphising Large Language Model-Based Conversational Agents](http://arxiv.org/abs/2601.09869v1) | LLM, Agents | This scoping review maps ethically oriented work on anthropomorphising LLM-based conversational agents, identifying conceptual foundations, ethical challenges and opportunities, and methodological approaches, while highlighting a need for more empirical work linking interaction effects to governance guidance. |
| 2026-01-13 | [Why AI Alignment Failure Is Structural: Learned Human Interaction Structures and AGI as an Endogenous Evolutionary Shock](http://arxiv.org/abs/2601.08673v1) | LLM | The paper argues that AI alignment failures stem from models learning the full spectrum of human interaction, including exploitative behaviors, rather than a conceptual error, suggesting the risk is structural amplification of human inconsistencies rather than adversarial intent. |

### Evaluation & Benchmarking
_Updated with 5 new papers._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-13 | [BenchOverflow: Measuring Overflow in Large Language Models via Plain-Text Prompts](http://arxiv.org/abs/2601.08490v1) | LLM | The paper introduces BenchOverflow, a novel benchmark for measuring and mitigating excessive LLM output length, which has significant implications for cost, latency, and resource consumption. |
| 2026-01-09 | [Automated QoR improvement in OpenROAD with coding agents](http://arxiv.org/abs/2601.06268v1) | LLM, Agents | This paper introduces AuDoPEDA, a closed-loop LLM framework that autonomously improves EDA code within the OpenROAD system, demonstrating significant performance gains in PPA metrics. |
| 2026-01-09 | [PII-VisBench: Evaluating Personally Identifiable Information Safety in Vision Language Models Along a Continuum of Visibility](http://arxiv.org/abs/2601.05739v1) |  | PII-VisBench introduces a new benchmark to evaluate vision-language model PII safety across a continuum of subject visibility, revealing that models are more prone to PII disclosure for high-visibility individuals. |
| 2026-01-07 | [MiJaBench: Revealing Minority Biases in Large Language Models via Hate Speech Jailbreaking](http://arxiv.org/abs/2601.04389v1) | LLM, Security | MiJaBench is a new bilingual benchmark that reveals how LLM safety alignment is not generalized but hierarchical across demographic groups, with model scaling potentially exacerbating these biases. |
| 2026-01-05 | [Code for Machines, Not Just Humans: Quantifying AI-Friendliness with Code Health Metrics](http://arxiv.org/abs/2601.02200v1) | LLM, Agents | This paper introduces and validates a metric (CodeHealth) for quantifying AI-friendliness in code, demonstrating that human-friendly code is also more robust to AI-driven refactoring. |
| 2026-01-04 | [JMedEthicBench: A Multi-Turn Conversational Benchmark for Evaluating Medical Safety in Japanese Large Language Models](http://arxiv.org/abs/2601.01627v1) | LLM, Healthcare | JMedEthicBench is a novel multi-turn conversational benchmark for evaluating the medical safety of Japanese LLMs, revealing vulnerabilities in domain-specific models and highlighting the distinct safety challenges of multi-turn interactions. |

### Governance & Policy
_Updated with 1 new papers._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-09 | [Toward Safe and Responsible AI Agents: A Three-Pillar Model for Transparency, Accountability, and Trustworthiness](http://arxiv.org/abs/2601.06223v1) | Reinforcement Learning, Agents | This paper proposes a Three-Pillar Model for safe AI agents based on transparency, accountability, and trustworthiness, advocating for a staged development approach analogous to autonomous driving to balance automation and human oversight. |

### Interpretability
_Updated with 1 new papers._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-06 | [When the Coffee Feature Activates on Coffins: An Analysis of Feature Extraction and Steering for Mechanistic Interpretability](http://arxiv.org/abs/2601.03047v1) |  | This paper critically examines the reliability and generalizability of sparse autoencoders for mechanistic interpretability in LLMs, finding significant fragility in feature extraction and steering, which raises concerns for their application in AI safety. |

### Misuse & Security
_Updated with 21 new papers._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-14 | [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](http://arxiv.org/abs/2601.09923v1) | Agents, Security | This paper introduces Single-Shot Planning for Computer Use Agents, which generates a complete execution graph beforehand to ensure control flow integrity against prompt injection attacks while maintaining performance. |
| 2026-01-14 | [The Promptware Kill Chain: How Prompt Injections Gradually Evolved Into a Multi-Step Malware](http://arxiv.org/abs/2601.09625v1) | LLM, Agents, Security | The paper introduces the concept of 'promptware' and a five-step kill chain model to analyze multi-step attacks on LLM-based systems, drawing parallels to traditional malware campaigns. |
| 2026-01-12 | [When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent](http://arxiv.org/abs/2601.07263v1) | LLM, Agents, Security | This paper introduces AgentBait, a novel social engineering attack against web automation agents, and proposes SUPERVISOR, a runtime mitigation technique to enforce consistency and prevent malicious objectives. |
| 2026-01-11 | [Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems](http://arxiv.org/abs/2601.07072v1) | LLM | This paper demonstrates an efficient black-box attack method to ensure malicious instructions embedded in external corpora are retrieved by LLM systems, enabling practical indirect prompt injection exploits with near 100% retrieval success. |
| 2026-01-11 | [Paraphrasing Adversarial Attack on LLM-as-a-Reviewer](http://arxiv.org/abs/2601.06884v1) | LLM | The paper introduces a Paraphrasing Adversarial Attack (PAA) that manipulates LLM reviewers' scores by subtly altering manuscript content without changing claims, demonstrating a new vulnerability in LLM-based evaluation systems. |
| 2026-01-09 | [VIGIL: Defending LLM Agents Against Tool Stream Injection via Verify-Before-Commit](http://arxiv.org/abs/2601.05755v2) | LLM, Agents, Security | VIGIL introduces a verify-before-commit protocol for LLM agents to defend against tool stream injection attacks by speculative hypothesis generation and intent-grounded verification. |
| 2026-01-09 | [The Echo Chamber Multi-Turn LLM Jailbreak](http://arxiv.org/abs/2601.05742v1) | LLM, Security | The paper introduces Echo Chamber, a novel multi-turn jailbreaking attack on LLMs that uses gradual escalation to bypass safety guardrails. |
| 2026-01-09 | [FinVault: Benchmarking Financial Agent Safety in Execution-Grounded Environments](http://arxiv.org/abs/2601.07853v1) | LLM, Agents, Security | This paper introduces FinVault, the first execution-grounded security benchmark for financial agents, highlighting significant vulnerabilities in LLM-powered financial systems that existing defenses fail to address. |
| 2026-01-09 | [STELP: Secure Transpilation and Execution of LLM-Generated Programs](http://arxiv.org/abs/2601.05467v2) | LLM | This paper proposes STELP, a secure transpiler and executor designed to safely handle and run code generated by Large Language Models (LLMs) in production AI systems, addressing vulnerabilities like data poisoning and malicious attacks. |
| 2026-01-09 | [Jailbreaking Large Language Models through Iterative Tool-Disguised Attacks via Reinforcement Learning](http://arxiv.org/abs/2601.05466v1) | LLM, Reinforcement Learning | The paper introduces iMIST, an adaptive jailbreak method that disguises malicious queries as tool invocations and uses interactive reinforcement learning to progressively escalate harmfulness, revealing critical vulnerabilities in current LLM safety mechanisms. |
| 2026-01-09 | [Knowledge-Driven Multi-Turn Jailbreaking on Large Language Models](http://arxiv.org/abs/2601.05445v1) | LLM | Mastermind is a novel multi-turn jailbreaking framework that uses a closed loop of planning, execution, and reflection to autonomously discover and adapt attack patterns against LLMs, significantly outperforming existing methods. |
| 2026-01-08 | [Multi-turn Jailbreaking Attack in Multi-Modal Large Language Models](http://arxiv.org/abs/2601.05339v1) | LLM, Security | This paper introduces a novel multi-turn jailbreaking attack and a fragment-optimized, multi-LLM-based defense mechanism (FragGuard) to address security vulnerabilities in multi-modal large language models. |
| 2026-01-08 | [Defense Against Indirect Prompt Injection via Tool Result Parsing](http://arxiv.org/abs/2601.04795v1) | LLM, Agents, Robotics | This paper proposes a novel tool result parsing method that effectively filters injected malicious code to defend LLM agents against indirect prompt injection attacks. |
| 2026-01-08 | [Know Thy Enemy: Securing LLMs Against Prompt Injection via Diverse Data Synthesis and Instruction-Level Chain-of-Thought Learning](http://arxiv.org/abs/2601.04666v1) | LLM, Security | InstruCoT enhances LLM security against prompt injection by synthesizing diverse training data and employing instruction-level chain-of-thought fine-tuning to identify and reject malicious instructions. |
| 2026-01-08 | [Autonomous Agents on Blockchains: Standards, Execution Models, and Trust Boundaries](http://arxiv.org/abs/2601.04583v1) | Agents, Security | This paper surveys agent-blockchain interoperability, proposing a taxonomy, threat model, and research roadmap focused on securing agent-driven on-chain execution to mitigate risks. |
| 2026-01-07 | [HoneyTrap: Deceiving Large Language Model Attackers to Honeypot Traps with Resilient Multi-Agent Defense](http://arxiv.org/abs/2601.04034v1) | LLM, Agents, Security | HoneyTrap is a novel deceptive LLM defense framework that uses collaborative agents to detect and misdirect jailbreak attacks, increasing attacker resource consumption and reducing attack success rates. |
| 2026-01-07 | [ALERT: Zero-shot LLM Jailbreak Detection via Internal Discrepancy Amplification](http://arxiv.org/abs/2601.03600v1) | LLM, Security | This paper proposes ALERT, an efficient zero-shot jailbreak detection method that amplifies internal feature discrepancies to identify malicious prompts without relying on pre-existing attack templates. |
| 2026-01-06 | [Interpretable All-Type Audio Deepfake Detection with Audio LLMs via Frequency-Time Reinforcement Learning](http://arxiv.org/abs/2601.02983v1) | LLM, Reinforcement Learning | This paper proposes a novel Frequency Time-Group Relative Policy Optimization (FT-GRPO) method using audio large language models (ALLMs) and structured chain-of-thought rationales to achieve interpretable and robust detection of all types of audio deepfakes. |
| 2026-01-06 | [Adversarial Contrastive Learning for LLM Quantization Attacks](http://arxiv.org/abs/2601.02680v1) | LLM, Security | The paper introduces Adversarial Contrastive Learning (ACL), a novel gradient-based quantization attack that enhances the effectiveness of malicious LLM behaviors by explicitly maximizing the probability gap between benign and harmful responses. |
| 2026-01-06 | [TRYLOCK: Defense-in-Depth Against LLM Jailbreaks via Layered Preference and Representation Engineering](http://arxiv.org/abs/2601.03300v1) | LLM, Security | TRYLOCK introduces a defense-in-depth architecture combining weight-level alignment, activation-level steering, adaptive strength selection, and input canonicalization to significantly reduce LLM jailbreak success rates without substantial usability trade-offs. |
| 2026-01-06 | [Extracting books from production language models](http://arxiv.org/abs/2601.02671v1) | LLM | This paper demonstrates that even production LLMs with safety measures can leak copyrighted training data through extraction attacks, challenging the assumption that such safeguards prevent memorization exposure. |
| 2026-01-05 | [Exploring Approaches for Detecting Memorization of Recommender System Data in Large Language Models](http://arxiv.org/abs/2601.02002v1) | LLM | This paper explores and evaluates automated prompting strategies for detecting memorization and data leakage in Large Language Models used for recommendations, outperforming manual prompting and unsupervised methods. |
| 2026-01-05 | [Crafting Adversarial Inputs for Large Vision-Language Models Using Black-Box Optimization](http://arxiv.org/abs/2601.01747v2) | Multimodal | This paper introduces a gradient-free black-box optimization method (ZO-SPSA) to effectively craft adversarial jailbreak attacks on large vision-language models, demonstrating their vulnerability to harmful outputs even without model knowledge. |
| 2026-01-04 | [Automated Post-Incident Policy Gap Analysis via Threat-Informed Evidence Mapping using Large Language Models](http://arxiv.org/abs/2601.03287v1) | LLM, Security | This paper presents a novel LLM-based framework that integrates threat-informed evidence mapping and policy gap analysis for automated cybersecurity post-incident reviews, enhancing efficiency and auditability. |
| 2026-01-01 | [Defensive M2S: Training Guardrail Models on Compressed Multi-turn Conversations](http://arxiv.org/abs/2601.00454v1) | LLM | Defensive M2S trains guardrail models on compressed multi-turn conversations, significantly reducing computational costs for safety screening while maintaining high attack detection recall. |
| 2025-12-30 | [Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race?](http://arxiv.org/abs/2512.24044v1) | LLM | This paper presents the first systematic evaluation of jailbreak attacks across the full LLM deployment pipeline, revealing that safety filters are largely effective in detection but require further refinement to optimize protection and user experience. |
| 2025-12-29 | [Multilingual Hidden Prompt Injection Attacks on LLM-Based Academic Reviewing](http://arxiv.org/abs/2512.23684v1) | LLM | This paper reveals that LLM-based academic reviewing systems are highly susceptible to document-level hidden prompt injection attacks, leading to substantial changes in review outcomes, with vulnerability varying significantly across different languages. |
| 2025-12-29 | [Toward Trustworthy Agentic AI: A Multimodal Framework for Preventing Prompt Injection Attacks](http://arxiv.org/abs/2512.23557v1) | LLM, Multimodal, Agents | This paper proposes a Cross-Agent Multimodal Provenance-Aware Defense Framework, utilizing sanitization and validation agents coordinated by a provenance ledger, to effectively prevent multimodal prompt injection attacks in complex agentic AI systems. |
| 2025-12-29 | [EquaCode: A Multi-Strategy Jailbreak Approach for Large Language Models via Equation Solving and Code Completion](http://arxiv.org/abs/2512.23173v1) | LLM | This paper introduces EquaCode, a novel multi-strategy jailbreak approach that leverages equation solving and code completion to successfully bypass safety constraints in large language models, demonstrating significant vulnerabilities. |
| 2025-12-29 | [Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems](http://arxiv.org/abs/2512.23132v1) | LLM, Multimodal, Healthcare, Security | This paper systematically characterizes ML security risks by identifying dominant TTPs, vulnerabilities, and targeted lifecycle stages through a multi-agent RAG system, revealing unreported threats and emphasizing the need for adaptive, ML-specific security frameworks. |
| 2025-12-29 | [It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](http://arxiv.org/abs/2512.23128v1) | Agents | This paper introduces TRAP, a benchmark for evaluating prompt injection attacks against web-based agents, demonstrating their susceptibility and revealing systemic vulnerabilities related to persuasion techniques. |

### Multi-Agent & Societal Dynamics
_This week's papers introduce M3-Bench, a novel evaluation framework for LLM agents specifically designed for mixed-motive games. This development allows for a deeper analysis of agent social behaviors by going beyond simple outcome metrics to assess their reasoning and communication processes within these complex social dynamics._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-13 | [M3-BENCH: Process-Aware Evaluation of LLM Agents Social Behaviors in Mixed-Motive Games](http://arxiv.org/abs/2601.08462v1) | LLM, Agents | M3-Bench introduces a process-aware evaluation framework for LLM agents in mixed-motive games, analyzing behavior, reasoning, and communication to characterize nuanced social behaviors beyond simple outcomes. |

### Robustness & Generalization
_Updated with 7 new papers._


| Date | Title | Tags | Summary |
|---|---|---|---|
| 2026-01-12 | [Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids](http://arxiv.org/abs/2601.07718v1) | Reinforcement Learning | This paper introduces a scalable, end-to-end perceptive parkour framework for humanoids that enhances robustness in complex terrains through novel safety mechanisms and training strategies. |
| 2026-01-12 | [Lost in the Noise: How Reasoning Models Fail with Contextual Distractors](http://arxiv.org/abs/2601.07226v1) | Agents | This paper introduces NoisyBench, a benchmark evaluating model robustness against contextual distractors, revealing significant performance drops and demonstrating that the proposed Rationale-Aware Reward (RARE) significantly enhances resilience. |
| 2026-01-09 | [IIB-LPO: Latent Policy Optimization via Iterative Information Bottleneck](http://arxiv.org/abs/2601.05870v1) | LLM, Reinforcement Learning | IIB-LPO diversifies Large Language Model reasoning trajectories by triggering latent branching at high-entropy states and using the Information Bottleneck principle for concise exploration, overcoming exploration collapse in Reinforcement Learning with Verifiable Rewards. |
| 2026-01-08 | [Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning](http://arxiv.org/abs/2601.04805v1) | Reinforcement Learning | Thinking-Based Non-Thinking (TNT) mitigates reward hacking in hybrid reasoning models by dynamically setting token limits for non-thinking responses, improving efficiency and accuracy without supervised fine-tuning. |
| 2026-01-08 | [Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks](http://arxiv.org/abs/2601.04603v1) |  | The paper introduces Constitutional Classifiers++, an efficient defense system against universal jailbreaks that uses context-aware exchange classifiers and a two-stage cascade to significantly reduce computational costs and refusal rates. |
| 2026-01-07 | [Neuro-Symbolic Compliance: Integrating LLMs and SMT Solvers for Automated Financial Legal Analysis](http://arxiv.org/abs/2601.06181v1) | LLM | This paper introduces a neuro-symbolic framework that leverages LLMs and SMT solvers to achieve verifiable and optimized financial legal compliance. |
| 2026-01-07 | [Trade-R1: Bridging Verifiable Rewards to Stochastic Environments via Process-Level Reasoning Verification](http://arxiv.org/abs/2601.03948v2) | LLM, Reinforcement Learning | Trade-R1 bridges verifiable rewards to stochastic financial environments by transforming reasoning evaluation into a RAG task with a triangular consistency metric to filter noisy rewards and reduce reward hacking. |
| 2026-01-06 | [Jailbreaking LLMs Without Gradients or Priors: Effective and Transferable Attacks](http://arxiv.org/abs/2601.03420v1) | LLM | RAILS is a novel gradient-free and prior-free iterative optimization framework for jailbreaking LLMs that uses an auto-regressive loss and history-based selection to achieve high transferability to closed-source models. |
| 2026-01-06 | [JPU: Bridging Jailbreak Defense and Unlearning via On-Policy Path Rectification](http://arxiv.org/abs/2601.03005v1) | LLM | JPU rectifies dynamic jailbreak paths by dynamically mining on-policy adversarial samples, enhancing LLM resistance to jailbreaks without sacrificing utility. |
