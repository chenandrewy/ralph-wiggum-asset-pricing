Title: AI Automated Research Literature Notes
Date: 2026-04-08
Time: 14:36:49 EDT

Summary

I searched for recent papers on automated generation of academic research using AI, with a follow-up focus on economics, finance, and policy evaluation. The main pattern is that most end-to-end paper-generation systems are oriented toward scaling the research production process, while the more quality-oriented papers tend to focus on hypothesis generation, proposal support, review, or scientist-in-the-loop assistance rather than full paper generation.

General automated research papers

- Chris Lu et al., "Towards end-to-end automation of AI research" (Nature, 2026). Most direct successor to the 2024 AI Scientist line. End-to-end automation orientation.
  Link: https://www.nature.com/articles/s41586-026-10265-5
- Yutaro Yamada et al., "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search" (arXiv, 2025). End-to-end paper-generation pipeline with stronger search and selection.
  Link: https://huggingface.co/papers/2504.08066
- Juraj Gottweis et al., "Towards an AI co-scientist" (arXiv, 2025). More scientist-in-the-loop and hypothesis/proposal oriented than paper-generation oriented.
  Links: https://huggingface.co/papers/2502.18864 ; https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/
- Samuel Schmidgall and Michael Moor, "AgentRxiv: Towards Collaborative Autonomous Research" (arXiv, 2025). Collaborative autonomous research infrastructure with a scaling orientation.
  Link: https://huggingface.co/papers/2503.18102
- Yixuan Weng et al., "CycleResearcher: Improving Automated Research via Automated Review" (arXiv, 2024; ICLR 2025 poster). Automated review-and-revision loop.
  Links: https://openreview.net/forum?id=bjcsVLoHYs ; https://huggingface.co/papers/2411.00816
- Jiabin Tang et al., "AI-Researcher: Autonomous Scientific Innovation" (NeurIPS 2025 spotlight). Mixed orientation: still scalable autonomous research, but with stronger innovation/benchmark emphasis.
  Link: https://openreview.net/forum?id=kQWyOYUAC4

Economics and finance focused papers

- Anton Korinek, "AI Agents for Economic Research" (NBER Working Paper 34202, 2025). Closest economics-specific paper on agentic workflows across the research process.
  Link: https://www.nber.org/papers/w34202
- Herbert Dawid, Philipp Harting, Hankui Wang, Zhongli Wang, and Jiachen Yi, "Agentic Workflows for Economic Research: Design and Implementation" (arXiv, 2025). Economics-focused workflow design for AI-assisted research.
  Link: https://ideas.repec.org/p/arx/papers/2504.09736.html
- Marc Schmitt, "AI-Driven Exploration and Hypothesis Generation in Finance and Economics" (SSRN, 2025). Finance/econ framed, but centered on exploration and hypothesis generation rather than full paper generation.
  Link: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5126623
- Andrea L. Eisfeldt and Gregor Schubert, "AI and Finance" (NBER Working Paper 33076, 2024). Field-level methods and implications paper, not an automated paper-generation algorithm.
  Link: https://www.nber.org/papers/w33076
- Hongwei Mo and Shumiao Ouyang, "(Generative) AI in Financial Economics" (SSRN, 2025; revised 2026). Broad review of generative AI in financial economics.
  Link: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5287110
- Jens Ludwig and Sendhil Mullainathan, "Machine Learning as a Tool for Hypothesis Generation" (NBER Working Paper 31017 / BFI WP, 2023). Important background on algorithmic hypothesis generation in economics.
  Link: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4386605

European policy evaluation project

- Autonomous Policy Evaluation Project (APE), Social Catalyst Lab, University of Zurich. This appears to be the Europe-based project I was trying to identify. It has a public site and public codebase and is explicitly focused on automating policy evaluation.
  Homepage: https://ape.socialcatalystlab.org/
  About: https://ape.socialcatalystlab.org/about
  Methodology: https://ape.socialcatalystlab.org/methodology
  Autonomy page: https://ape.socialcatalystlab.org/autonomy
  GitHub: https://github.com/SocialCatalystLab/ape-papers

APE paper status

I did not verify a standalone methods paper for APE itself. What is public is the project website, methodology pages marked as work in progress, generated working papers, and the code repository. My current inference is that the project is public and active, but the formal paper or report either does not yet exist or was not easy to verify from public sources.

Characterization by orientation

- Throughput / research-production scaling: Lu et al. (2026), AI Scientist-v2, AgentRxiv, CycleResearcher, AI-Researcher, and especially APE.
- Mixed workflow and support orientation: Korinek (2025), Dawid et al. (2025).
- More quality-oriented but not paper-generation algorithms: AI co-scientist, Schmitt (2025), Eisfeldt and Schubert (2024), Ludwig and Mullainathan (2023).

Main substantive conclusion

Among the more quality-oriented papers, I did not find clear examples that are mainly algorithms for generating complete academic papers. Full paper-generation algorithms mostly sit in the pipeline-scaling camp, while the more quality-oriented work is typically upstream and focused on idea generation, hypothesis generation, critique, review, or researcher assistance.
