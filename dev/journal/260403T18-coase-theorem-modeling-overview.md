# Coase Theorem: How Economists Have Formally Modeled It
**Date:** 2026-04-03, 6:00 PM ET

## Motivation
Background research on how economists have formalized the Coase theorem since Coase (1960). Interested in bargaining models, key modeling elements, highly cited papers, and how thinking has evolved.

## Origins

- **Coase (1960), "The Problem of Social Cost," JLE** — entirely verbal, no equations. Argued that with well-defined property rights and zero transaction costs, parties bargain to efficiency regardless of initial rights assignment. But his *actual* point was the converse: transaction costs are never zero, so institutions matter.
- **Stigler (1966), *The Theory of Price* (3rd ed.)** — coined the term "Coase theorem." Became the canonical formulation, but Coase disliked it. As Medema noted: not a theorem, and not really Coase's message.

## Two Versions

1. **Efficiency version**: Bargaining reaches Pareto-efficient outcome regardless of initial rights.
2. **Invariance version** (stronger): Final allocation is the *same* regardless of initial rights. Hurwicz (1995, *Japan and the World Economy*) proved quasi-linear utility is necessary and sufficient for invariance.

## Bargaining Formalizations

- **Nash bargaining (1950)**: Two parties split surplus. Efficient outcome, but division depends on threat points (initial rights). Confirms efficiency, not invariance.
- **Rubinstein (1982, *Econometrica*)**: Alternating-offers, complete info — unique SPE, immediate agreement, efficient. Noncooperative foundation for Coase in bilateral complete-info case. Breaks down with multiple parties.
- **Coase conjecture / durable goods**: Coase (1972) conjectured monopolist converges to MC pricing. Gul, Sonnenschein, and Wilson (1986, *JET*) proved it. Related but distinct from Coase theorem.

## Major Formal Challenges

### Incomplete Information (most devastating line of attack)

- **Myerson and Satterthwaite (1983, *JET*)**: With private valuations from overlapping distributions, no mechanism can simultaneously achieve IR + budget balance + IC + efficiency. Coase theorem fails generically under incomplete info.
- **Chatterjee and Samuelson (1983, *Operations Research*)**: Double auction, two-sided private info — too little trading in equilibrium.
- **Farrell (1987, *JEP*)**: Early influential discussion of private info undermining the theorem.
- **Cramton, Gibbons, and Klemperer (1987, *Econometrica*)**: Partnership dissolution. Efficient dissolution possible only if no single partner owns too large a share. Initial property rights determine whether efficient bargaining is feasible.
- **McKelvey and Page (2002, *JET*)**: Most efficient Bayesian mechanism exhibits *status quo bias* — expected allocation biased toward initial endowment. Directly contradicts invariance.

### Multiple Parties

- **Aivazian and Callen (1981, *JLE*)**: With 3+ parties, cooperative game can have an empty core — no stable allocation. Endless recontracting.
- **Dixit and Olson (2000, *JPubE*)**: Voluntary participation + public goods → free-riding grows with number of parties. Coase essentially inapplicable to large-group externalities.

### Transaction Costs

- **Williamson (1979, 1985)**: Bounded rationality, opportunism, asset specificity, hold-up. The whole TCE program.
- **Anderlini and Felli (2006, *EJ*)**: Ex ante transaction costs create hold-up. Negotiating over costs generates new costs — infinite regress. No Coasian solution available.

### Political Economy

- **Acemoglu (2003, *JCE*)**: Political Coase theorem fails because the state can't credibly commit — the enforcer is a party to the bargain.

## Law and Economics

- **Calabresi and Melamed (1972, *HLR*)**: Low transaction costs → property rules (voluntary exchange); high → liability rules (forced exchange at court-determined price).

## Empirical / Experimental

- **Ellickson (1991, *Order Without Law*)**: Shasta County ranchers used informal norms, not legal rules. Consistent with Coasian spirit but norms didn't track legal entitlements.
- **McKelvey and Page (2000, *Experimental Economics*)**: Much more inefficiency under private info. Rejected Coase in favor of M-S predictions.

## Evolution of the Profession's View

| Decade | Development |
|---|---|
| 1960s | Initial resistance → Stigler's canonization |
| 1970s | Calabresi-Melamed for law; Williamson builds TCE |
| 1980s | Formal challenges: M-S, incomplete info, empty core |
| 1990s | Hurwicz pins down quasi-linearity; Coase Nobel (1991); profession recognizes his actual message |
| 2000s | Political Coase fails (Acemoglu); status quo bias; infinite regress |
| 2010s–20s | Consensus: useful benchmark like Modigliani-Miller, valued because assumptions are violated |

