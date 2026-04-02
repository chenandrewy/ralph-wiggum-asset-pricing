# Personal Notes on Jones (retrieved from dev/tmp/)
**Date:** 2026-04-01
**Note:** This is an old file retrieved from `dev/tmp/my-notes-on-Jones.md` and saved to the journal for archival.

---

# Simple Model
If we invest in AI for time of length $T$ , it raises consumption at rate $g$
$$
c = e^{gT}
$$
But then the prob humanity survives to time $T$ decays with $\delta$: 
$$
S(T) = e^{-\delta T}
$$
The planner then chooses $T$ to maximize
$$
EU = S(T)u(c) = e^{-\delta T} u(e^{gT})
$$

This is a bit strange to me, since it doesn't seem to treat extinction as anything special. Extinction here is simply zero utility. But maybe one can just scale the utility function appropriately.

The FOC implies AI is used as long as 
$$
\delta v(c) \le g
$$
where
$$
v(c) \equiv \frac{u(c)}{u'(c)c}
$$

where the LHS is the cost of losing life. Life is valued at $v(c)$ per period. 

Simplifiying, the optimal $T^*$ satisfies
$$
v(c^*) = v(e^{gT^*}) = \frac{g}{\delta}
$$
This can also be thought of in terms of the optimal $c^*$ at which one should stop investing. This framing is helpful, since it shows how optimal AI investment depends on the utility function, embedded in $v()$ . 

Since VSL is $10m for a 40-year old, who might live 40 years, and consuption is around $40k per person, Jones says $v(c_{us,today})\approx10m/40/40k=6$: a year of life is worth six times per capita consumption. 


Jones focuses on 
$$
u(c) = \bar{u} + \frac{c^{1-\gamma}}{1-\gamma}
$$
And notes
1. if $\gamma>1$, then $v(c)$ is increasing
2. $\bar{u}$ controls the utility when dead, and it must be positive, otherwise death is preferred
I guess the more important thing is that $\gamma$ really matters.

## Calibration
With log utility and some baseline parameters, we should run AI until consumption increases by a factor of 55! log utility means we don't care about existential risk, according to this calibration. The survival odds are only 0.67 for this model.

But if we double the exiistential risk from $\delta = 1\%$ to $\delta = 2\%$, we should stop doing AI research right now. We already have enough consumption.

Then of course it also depends on whether we allow for heterogeneity. Poor people are much more willing to invest in AI, according to the model.

## Discussion

 jones also discusses how there are philosophical concerns with this framing. For example, the end of all human life certainly seems to be different than simply aggregating the loss of many individual lives. Also, the modeling ignores the loss of future people who would not get to live. So it's interesting because while the paper makes a valiant attempt to model an important thing, an important question. There are fundamental ways in which this modeling cannot possibly be satisfactory. 

# Richer model, with singularity


 the richer model allows for infinite consumption, reduction in mortality and putting weight on future generations.

 I think this is where the bounded utility matters because with infinite utility you can't really make any mathematical statements that make much sense. But because gamma is greater than 1, utility is bounded and even if consumption is infinite, utility is still finite. 

 in this singularity, social welfare becomes:
 $$
  W_{sing} = N_0 * ū / ((ρ + m_{ai})(ρ_s - b)).
 $$

 with that, you can solve for the delta that makes the planner indifferent to investing in AI. 
# Relation to my paper

Of course, this is very different than my paper where in the singularity the representative household suffers while the AI owners gain dramatically.

 that's what we would have here is that in the singularity, the AI owner's consumption increases dramatically and perhaps even becomes infinite. 
 
 I feel like it's implicit in my paper, or at least in the framing that I was thinking, that marginal utility can become infinite. That is people can always suffer more. 

The closest tie I can see to my paper is that I should consider what happens if the AI owners have infinite consumption. In that case, it seems obviously optimal to share the consumption with the rep houshold. Even if there are frictions preventing that sharing, consumption is infinite, and can be spent to overcome the friction.

The other way to relate to Jones is to say in passing, that Jones does not consider that a portion of the population can suffer greatly from the singularity. one can enrich jones with such modeling but i think the result is very different from my hedging paper, at least that's my initial feeling.

It might be good to respond to the ref by including the infinite consumption overcoming incomplete markets idea, and then also adding Korinek and Suh. I think the paper is better positioned as a connection between GKP and Korinek and Suh.
