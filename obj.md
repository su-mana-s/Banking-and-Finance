Statistic methods and metrics(LCR, ratios etc), Modelling(stress testing)
For more Data: 
- https://www.ffiec.gov/npw/Institution/TopHoldings
- https://finance.yahoo.com/quote/BAC/key-statistics


Proc:

1) - See if monthly financial stmts(bs, is) available,  else do quarterly and also find monthly/qtrly macroeconomic data accordingly. 
-------------------------Did - annual--------------------------------
> Then You should be able to calculate current and quick ratios
> https://www.investopedia.com/terms/l/liquidityratios.asp

2) - Scrape Yahoo for f stmts, uslocs for other data n fed:-----------------------Done
- Macroeconomic data under normal and stressed conditions from FED
===========Downloadable csv - need to concat dfs================================

3) - Read: https://www.bis.org/bcbs/publ/d424_hlsummary.pdf (pg 15, wts)


ToDo:
1) Banking stress testing(with macroeconomic vars and basic bank info):
https://www.kaggle.com/code/sherrytp/banking-stress-testing

2) DeepLearning and further references (capital risk and modelling)
https://www.proquest.com/openview/dd4567bfeeadb84a65ea2a956e070708/1?pq-origsite=gscholar&cbl=18750&diss=y

3) Stress Testing for loan portfolios under various macroeconomic conditions
https://github.com/KhalilBelghouat/StressTestingLoanPortfolio/tree/main

4) *** Examine the literature review section 2.4 n the references in it to get a list of attributes/factors for LR and various models to calculate and measure the same(Table 3 esp.)
- Also see Charts(fig 1 etc) and factors(table 5) and section 4.4
https://www.sciencedirect.com/science/article/pii/S2666827023000646

5) https://www.sciencedirect.com/science/article/abs/pii/S1877750317311377

6) Stress testing scenarios on the balance sheet:
- See data section 
https://stanfordeconreview.com/wp-content/uploads/2018/09/diressova-comparative-advantage.pdf


Considerations:
- Dunno how you will mode LCR as it is calculated only over a period of 30 days, with HQLA being that at the beginning of the test period and the tot net cash outflows beinf the one anticipated(as outflows-inflows: deposits(here how do you determine that the term ends in 30 days) - accounts recievable(cash n balanes recievable))
1) See basel 3 para 46, 47 for Level 2 assets inclusion caps for HQLA 

- Level 1: Cash and Cash equivalents, Central Bank reserves(to the extent that the central bank policies allow them to be drawn down in times of stress and no term deposits, see footnotes), marketable securities(see further conditions), 


Ideas:
 
 - If you want to forcast default rates, then you need historic data for loan defaults for each bank per quarter. P.S: Predicting loan default rates is not the same as credit risk assessment. CR A will be more on the lines of risk arising from loans to counterparties and the level of threat that that amount and type of loan poses
 



 Terms:

- Scenario analysis is basically simulated values for various attributes or factors tht are expected to occur according to  the scenario and then predicting the dependent variable and further figuring out how the entire portfolio is affected because of the effect of the dependent vars on the independen var for that scenario
- Here (for liq risk for eg) the marketability of certain assets ie., the increase ir dec in their vals in a given scenario rep by various macroeconomic factors is calc such that the actual effect on the portfolio altogether can be calculated

Objectives:

3. Risk model development: Yahoo fins stmts, US locs fin data per bnk and econometrics must be enough atleast for liq risk modelling
> Interest Rate Risk:
> - Market risk is also along the same lines I think, ie., with macroeconomic analysis of how changes in economic factors might affect he prices of various assets, ie., interest rate risk etc, not necessarily market portfolio risk
> - You cant really model risk or stress test a trading book, but you can risk model for a banking book(so, calc interest rate risk for a banking book, data: banking book, RFRs)
> - If you wanna do credit risk according to (3) and want aggregate loans that have been defaulted on, check NPA information(Non Performing Assets percentage or smthn)
>- Operational Risk:
> - Page 12 in Basel 3 https://www.bis.org/bcbs/publ/d424_hlsummary.pdf
> - Basel 3 documentation for various metrics and calcs: https://www.bis.org/basel_framework/chapter/MAR/20.htm?inforce=20191215&published=20191215

4. > -Stress Testin and Scenario analysis:
> - Macroeconomic factors: historic data and scenario data from FED
> - Balance Sheets from YF
> - Banking Portfolio(banking book) from 3.ie., various financial attributes
> - Also see (6), data for data
> - If you get scenario macroeco data, then for predictive/historic time series modellin you can couple that ad other independent vars acc to the year/quarter and then predict the independent var for bs or irr or whatev
> - https://github.com/jason-ash/pyesg : This looks Good!!
> - ? https://github.com/danielhuppmann/ENGAGE-pyam-tutorial
> - Dunno what this is: https://www.ngfs.net/ngfs-scenarios-portal/data-resources/

- https://stanfordeconreview.com/wp-content/uploads/2018/09/diressova-comparative-advantage.pdf
 - https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2005/stress-tests-of-uk-banks-using-a-var-approach.pdf

5. Ask GPT or gen AI to gen reports if req:')

6. Back Testing from various papers above, benchmark

7. Diff Bussiness Lines(from SEC as a last resort: has comprehensice info for diff loans in diff demographics), geo regions data, if req get from us locs


Theory:

1) Liquidity: https://www.apra.gov.au/apra-explains-liquidity-banking
2) Capital: https://www.apra.gov.au/capital-explained
3) Var based capital requirement