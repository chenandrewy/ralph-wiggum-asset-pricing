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

### The First Draft (April 2025) and R&R Decision

The first draft was finished 4 weeks later (April 9, 2025). It comes with a [Github repo](https://github.com/chenandrewy/Prompts-to-Paper), in which `make-many-papers.py` generates many papers through a series of LLM (mostly Claude Sonnet 3.7) [prompts](https://github.com/chenandrewy/Prompts-to-Paper/blob/master/plan0408-piecewise.yaml)

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
I ran 5 papers, and chose the [best one](https://raw.githubusercontent.com/chenandrewy/Prompts-to-Paper/master/manyout0408-pdf/paper-run05.pdf). 

As you can see from this algo, the AIs required substantial hand-holding. They were a pain. You couldn't just ask them to "write down a model of hedging disaster risk" and expect a good result. You really needed to talk them patiently through the process. In a way, it's not *that* different with human co-authors. But as of April 2025, they were in no way a replacement.

The first draft included a [human-written appendix](https://github.com/chenandrewy/Prompts-to-Paper/blob/master/README.md), which was just the README.md for the Github repo. I was told this was the best part. 

Sadly (hilariously), the paper was rejected from arxiv.org:

> Our moderators determined that your submission does not contain sufficient original or substantive scholarly research and is not of interest to arxiv.

Fortunately, the Critical Finance Review offered me an R&R. 

The editor tasked me with rewriting (re-programming?) the paper from scratch, based on what I've learned about AI since April 2025. The referee provided helpful suggestions for improving the differentiation relative to [Garleanu, Kogan, and Panageas (2012)](https://www.sciencedirect.com/science/article/abs/pii/S0304405X12000621), by incorporating deeper notions of the singularity from [Jones (2024, AERI)](https://www.aeaweb.org/articles?id=10.1257/aeri.20230570). 

The editor also said the human-written appendix was the best part, and should be in the main text. I agreed, hence this long and strange preface. The strangeness is good...  ...right?


## The April 2026 Paper Generation Algorithm

The biggest change in AI relative to April 2025 is, of course, agents. Anthropic's Claude Code and OpenAI's Codex don't just provide responses to prompts, they are fluent with navigating, writing, and executing in computing environments. They also persist through challenging tasks. 

These agents allow for a *real* demonstration of AI displacement. They really looked like they could take my job. 

### The Ralph Loop

The new algo employs agents following Geoff Huntley's [Ralph Wiggum](https://ghuntley.com/ralph/) loop. The idea behind the Ralph loop is that Ralph Wiggum (from [the Simpsons](https://en.wikipedia.org/wiki/The_Simpsons)) may not be the smartest, but he doesn't mind doing the same thing over, and over, and over again.

For my paper, the Ralph loop is:

```

Algo 2026:
----------------
1. Author Prompt: improve the paper and code based on
    - paper-spec.md: a human-written paper specification
    - other documentation (e.g. the CFR referee report)
    - Previous test results

2. Test Prompts: evaluate the improved paper and code:
    - test 01:  Factcheck the theory
    - ...
    - test 25:  Check that the "AI writes a paper about AI taking my job" 
                rhetoric is subtle

3. If any test fails, go back to 1.
```
Like Ralph Wiggum, Claude doesn't seem to mind working on this, day and night. 

Huntley's idea is actually "human on the loop": the humans keeps an eye on what the AIs are doing, and they update the specs and tests (perhaps turning off or on selected tests) to steer the ship.

But to demonstrate AI displacement, my goal is "human as Clockmarker". The humans carefully design the clock. When finished designing, they run `go-ralph-go.sh`, and come back later to see a paper that is good enough, and trustworthy enough, that they can put their name on it---at least for now. 

I expect our standards for a "good enough" paper will change (see below).

### Agent Selection

I used Claude Code + Opus throughout the algo, as it is the best at writing, and I wanted to get this done with a single $100/month subscription. That was a mistake. 

I ended up with two $200/month Claude Code subscriptions, and even that struggled to crunch through the 25 test suite. 

With hindsight, I would have aimed for:

1. One $100/month Claude Code sub for the writing
2. One $200/month ChatGPT sub for testing 

Because while Claude Code Opus wins on creativity and fun, Codex with gpt-5.4 is so much more reliable, logical, and efficient. Peter Steinberger (creator of OpenClaw) [put it well](https://lexfridman.com/peter-steinberger-transcript/)

> In general, it’s almost like Opus was… Is a little bit too American. And I shouldn’t… Maybe that’s a bad analogy.

As an American, I think it's a great analogy.

### 25 Tests?!

I didn't want to have 25 tests! I was hoping for four: for one for theory, for code, for writing, and for visuals.

Arriving at 25 tests was empirical. I would run the Ralph loop overnight, read the paper output in the morning, and then get frustrated by the result. This would lead to test updates and new tests.

The many tests helped a lot. Like [Ralph Wiggum](https://en.wikipedia.org/wiki/Ralph_Wiggum), Claude is easily distracted, and breaking up the tests into smaller tasks helped Claude focus. Actually, since many of the tests used subagents (e.g. N subagents would test the N sections of the paper), you could say there were more like 40 or 50 tests.

### 20 Reusable, General-Purpose Tests

The beauty of making tests is that they can be applied to future papers. Of course we want our papers to be fact checked:

- `factcheck-theory`
- `factcheck-narrative`
- `factcheck-code`
- `factcheck-lit`

These are intuitive. You gotta check the theory. Gotta check that the narrative matches the theory. And of course you gotta check the code and the citations for accuracy.

The other factchecks were not obvious, a priori:

- `factcheck-anaphora`
- `factcheck-exhibits`
- `factcheck-freely`
- `factcheck-bysection`

I had never heard of an "anaphora" before encountering this nightmarish passage in one of the Ralph loop runs:

> Part (iii) [of Proposition 2] captures the interaction: existential risk *attenuates* the sensitivity of AI valuations to singularity beliefs.

> If the singularity also accelerates growth Jones (2024), AI owners' resources could grow large enough to make the cost of compensating the household negligible---the friction becomes self-resolving. Section 4 quantifies this attenuation.

"this attenuation" could refer either to the friction or to valuations. Technically, Section 4 addressed "this attenuation", but only if it referred to valuations. No other test was able to catch this error, aside `factcheck-anaphora`, which is dedicated to checking "anaphora resolution problems".

`factcheck-freely` is also interesting. This test just asks Claude to "Review the paper. Look for flaws." Consistent with [Tam et al. (2024)](https://arxiv.org/abs/2408.02442), letting the AI speak freely often led to higher quality results. Hamstringing Claude with process and reporting requirements seemed to distract it, sometimes preventing insight.

Then there are the quality tests. We generally want econmoic theory to be clear and concise (no deadweight)

- `theory-clarity`
- `theory-deadweight`

And we want good visuals too:

- `visual-figures`
- `visual-figures-image-only`
- `visual-pages`

`visual-figures` judges the figures together with the surrounding text. `visual-figures-image-only` uses only the figure images. A human might do both at the same time naturally, but Opus struggled with this.

And, of course, we want good writing:

- `writing-econ-messaging`
- `writing-flow`
- `writing-intro-payoff`
- `writing-intuition`

Last, we want the paper to stick to the spec: 

- `spec-paper`
- `spec-economic`
- `spec-scope`

There was both a paper spec (more on this below), as well as an economic background spec (for general asset pricing and "singularity" concepts). I also found it helped to require that Claude stay within the scope of the paper spec, in a specialized test. 

### Specialized Tests (for now)

All of the previous tests will be useful beyond my paper. I really do see researchers using Ralph loops regularly, very soon. I believe we'll be teaching it to grad students. 

But a proper Ralph loop is human *on* the loop. The humans should get their hands dirty for the key elements. 

For my curious goal of human as Clockmaker, I required tests to automate *everything*, including compelling figures:

- `element-opening-fig`
- `element-transfers-fig`

Right now, Claude makes beautiful webapp front ends. But it does not do great academic "money figures"---not naturally. But it's just a matter of time. Someone will make a generalizable tool for this soon.

I also wanted a specific style of short lit review:

- `element-lit-review`

Really, the human should be on the loop here. I don't see that ever changing. Scholars are supposed to know the literature.

For my paper, I needed to ensure that the "AI writing a paper about AI taking my job" rhetoric is carefully done:

- `element-rhetoric-meta`

Claude would occasionaly start the abstract *and* introduction with "This paper was written by AI". The writing evaluations (above) would all say "this is great! So engaging!" So `element-rhetoric-meta` informs poor Claude that, unfortunately, humans strongly prefer to read human-written text (even if it has typos and errors, right?). 

Most importantly, the human should get hands on with citing the most closely related papers. But in my case, I needed the AI to take care of it, leading to:

- `element-gkp-cites`

which instructs the AI to read [Garleanu, Kogan, and Panageas's (2012)](https://www.sciencedirect.com/science/article/abs/pii/S0304405X12000621), read the CFR referee report, and accurately represent these ideas, while also being sensitive, gracious, and not-awkward in its citations. Right now, humans scholars are much better at citing graciously. Naturally, all our study and practice of citing people graciously is hidden from the training data... 

...

...I guess that's our comparative advantage?

### The Paper Spec

The [paper-spec](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/main/spec/paper-spec.md) was critical. I originally wanted to have a very short, perhaps 100 word, paper spec. But the quality of the paper was too low. Or, maybe, my standards increased after seeing what Claude Code can do. 

The ultimate paper spec was 700 words. It's basically the paper in bullet points. For example, Extension 1 is described as:
1. Extension 1: Market incompleteness is closely related to efficient development of AI. 
    1. There is a chance of a *positive* singularity, in which the household also benefits. The positive singularity is the most likely outcome. 
    2. AI development is socially efficient in the sense that the positive singularity outweighs the negative singularity in a welfare calculation.
    3. The household can block ("veto") development of AI at a significant cost. The cost is significant because it requires intense government intervention and associated deadweight costs. 
    4. There is a base case, in which the household vetoes development of AI, due to the disaster risk and risk aversion. 
    5. But if markets are complete, the household would never veto.

This extension responds to the CFR referee's advise to connect more deeply with the singularity concept. 

As you can see, the extension is rather hard coded. I had hoped that the AIs could just read the referee report and come up with a sketch like this. But unfortunately (or fortunately), I had to go in there and hand-design the extensions.

You should be able to clone this [Github repo](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/main/spec/paper-spec.md), change the spec, turn off the specialized `element-` tests, run `go-ralph-go.sh`, and return to a well-written, error-free paper.

## Comparison with the Paper Generation Process in April 9, 2025

In April 2025, the paper generation algo was pure gimmick. It would have made so much more sense for me to use LLMs as a souped-up Google query, and write the paper more-or-less the old fashioned way. 

In 12 months later, the algo is mostly practical. The only impractical element is the human-as-Clockmaker design. Following Huntley's "human on the loop" method would be more practical, but inspecting the paper, updating the spec, and then letting the Ralph loop do its job is absolutely a real way to produce research. 

The human on the loop research is quite satisfying, in a way. I find the spec to be the most fun part. There were several nights where I was quite excited to tell my 


## AI is Better at Empirical Work

I used a Ralph loop to write a (straightforward) empirical paper for my [submission to the UCLA HumanxAI competition](chenandrewy/HumanxAI-ChenAY: Repurposed from FinRep).  

It was much easier. I rarely woke to find frustrating errors. I never spent all day designing a test. The AI did a good job generating ideas for empirical tests. 

Most notably, I was able to use an Opus-generated open ended [referee review](HumanxAI-ChenAY/ralph/reviews/top3-referee.py at main · chenandrewy/HumanxAI-ChenAY) as part of the Ralph loop. The referee would offer helpful new empirical tests, which the author agent would implement nicely. 

The open ended referee made a mess in this theory paper. It would lead to idle speculation and stray loose ends in the modeling. I ultimately turned off this feature. 

It’s kind of intuitive that theory is "harder." But it’s not obvious this applies to AI. 

My interpretation is that good theory is harder to define. I not only had to turn off the open-ended referee, I also had to include a special test for limiting the scope, as well as targeted [theory-clarity](ralph-wiggum-asset-pricing/tests/theory-clarity.py at main · chenandrewy/ralph-wiggum-asset-pricing) and [theory-deadweight](ralph-wiggum-asset-pricing/tests/theory-clarity.py at main · chenandrewy/ralph-wiggum-asset-pricing) tests. 


## Lessons about Research

A common response to Novy-Marx and Velikov (2025) was: "people are not ready for this." I heard concerns that peer review will be inundated with AI-generated slop. 

Working on this paper gave me a different perspective. It made me think about the fundamentals. I think the fundamentals are the following:

1. Readers want to learn something interesting and true.
2. Readers don't want to check all the math.
3. A system of author reputations makes 1 and 2 possible.

AI-generated papers don't change any of these fundamentals. Critically, fundamental 3 made me quite wary of putting my name on AI slop. 
As a result, I made a [prediction](https://github.com/chenandrewy/Prompts-to-Paper/edit/master/README.md#lessons-about-research) in the April 2025 draft:
> I don't think AI-generated papers will change much about peer review, at least not the current generation of AI.
So far, this prediction has been born out. The JF and RFS journal statistics pages show no sign of an increase in submissions. 

| Sub Year	| JF 	| RFS* |
| ---       | ---        | ---  |
|2023 		| 1,142 	 | 1534 |
|2024 		|  937		 | 1544 |
|2025 		|  1,100 (p) | 1474 |

where 2025 is projected, and * indicates RFS counts end in May (2025 means May 8, 2024 to May 8, 2025).
There could be an “AI investment” effect in this table. Perhaps many scholars, like myself, took time off producing papers in favor of investing in AI tools.
But I personally found the AI developments also led me to invest *more* in any individual paper. Now I can do so much! I can’t settle for the kind of work I did way back in 2024, or even 2025! I have a reputation to maintain. 

## Limitations of Current AI (April 9, 2026)

12 months ago, I said AI was (limited)[https://github.com/chenandrewy/Prompts-to-Paper/blob/master/README.md#limitations-of-the-current-ai-april-9-2025] in that 

1. AI economic modeling was unsatsifying
2. AI empirical and numerical work required a plethora of technical challenges
3. AI lit reviews over-interpreted or mis-cited papers. 

I also speculated that 2024-style economic analysis will be "on tap" at some point inspired by (Josh Gans' essay on (p)research)[https://joshuagans.substack.com/p/what-will-ai-do-to-presearch?triedRedirect=true]. 

All three limitations are gone now. And we're almost at the point where 2024-style economics is "on tap". You should be able to clone my repo (or my [Human x AI submission](https://github.com/chenandrewy/HumanxAI-ChenAY/commits/main/)), modify the spec and tests, run `go-ralph-go.sh`, and come back to a completed paper, with satisfying economic modeling, empirical work, and lit reviews. The quality is probably high enough to have publishable in 2024. But I think it will get there soon.





## The Future of AI and Economics Research


That point is almost here. 

"Economics on tap" could be a disaster for the economics labor market (could be). It certainly *will* be an extremely cheap substitute for at least some economists' labor. I suppose the questions is whether that will result in a strong substitution away from labor.

The optimistic argument is that AI also *complements* economists' labor. Perhaps, the number of economists will remain the same, but our research output increases in terms of both quantity and quality. 

But there are reasons why total research output is limited. Two key factors in academic publishing are attention and reputation ([Klamer and van Dalen 2001, J of Economic Methodology](https://repub.eur.nl/pub/6875/2001-0221.pdf)). Readers can only pay attention to so many scholars.  Put another way, I might augment the fundamentals of economics research with a sub-bullet:

1. Readers want to learn something interesting and true.
    1. **What bleeding edge experts are studying is interesting**

By definition, there are a limited number of experts at the bleeding edge. These experts, in turn, can only pay attention to so many projects.

I'm not saying that I *expect* a disaster for the economics labor market.  But even if it's highly unlikely, it's still a scenario that economists should consider. 

