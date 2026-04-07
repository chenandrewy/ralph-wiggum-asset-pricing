# Preface

This preface is entirely human-written. Please forgive typos and errors.

- Andrew Chen, April 9, 2026.

## Background

On March 8, 2025, I thought I should write a paper about hedging the singularity.

I was worked up. I was using AI to prove theorems, do lit reviews, and vibe code in my daily life. Six months ago, I had thought each of these things is impossible.

What will happen in the next six years?! Will my entire job be replaced by AI? I had no idea.

But I did know that if there are huge AI disruptions, then tech stocks would most likely benefit. So if anything bad happens to my human capital, I could partially hedge. 

I asked a friend if he would be interested in working on this paper. Unfortunately, he was busy. So, I thought I should use AI to do it.

This project was inspired by [Novy-Marx and Velikov (2025)](https://www.nber.org/papers/w33363)  and [Chris Lu et al. (2024)](https://arxiv.org/abs/2408.06292). These projects use AI to generate massive amounts of academic research. My goal differs in quality over quantity. I want to generate just one paper, but one paper that (I hope) people find is worth reading.

This project was also inspired by [Garleanu, Kogan, and Panageas's (2012)](https://www.sciencedirect.com/science/article/abs/pii/S0304405X12000621) beautiful model of innovation and displacement risk. I read Garleanu et al. back when I was a PhD student and it has stuck with me. 

Last, I drew from [Hadfield-Menell and Hadfield (2018)](https://arxiv.org/abs/1804.04268) and [Bengio (2023)](https://www.journalofdemocracy.org/ai-and-catastrophic-risk/), who apply ideas from economics to AI catastrophe risk. [Hadfield-Menell and Hadfield (2018)](https://arxiv.org/abs/1804.04268) explains the connection between incomplete contracting and AI alignment. [Bengio (2023)](https://www.journalofdemocracy.org/ai-and-catastrophic-risk/) frames AI catastrophe risk in terms of what I would call decision theory and human incentives---though the essay is written in plain English. 

### The First (April 2025) Paper Generation Algo and R&R Decision

The first draft was finished 4 weeks later (April 9, 2025). It comes with a [Github repo](https://github.com/chenandrewy/Prompts-to-Paper), in which `make-many-papers.py` generates many papers as through a series of LLM (mostly Claude Sonnet 3.7) [prompts](https://github.com/chenandrewy/Prompts-to-Paper/blob/master/plan0408-piecewise.yaml)

```
Algo 2025:
----------------
- Prompt 1: draft the model description based on human-specified 
            functional forms and motivations
- Prompt 2: find the price/dividend ratio
- Prompt 3: generate a table based on human-specified
            parameter values
...             
- Prompt 10: write the full paper, based on the prose generated 
            by previous prompts
```
I ran 5 papers, and chose the [best one](https://raw.githubusercontent.com/chenandrewy/Prompts-to-Paper/master/manyout0408-pdf/paper-run05.pdf). The paper included a [human-written appendix](https://github.com/chenandrewy/Prompts-to-Paper/blob/master/README.md), which was just the README.md for the Github repo.

I was told the human-written appendix was the best part. 

Sadly (and hilariously) the paper was rejected from arxiv.org:

> Our moderators determined that your submission does not contain sufficient original or substantive scholarly research and is not of interest to arxiv.

Fortunately, the Critical Finance Review offered me an R&R. 

The editor tasked me with rewriting (re-programming?) the paper from scratch, based on what I've learned about AI since April 2025. The referee provided suggestions for improving the differentiation relative to [Garleanu, Kogan, and Panageas (2012)](https://www.sciencedirect.com/science/article/abs/pii/S0304405X12000621), by incorporating deeper notions of the singularity from [Jones (2024, AERI)](https://www.aeaweb.org/articles?id=10.1257/aeri.20230570). 

The editor also said the human-written appendix was the best part, and should be in the main text. I agreed, and so we have this strange preface. The strangeness is part of why it's good, right?


## The April 2026 Paper Generation Algorithm

To really demonstrate AI displacement, I wanted the AI 

a completely hands-off method. The human should just run the code, and come back to a paper that is good enough, 


The paper is generated using Geoff Huntley's [Ralph Wiggum](https://ghuntley.com/ralph/) method. The idea behind the loop is that Ralph Wiggum (from the Simpsons) may not be the smartest, but he is very persistent.

For my paper, the Ralph loop is:

```
Algo 2026:
----------------
1. Claude Code (Claude Opus 4.6) improves the paper based on
    - `paper-spec.md`: a human-written paper specification
    - Previous test results

2. Run tests:
    - test 01: Factcheck the theory
    - ...
    - test 25: Check that the "AI writes a paper about AI taking my job" 
      rhetoric is subtle
3. If any test fails, go back to 1.
```

Huntley's idea is "human on the loop": the human keeps an eye on what the AI is doing. This is the practical way to deploy AI. 

To really demonstrate AI displacement, my goal is "human as Clockmarker". The human carefully designs the clock. The he/she runs `go-ralph-go.sh`, and comes back later to see a paper that is good enough, and trustworthy enough, that they can put their name on it---at least for now. 

I expect our standards for a "good enough" paper will change soon (see below).

### The Paper Spec

The `paper-spec.md` was critical. I originally wanted to have a very short, perhaps 100 word, paper spec. But the quality of the paper was too low. Or, maybe, my standards increased after seeing what Claude Code can do. 

The ultimate paper spec was 700 words. It doesn't describe any functional forms, but it does lay out the main model's agents, assets, and environment in a few sentences. 

is a [700-word human written outline of the paper](#econ-spec). 


The tests were almost all done by Opus. Appendices [B.2](factcheck-theory) to [B.TBC](element-rhetoric) provide examples of the prompts.

### 25 tests?!

It seems overboard to run 25 tests

TBC
- explain why we need so many tests
- some tests are reusable

## Comparison with the Paper Generation Process in April 9, 2025

## Comparison with UCLA Project


## Limitations of AI in April 9, 2026

TBC
- Much harder to do theory than empirics. Link to UCLA project.
- 



## Lessons about Research

A common response to [Novy-Marx and Velikov (2025)](https://www.nber.org/papers/w33363) is: "people are not ready for this." I heard concerns that peer review will be inundated with AI-generated slop.

Working on this paper gave me a different perspective. It made me think about the fundamentals. I think the fundamentals are the following:

1. Readers want to learn something interesting and true.

2. Readers don't want to check all the math.

3. A system of author reputations makes 1 and 2 possible.

AI-generated papers don't change any of these fundamentals.  Critically, fundamental 3 made me quite wary of putting my name on AI slop. As a result, I don't think AI-generated papers will change much about peer review, at least not the current generation of AI.

## The Future of AI and Economics Research (Speculative)