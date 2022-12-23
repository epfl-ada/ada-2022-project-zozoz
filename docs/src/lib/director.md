<script>
import { base } from "$app/paths";
</script>

<section class="justify">

## Director

With all the respect we have for the fans of [Quentin Tarantino](https://www.imdb.com/name/nm0000233/), [Rajkumar Hirani](https://www.imdb.com/name/nm0386246/) or [Agnès Varda](https://www.imdb.com/name/nm0889513/), we still wanted to see if we could attribute the success (or failure in our case) of a movie to the choice of its director. As stated before, directors are often at the heart of movie creation. You probably have one, if not several, directors of which you like the work, and you praise like the new creator of heaven on earth.

Due to a large number (4702) of directors in our database and the omnipresent curse of dimensionality, we were unable to test for each different director to identify precisely if a subset could be considered as the bad-movies-makers. Thus we decided to develop a summary feature for the entire directing team. We tested if a directing team with no successful movie in the past was more likely to produce a bad film. To sum up, do the loose attract the loose?

After our traditional observational study over decades, we see that having a directing team that has no previous success is not necessarily good news for the quality of the film. Or conversely, a successful directing team is more prone to create movies that will find its audience. However, we have to be careful about the interpretation of these results. The classification of a film depends on the rating of the users. Thus we could have a trend where users involved in creating these databases are biased toward praising the work of famous or successful directors regardless of the movie's actual quality.


A second question we asked ourselves is how the non-success of a director evolves over their lifetime. Are some directors doomed to produce terrible films over and over again? To perform the analysis over time, we modelled the realization of a successful movie as the "death" of the infamous director. 

![Rating Distribution]({base}/plots/director_success.png)

It allowed us to draw the following Kaplan-Meier curve. Knowing that in our data, the mean (median) age of death of a director is 75.35 (77.0) years old, we can see that a significant portion of directors will stay in the a posteriori, not-so-closed circle of non-successful directors for eternity. So if one day you are in charge of the production of a movie, be careful before recruiting an old director without any previous success. But mainly, perform additional statistical analyses on the causation of director age in the movie success because we would not want to draw early conclusions; everyone deserves a chance

</section>

