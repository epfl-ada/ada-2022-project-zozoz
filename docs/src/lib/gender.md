<script>
import { base } from "$app/paths";
</script>

<section class="justify">

## Gender Ratio

The fact that sexism is rooted in the cinema industry is not new. Several concepts, such as the [Bechdel test](https://bechdeltest.com/), have already demonstrated the imbalance in the roles of actresses vs actors. To investigate the role of gender balance in the movie's success, we computed the mean of the number of actresses minus the number of actors: $$E[\#actress - \#actor]$$. Our preliminary analysis has shown a negative correlation between this handcrafted feature and the movie's success. Would movies with more men than women be more successful? 

![Genderratio]({base}/plots/genreratio.png)

A quick look at the evolution of the gender balance across decades showed a biased but relatively stable value. Nevertheless, we still asked ourselves if we could find any signal in the data indicating a causal effect for the gender balance. After running an observational study over several decades, we discovered no significant impact, neither on the global success of a movie nor on the fact that a movie was designated as a bad one across time. This is somehow a reassuring statement that, indeed, gender has nothing to do with the success of a piece.



The initial correlation can come from multiple factors. Maybe some genres favour the usage of actors over actresses, and these genres are more readily associated with terrible movies. It would be interesting to extend this analysis to people behind the camera, such as directors, producers or writers, as those are also prominent actors in the movie's success.

</section>

