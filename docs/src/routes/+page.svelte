<script>
    import Intro from "$lib/intro.md";
    import Why from "$lib/why_bad_movies.md";
    import Gender from "$lib/gender.md";
    import Director from "$lib/director.md";
    import Genre from "$lib/genre.md";
    import Budget from "$lib/budget.md";
    import Conclusion from "$lib/conclusion.md";
    import Footer from "$lib/footer.md";
    import Video from "$lib/Video.svelte";

    let y;

    function scrollIntoView({ target }) {
        const el = document.querySelector(target.getAttribute("href"));
        if (!el) return;
        el.scrollIntoView({
            behavior: "smooth",
        });
    }
</script>

<svelte:head>
    <title>What makes a bad movie bad? - ZOZOZO</title>
</svelte:head>

<svelte:window bind:scrollY={y} />
{#if y > 100}
    <ul class="list-reset nav ml4">
        <li>
            <a
                href="#start"
                class="hover-underline-animation"
                on:click|preventDefault={scrollIntoView}>Intro</a
            >
        </li>
        <li>
            <a
                href="#genre"
                class="hover-underline-animation"
                on:click|preventDefault={scrollIntoView}>Genre</a
            >
        </li>
        <li>
            <a
                href="#gender"
                class="hover-underline-animation"
                on:click|preventDefault={scrollIntoView}>Gender Balance</a
            >
        </li>
        <li>
            <a
                href="#director"
                class="hover-underline-animation"
                on:click|preventDefault={scrollIntoView}>Director</a
            >
        </li>
        <li>
            <a
                href="#budget"
                class="hover-underline-animation"
                on:click|preventDefault={scrollIntoView}>Budget</a
            >
        </li>
        <li>
            <a
                href="#conclusion"
                class="hover-underline-animation"
                on:click|preventDefault={scrollIntoView}>Conclusion</a
            >
        </li>
    </ul>
{/if}

{#if y > 1000}
    <ul class="list-reset nav mr4" style="right: 0;">
        <li>
            <a
                href="#start"
                class="hover-underline-animation"
                on:click|preventDefault={scrollIntoView}>Scroll to top</a
            >
        </li>
    </ul>
{/if}
<Video />

<div class="max-width-3 mx-auto mt3" id="start">
    <Intro />
    <Why />
    <div id="genre">
        <Genre />
    </div>
    <div id="gender">
        <Gender />
    </div>
    <div id="director">
        <Director />
    </div>
    <div id="budget">
        <Budget />
    </div>
    <div id="conclusion">
        <Conclusion />
    </div>

    <Footer />
</div>

<style>
    #start {
        min-height: 100vh;
    }
    .nav {
        position: fixed;
        bottom: 0;
    }
</style>
