
## The What
Banking Risk Management Framework
- The project executes ratio analyses to determine trading book health concerning liquidity and capital adequacy, audits compliance with various regulatory requirements(BASEL3, CCAR) for mandatory financial reporting and projects financials for scenario analysis following the FRB framework for the Dodd-Frank Stress Assessment
- Scrapes financial information of over 27 major US Banks with 190+ parameters each, for 94 quarters.
----------
## The Project
### The Data:
- We decided to scrape relevant financial data for the project. Our data requirements were threefold – banks’ financial statements, different financial details (like cash run-offs, loans along demographics, foreign holdings etc.) and regulatory stress test scenarios.
- Financial Statements: We scrape the financial statements of various U.S banks from Yahoo finance. While the yFinance library does provide the statements for different tickers, we found that it wasn’t comprehensive in the data it returned- various subheadings from the statements were missing and since they were of import to our analysis, we decided to scrape the statements directly from the website. We use Selenium and Beautiful Soup to achieve the same.  
- Finances: To get a more detailed view of the finances of banks, we also decided to scrape another website – US Bank Locations, which contained information on the assets, liabilities, holdings, deposits, loans, trading books, income and expenses of various U.S Banks. Beautiful Soup is used to achieve this purpose. 
- Scenarios: To get the macro-economic variables like Real GDP, Dow Jones Index, Corporate yield, Unemployment rate etc. the Historic Domestic, Supervisory Baseline and Severely Adverse scenarios are downloaded from the Federal Reserve’s DFAST scenario documents. 

### The Files:
1) The data directory in src contains scripts for scraping Yahoo Finance and the US Locations websites.
2) Find under models
   - risk and compliance which models ratios, checks compliance and performs statistical analysis;
   - scenario-final which fits a regression model to predict finances under scenarios;
   - stress_framework which models the Dodd-Frank Stress Test.
3) Basic visualisation plots with matplotlib for risk ratios and macroeconomic variables

### The Models:
- The various financial models and variables used in practice by individual US banks and their regulatory authorities are examined. We include scripts for computing ratios from their base components which were obtained from the data, analyze the obtained ratios and different parts of the trading book for minimum requirements compliance with regulatory guidelines, based on the size of the bank.
- We also model severely adverse and baseline scenarios using regression for parts of the stress testing framework – which are computed according to the stress tests methodology published by the Federal Reserve [2]. 
1) Risk ratios: The quick ratios and current ratios are calculated from the quick assets, current assets and current liabilities computed from the balance sheets for each bank.
2) Scenarios: Scenarios are analysed for the Dodd Frank Test with the methodology [2] presented by the FRB. The stress framework includes calculation of PPNR (pre provision net revenue) and its components, the various variables that cascaded from it for historic data as baseline. These are then put up as regressands in different models with macro-economic variables stated by DFAST for regressors. The financial modelling approach presented by the DFAST methodology is followed.  

- The regressors included – BBB Corporate Yield, Unemployment Rate, Real GDP Growth, Dow Jones Index and Ten-Year Treasury rate. The calculated components were then again aggregated as directed by the FRB to produce PPNR for stressed scenarios. 
 
- The FRB provides 2 scenarios – supervisory baseline and severely adverse for domestic stress. We modelled the 2024 scenarios, starting predictions from 2025 Quarter 1.
3) Regression: PPNR prediction under supervisory baseline and severely adverse scenarios - DFAST 
```
Pre-Provision Net Revenue = (Net Interest Income) + (Non-Interest Income) – (Non-Interest Expense) + (Additional non-Interest Income) – (Additional non-interest Expense)
```
- Model - Random Forest Regressor 

- Regressors - 
BBB Corporate Yield 
Ten Year Treasury Rate,
Unemployment Rate 
Dow Jones Market Index 
Real GDP Growth 
Dependant Variables  
Net Interest Income 
Non-Interest Income 
Non-Interest Expense 
Additional non-Interest Income 
Additional non-Interest Expense

4) Capital Adequacy, Regulatory Compliance: The methodology for checking regulatory compliance for banks involves calculation of CAR (capital adequacy ratio), Tier 1 Capital Ratio, Tier 1 leverage ratio, Total Capital Ratio. The banks are tested for size largeness as specified by Basel 3 and the applicable tests are done to analyze whether the ratios were compliant with the given standards. 
 
----------
## Results
Liquidity Ratios: We analyzed JP Morgan Chase & Co’s finance profile along different lines. The results are presented here as follows:

