<script>
import { base } from "$app/paths";

let num = true;
let innerText = "Num"
</script>


<section class="justify">

## Genre
Clustering movies into genres is a complex task, maybe harder than agreeing on what is a good movie. Among the enormous diversity of genres in the movie landscape, we all have our preferred one. An adventure movie could remind us of our childhood experiences or awaken us as a hidden explorers. A horror movie can give us a rush of adrenaline worthy of a 1h30-long bungee jump. But are they genres that tend to produce bad films? Based on preliminary annotations, we gathered movies into eleven non-exclusive genres ranging from animation to comedy. In the heatmap, we can see that the distribution of movies is not uniform across these genres. Is it because the public especially likes the drama type? Is it because these are the movies which cost less to produce? So many questions and still no answer. Let’s jump into a serious analysis.

<button class="hover-underline-animation" on:click="{() => num = !num}">
    {#if num == true}
        Show #num of releases per decade 
    {:else}
        Show average rating per decade
    {/if}
</button>
{#if num == true}
    <img src="{base}/plots/genre_heatmap_num.png" alt="Count"/>
    <img src="{base}/plots/genre_heatmap_rating.png" style="display:none;" alt="Rating"/>
{:else}
    <img src="{base}/plots/genre_heatmap_num.png" style="display:none;" alt="Count"/>
    <img src="{base}/plots/genre_heatmap_rating.png" alt="Rating"/>
{/if}

We used an observational study framework using the genre as the treatment and a simple goal: Is the treatment causal for deciding if a movie is bad? We proceeded to an analysis per genre and decade to see potential variations across time. Eight of the eleven genres showed significance in determining if a movie is bad. The three ones associated with the coefficients with the most considerable absolute value are drama, horror and “genre”. The two first have positive coefficients. Thus, it may be time to reconsider the pitch of your horror movie that displays deep familial drama.

On the other hand, a movie that has a more pronounced artistic approach (that we tag as “genre”) is more likely to please the IMDb audience. This could be explained by the themes and stories these different genres approach. A slasher with a lot of blood or a psychological horror movie is more likely to result in diverging opinions than a comedy (which has, as “genre”, a negative coefficient). The fact that “genre” movies have better ratings could be due to a specific community of users in IMDb. They could be the only ones to watch and rate these movies, whereas the other genres are more widespread. Note that these results could also result from how we define the genre of a film, which is entirely subjective.
</section>