## Definitive Survey

**Medema (2020), "The Coase Theorem at Sixty," *JEL*** — 84-page comprehensive survey. The one paper to read.

## Bottom Line

The profession now treats the Coase theorem like Modigliani-Miller — a benchmark whose value lies in clarifying which frictions matter, not in describing reality. Medema (2020) argues the theorem's lasting contribution is as a *diagnostic tool*: if you observe persistent inefficiency from an externality, the theorem says point to the specific friction that prevents bargaining. Is it transaction costs? Information asymmetry? Too many parties? Commitment problems?

## What Stands Out

1. **The theorem's biggest legacy may be methodological, not substantive.** It redirected economists to ask *why* institutions exist — why firms, why courts, why liability rules — rather than just assuming a frictionless world. Williamson's entire TCE program flows from this.

2. **Incomplete information is arguably the most important formal challenge.** Myerson-Satterthwaite shows that even with just two parties and zero transaction costs, private information alone kills efficiency. This is sharper than "transaction costs are positive" — it says even if you could costlessly bring parties to the table, bargaining still fails when valuations are private. A deep structural impossibility, not just a practical difficulty.

3. **The invariance version is basically dead.** Almost nobody defends it. Wealth effects, information asymmetries, status quo bias all point the same direction: initial property rights assignments *do* affect final allocations. The efficiency version survives only as a limiting case under very strong assumptions (complete info, two parties, no wealth effects).

4. **For any externality/friction paper**, the Coase theorem is the "why don't private parties just bargain away the problem?" question you need to address. The literature's answer: because information, because many parties, because commitment, because transaction costs.

## Strategy for Incorporating Coase into the Paper

### The Problem with a Naive Coase Citation

The Coase theorem is about allocation of real resources. Our paper is about financial markets and asset pricing. A loose Coase reference (the current line 27 of the paper spec) is hand-wavy and invites referee pushback. We either need to make the connection concrete or drop it.

### The Household Veto Idea

We can make Coase genuinely relevant by giving the household veto power over AI deployment. This is a participation constraint: the household can block AI development unless its continuation utility exceeds an outside option (a no-AI world with lower but safer consumption). This is realistic — if households collectively hate the data centers and displacement, they can find ways to stop it (regulation, revolution, political action).

### Proposed Formulation

"The household can block AI deployment unless its continuation utility exceeds an outside option. Because private compensation is limited by contracting frictions, we model transfers through a government program that incurs deadweight costs."

### Implementation Steps

1. **Define a no-AI outside option.** A consumption path with no AI investment — lower growth, no displacement risk, no extinction risk, no singularity upside.
2. **Add a household participation constraint.** The household allows AI investment iff $E[U(\text{continue})] \geq E[U(\text{veto})]$. One inequality.
3. **Show that without compensation the constraint may bind.** Under incomplete markets, the household bears displacement risk but gets none of the AI surplus. The constraint binds, AI investment stops, singularity probability goes to zero. Inefficient outcome.
4. **Introduce the transfer scheme with deadweight cost.** Already in the spec (5.c). The government program shifts surplus from AI owners to households.
5. **Show that when singularity surplus is large enough, compensation can satisfy participation despite deadweight costs.** Already in the spec (5.c.i). The singularity's infinite output overcomes even huge deadweight costs.

### Why This Works

- **Coase connection is now concrete.** The transfer is the Coasian side payment. Contracting frictions prevent it from arising privately. The government program is the institutional fix (Calabresi-Melamed: when transaction costs are too high for property-rule bargaining, use a liability rule / institutional mechanism).
- **Deepens the GKP connection.** The participation constraint gives a formal reason why displacement risk matters for investment levels, not just prices.
- **Stays minimal.** One inequality added to the extension. No game theory, no bargaining protocol. Just a participation constraint.
- **Keeps it in the extension.** The core model is untouched. This is "exploring wild singularity ideas" per the referee's request.
- **Greenwald-Stiglitz (1986) as the intellectual anchor.** Frictions (incomplete markets, imperfect information) → constrained Pareto inefficiency → welfare improvements are blocked. The veto makes this concrete: the blocked improvement is AI investment itself.
