<script>
    import Intro from "$lib/intro.md";
    import Why from "$lib/why_bad_movies.md";
    import Footer from "$lib/footer.md";
    import Video from "$lib/Video.svelte";
    import SimplePlot from "$lib/plots/simple_plot.svelte";
</script>

<Video />

<div class="max-width-3 mx-auto mt3" id="start">
    <Intro />
    <Why />
    <SimplePlot />
    <Footer />
</div>

<style>
    #start {
        min-height: 100vh;
    }
</style>
