
*For Stress Testing and Sccenario Analysis*
A very high-level analysis of how bank variables are affected by economic variables
- I am thinking that scenario testing is basically just time series forcasting
- Get macroeco vars - annual/quarterly?
- map them to the data - ie., for 1 bank, say u r considering balance-sheet- or the uslocs data, then if you map the years in the data to be analysed(dates are cols in base, concat scenarios and base such that dependent variables are identified)
- I am thinking that dependent vars will be many- basically everything you need to analyse changes/effect of economic scenarios for
- Then use basic historic prediction for val prediction(regression? for basic anly)

> I am gonna skip shocks for now- it seems you give them as percentages and directly calculate effects and analyse them - I will look into implementing them later
> - That means I am skipping the Severely adverse market shocks segment in the dodd frank test for now

That leaves us with Historic domestic- eco vars till 2023; Historic International(which I am gonna skip for now cos idk what it means, it has euro, uk and japan vars); Supervisory baseline domestic( I am thinking these are prediction scenarios, so am gonna keep them as such - esp cos they go up until 2027); gonna skip international in this too(but if i manage to figure out how to use historic, it will be lit); Supervisory severly adverse domestic(has the same pred data, but probably for an apocalyptic scenario lol) -> This leaves us with 2 answer sets

>They also have data defs - how convenient(not.)

Now the question arises - 1 answer set is going to contain a lot of predictions for different variables: lets say we take balance sheet as the base dat; then we have predictions or total assets and total liabilities(and a lot more) for each bank. (This would mean in the analysis-interim dataset, concat needed with historic data for each bank for each variable, by year - too many dimensions:===); Now how am I supposed to let users query this? Thats a lot of data - I can pick and choose vars for my analysis/report, but can I let people query visualisations? I can write a prog for this, but is there a tool? an easier way?

**Alternative to FRB eco vars - FRED : https://fred.stlouisfed.org/docs/api/fred/**

<h3> Risk </h3>
*For Market Risk*
 - If, say I want to analyse trading book exposure risk - then do I just scenario analyse for the specific subsections of the trading book? Like - debt securities, equities etc? and perhaps convert them to a ratio/percentage to give an approximation for risk

 - I am thinking, do statistical modelling for liquidity risk
 
 >Or, its ulta- trading book exposure has multiple varieties of risk- including market risk and liquidity risk and credit risk

 - If you want to analyse trading portfolio market risk, you need time_ti_liquidate transactions along with the holdings portfolio

 >  Worst case, get holdings portfolio and do VaR and corr analysis to get overall risk, diversification with no time bounds

 *For Market Risk*
 - Instead of transaction level risk(worst case, can do), try looking for credit portfolio level risk(systematic/intrinsic and concentration risk)
  - Apparently this risk is indirectly proportional to diversification
  - A diverse portfolio here would be in terms of markets, demographies, geographies, industries and borrowers for the loans
  > So, you can just collect various demographic data(ip for obj 7) and analyse diversification, which i am thinking is basically corr analysis and how many(and at how much magnitude) of the factors are negatively and positively correlated etc. I think this is concentration risk, not sure.
  - But should be able to calc systematic also with the data available
  
 *For Backtesting*
 - Split the historic data into 25-75; so that over and above predicting stuff on data we have no test base for, we can just use this as a validation set to measure performance
 > Throw in a bunch of performance metrics for the models