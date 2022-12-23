<script>
import { base } from "$app/paths";

let num = true;
let innerText = "Num"
</script>


<section class="justify">

## Genre
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
</section>

