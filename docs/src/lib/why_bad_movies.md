<script>
import { base } from "$app/paths";
</script>

<section class="justify">

## What is a bad movie?

But first, let’s define the landscape a bit. The main question that will drive the analysis is what we consider a good or a bad movie. And as we know taste is subjective. So it's subjective what constitutes a "bad" movie, as different people have different tastes and opinions about films. However there objective numbers like ratings and revenue, which quantify how successful, popular and beloved a movie is. We can use these measures as a proxy to select movies for the further analysis. The revenue would be a bad idea, since it would just tell us how popular a movie is. Think here of the last big Marvel Studios movie. Alternatively we use the IMDb rating to determine how good a movie is.

![Distribution of Average Ratings in our IMDb Dataset]({base}/plots/ratings_distribution.png)

Using the ratings from IMDb users, we set up two thresholds to perform the classification. We feel that a movie is bad if its rating is below 6.5 and good if it is above 7.5. These thresholds have been set empirically using a small poll around us ($$n$$=10, they are pretty picky voters 🌚). For the sake of simplicity, we will use the above framework through our different analyses, but these boundaries are arbitrary and unrealistic. Our appreciation of a movie is part of a continuum, not a simple binary value.
 Another point worth mentioning is the structure of the data and its inherent bias. We base our results on ratings from a specific part of the population, the users of IMDb. Their opinion may not reflect what a random sample of people would feel during a movie screening. Furthermore, we ran our analysis for decades from 1920 to 2020, but the ratings collected come mainly from the past ten years. Thus, a movie could be perceived as a great movie today, but most of the audience rejected it at the moment of its release. Therefore we should be conscient of the final scope of our results and that we may not be able to generalize to the entire population.

 _The movies are selected from the [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) and IMDb ratings are taken from the [IMDb Datasets](https://www.imdb.com/interfaces/)._

</section>

