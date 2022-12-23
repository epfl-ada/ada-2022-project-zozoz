<script>
import { base } from "$app/paths";
</script>

<section class="justify">

## Conclusion

To sum up, the search for causation behind the non-success of a movie seems like a dive into an infinite abyss of possibility and eternal questions. We still succeeded in showing that features such as the director, genre and budget can be associated with the final quality of a movie. Nevertheless, we should interpret our results with caution. First, we did not perform sensitivity analysis for our observational studies, so the signal for causation may be low. 

![Rating Distribution]({base}/plots/badmovie.png)

Furthermore, the different models' overall $$r^2$$ of 0.163 and other fit metrics are low. Thus our set of features cannot explain a large part of the variance in the data. It was expected based on the small subset of metadata we had. A movie cannot be reduced to the length of its title or the number of actors and actresses who play in it. It is time for us to put on our astronaut suits again, the exploration of the bad movie world awaits.

## Side nerdy note

If you are interested in the methods and the details of our analysis and its implementation, we encourage you to look at our <a href="https://github.com/epfl-ada/ada-2022-project-zozoz">GitHub</a>. But for the most hurried of you, the observational study pipeline was done using propensity score computation with logistic regression and matching with KNN. Then to assess if the treatment was significant to decide if a movie was good or bad, we used our old friend: logistic regression!



<!-- ```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         average_rating   R-squared:                       0.163
Model:                            OLS   Adj. R-squared:                  0.162
Method:                 Least Squares   F-statistic:                     223.4
Date:                Fri, 23 Dec 2022   Prob (F-statistic):               0.00
Time:                        17:42:34   Log-Likelihood:                -26013.
No. Observations:               19572   AIC:                         5.206e+04
Df Residuals:                   19554   BIC:                         5.220e+04
Df Model:                          17                                         
Covariance Type:            nonrobust  
==============================================================================
Omnibus:                     2373.816   Durbin-Watson:                   1.995
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             4095.371
Skew:                          -0.825   Prob(JB):                         0.00
Kurtosis:                       4.517   Cond. No.                         158.
==============================================================================

``` -->





</section>

<style>
pre {
   display: flex;
   justify-content: center;
}
</style>