<script>
import Histogram from "$lib/plots/histogram.svelte"

</script>

<section class="justify">

## What is a bad movie?

Taste is subjective. So it's subjective what constitutes a "bad" movie, as different people have different tastes and opinions about films. However there objective numbers like ratings and revenue, which quantify how successful, popular and beloved a movie is. We can use these measures as a proxy to select movies for the further analysis. The revenue would be a bad idea, since it would just tell us how popular a movie is. Think here of the last big Marvel Studios movie. Alternatively we use the IMDb rating to determine how good a movie is.

<Histogram />

The histogram shows that more movies are positively rated. Since our data is just have a partial snapshot of the IMDb ratings and is biased towards positive and more popular movies. To define a cutoff rating we made small survey ($n =$ 10), which resulted in a cutoff rating of x.
</section>

