<script>
import { base } from "$app/paths";
</script>

<section class="justify">

## Budget

The 7th art always had a duality, two faces of the same coin. Cinema was initially designed as an experience that aimed to bluff the audience, something they could remember. Of course, with the medium's depth, cinema's artistic side quickly rose and is now an undeniable part of its DNA. Nowadays, we can still easily find the original search for the wow effect with the giant blockbusters distributed worldwide. This race to further, more robust and higher led to budgets and box office revenues reaching levels that even the [Lumière brothers](https://blog.scienceandmediamuseum.org.uk/the-lumiere-brothers-pioneers-of-cinema-and-colour-photography/) could not have ever dreamt. 

But where money is found, problems and tension are usually not so far. We often hear that blockbusters are, in fact, of relatively poor cinematographic quality. This creates a deep boundary between two communities that often seem disjoint: the blockbuster and the author cinema. But is the budget responsible for the final appreciation of the film? This was the last question we wanted to investigate in our analysis.

![Budget Boxplot]({base}/plots/budget_histplot.png)

At first glance of the data, there was no significant difference between the budget of bad and good movies, as shown in the histogram. But it did not mean that we could not find something valuable.


To use our beloved observational study pipeline, we first split the movies into two subcategories: high- and low-budget movies. The threshold was set up according to the median of all budgets to  25'000'000$. Then we investigate whether the budget had a causal effect on making a film terrible. Interestingly, we found a significant coefficient associated with the budget, and it was negative. Thus, movies with high budgets were more prone to good films than bad ones. This could be explained by the type of users rating movies on IMDB, favouring movies with features that need a lot of money. It could also be due to the fact that with more money, you can produce better FX, recruit great actors and reach the expectations of more elaborated plots.

</section>

