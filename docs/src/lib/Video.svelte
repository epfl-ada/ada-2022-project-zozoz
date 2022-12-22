<script>
    import { base } from "$app/paths";
    function scrollIntoView({ target }) {
        const el = document.querySelector(target.getAttribute("href"));
        if (!el) return;
        el.scrollIntoView({
            behavior: "smooth",
        });
    }
</script>

<div class="bg-video-wrap mt2">
    <video
        poster="{base}/poster.jpg"
        src="{base}/movie.mp4"
        loop
        muted
        autoplay
    />
    <div class="overlay-text">
        <span class="bg-pad h1"> What makes a bad movie bad? </span>
        <br />
        <br />
        <span class="h1 bg-pad italic mt4"
            >A data-driven analysis of Sharknado and co.</span
        >
    </div>
    <div class="overlay-bottom">
        <span class="bg-pad">
            <a
                href="#start"
                class="hover-underline-animation"
                on:click|preventDefault={scrollIntoView}>👇🏽 Read our story!</a
            ></span
        >
    </div>
</div>

<style>
    .bg-video-wrap {
        position: relative;
        padding-bottom: 50%;
        padding-top: 0px;
        height: 0;
        overflow: hidden;
    }
    video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }

    .overlay-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        text-align: center;
    }
    .bg-pad {
        padding: 0.5rem 1rem;
        color: #000;
        background: #fcbe11;
    }

    .overlay-bottom {
        position: absolute;
        top: 95%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #000;
        text-align: center;
    }

    a {
        color: #000000;
        text-decoration: none;
    }

    a:visited {
        color: #000000;
    }

    .hover-underline-animation {
        display: inline-block;
        position: relative;
        color: #000000;
    }

    .hover-underline-animation::after {
        content: "";
        position: absolute;
        width: 100%;
        transform: scaleX(0);
        height: 2px;
        bottom: 0;
        left: 0;
        background-color: #000;
        transform-origin: bottom right;
        transition: transform 0.25s ease-out;
    }

    .hover-underline-animation:hover::after {
        transform: scaleX(1);
        transform-origin: bottom left;
    }
</style>
