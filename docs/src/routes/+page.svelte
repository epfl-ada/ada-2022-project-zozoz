<script>
    import Intro from "../content/intro.md";
    import Why from "../content/why_bad_movies.md";
    import Footer from "../content/footer.md";
    import Video from "../content/Video.svelte";
    import SimplePlot from "../content/plots/simple_plot.svelte";
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
