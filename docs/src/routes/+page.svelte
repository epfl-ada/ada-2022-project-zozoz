<script>
    import Intro from "$lib/intro.md";
    import Why from "$lib/why_bad_movies.md";
    import Footer from "$lib/footer.md";
    import Video from "$lib/Video.svelte";
</script>

<Video />

<div class="max-width-3 mx-auto mt3" id="start">
    <Intro />
    <Why />
    <Footer />
</div>

<style>
    #start {
        min-height: 100vh;
    }
</style>