<!--
| YTD	       | Quick  |	Current |
| ---------- |:------:| -------:|
| 12/31/2023 | 0.4549 |	0.8262  |
| 12/31/2022 | 0.4480	| 0.8312  |
| 12/31/2021 | 0.4590 |	0.8480  |
| 12/31/2020 | 0.4598 |	0.8584  |
-->
1) Table 1 : Ratios JPMC 2020-23 compiles the quick and current ratios for JPMC over four years. The ratios are calculated on Year-to-Date financial data obtained from the annual balance sheets.
![Ratios JPMC 2020-23](https://github.com/user-attachments/assets/9d2424d1-030e-4ac6-9f6a-e44a948b97ae)![image](https://github.com/user-attachments/assets/211c9e45-6d2d-4c50-b121-787e631e8187)

2) Table 2 : Assets & Liabilities 2020-23 (in billions) compiles the quick assets, current assets and liabilities used to calculate the ratios.
![image](https://github.com/user-attachments/assets/4da1988e-3a72-4935-8f8e-81c3e4df715f)

3) The Dodd Frank test is used to project trading book variables over severely adverse scenarios. <br><br>
Table 3 : Projected Statistics for DFAST 2024 – JPMC represents the regression outputs for the severely adverse scenario for 2024 for variables
projected over 9 quarters.
![image](https://github.com/user-attachments/assets/fee23177-a665-4bcf-8eeb-3b8cb3505ca3)

4) Correlation Matrix for Regressors and Economic Indicators
![image](https://github.com/user-attachments/assets/30e630d9-a340-45be-b69d-0da75292a332)

5) Capital Adequacy Ratio and leverage ratios calculated for the last quarters of the past 4 years. The minimum requirement of CAR under Basel 3 is 8% and 3% for Leverage ratio.
JPMC easily surpasses the basic requirements set for large banks (over $ 100 Billion in assets).
![image](https://github.com/user-attachments/assets/6ee451c7-3e2e-417c-8c83-9865c6d618a1)

### Analysis
An analysis of the results derived through the aforementioned methods from the data at hand.
- Over the course of four years (2020-2023), JPMC has continuously maintained healthy quick and current
ratios of 0.4 and 0.8, respectively, exceeding minimum criteria. These ratios show that the bank has
excellent liquidity positions.
- Banks typically strive for ratios of one or two times, therefore JPMC's assets over liabilities of four and
eight times are especially impressive, indicating little liquidity risk in its trading book. The bank has a
strong financial position overall, as seen by its average ratios and assets.
- The Dodd Frank test predicts trading book variables over scenarios that are extremely unfavourable, and
the forecasts are consistent with what banks might anticipate under such circumstances. Losses match the
FRB's estimated amounts.
- With a minimum Capital Adequacy Ratio (CAR) of 8% and a minimum Leverage Ratio of 3%, JPMC
surpasses Basel 3 criteria, exhibiting robust performance in comparison to the fundamental prerequisites
for major banks with assets exceeding $100 billion.
- JPMC maintains a balanced exposure profile across various credit lines, including Credit cards, C&I,
Auto, Home equity, and Consumer loans, diversifying risk across ten demographics. While heavily
relying on Real Estate Loans and C&I loans, JPMC spreads risk by diversifying across business lines.
- However, this concentration in two demographics increases overall credit risk, especially considering
potential losses from sector failures. This can be validated by the fact that the stock market crash resulting
from a bubble burst and bank runs with banks having overly invested in mortgage loans.
- Also, Although JPMC’s higher principal loans (1 million) are concentrated in the C&I sector, the overall
profile remains adequately diversified. Farmland and Agricultural loans are evenly distributed,
contrasting with the concentration of C&I loans at high or low levels. Overall, JPMC's profile maintains
sufficient diversification, mitigating potential risks.

----------
## References
[1] [Federal Reserve 2024 Supervisory Stress Test Methodology](https://www.federalreserve.gov/publications/files/2024-march-supervisory-stress-testmethodology.pdf) (Accessed 10th April 2024)<br>
[2] [Understanding Liquidity Ratios: Types and Their Importance](https://www.investopedia.com/terms/l/liquidityratios.asp) (Accessed 10th April 2024)<br>
[3] [Basel 3 documentation for various metrics and calculations](https://www.bis.org/basel_framework/chapter/MAR/20.htm?inforce=20191215&published=20191215) (Accessed 10th April 2024)<br>
