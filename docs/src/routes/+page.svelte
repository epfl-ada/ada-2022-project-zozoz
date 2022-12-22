<script>
    import Intro from "$lib/intro.md";
    import Why from "$lib/why_bad_movies.md";
    import Gender from "$lib/gender.md";
    import Director from "$lib/director.md";
    import Conclusion from "$lib/conclusion.md";
    import Footer from "$lib/footer.md";
    import Video from "$lib/Video.svelte";
</script>

<Video />

<div class="max-width-3 mx-auto mt3" id="start">
    <Intro />
    <Why />
    <Gender />
    <Director />
    <Conclusion />
    <Footer />
</div>

<style>
    #start {
        min-height: 100vh;
    }
</style>
