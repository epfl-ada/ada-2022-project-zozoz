<script>
    function scrollIntoView({ target }) {
        const el = document.querySelector(target.getAttribute("href"));
        if (!el) return;
        el.scrollIntoView({
            behavior: "smooth",
        });
    }
</script>

<div class="bg-video-wrap">
    <video src="./movie.mp4" loop muted autoplay />
    <div class="overlay-text">
        <span class="bg-pad h1"> Is John the reason for the success? </span>
        <br />
        <br />
        <span class="h1 bg-pad italic h1 mt4"
            >A deep dive of the temporal changes in movie</span
        >
    </div>
    <div class="overlay-bottom">
        <span class="bg-pad">
            <a
                href="#start"
                class="hover-underline-animation"
                on:click|preventDefault={scrollIntoView}>👇 Read our story!</a
            ></span
        >
    </div>
</div>

<style>
    .bg-video-wrap {
        position: relative;
        overflow: hidden;
        width: 100%;
        height: 100vh;
    }
    video {
        min-width: 100%;
        min-height: 100vh;
        z-index: 1;
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
        padding: 0.5rem 2rem;
        color: #fff;
        background: rgb(0, 0, 0);
    }

    .overlay-bottom {
        position: absolute;
        top: 95%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        text-align: center;
    }

    a {
        color: #ffffff;
        text-decoration: none;
    }

    a:visited {
        color: #ffffff;
    }

    .hover-underline-animation {
        display: inline-block;
        position: relative;
        color: #ffffff;
    }

    .hover-underline-animation::after {
        content: "";
        position: absolute;
        width: 100%;
        transform: scaleX(0);
        height: 2px;
        bottom: 0;
        left: 0;
        background-color: #ffffff;
        transform-origin: bottom right;
        transition: transform 0.25s ease-out;
    }

    .hover-underline-animation:hover::after {
        transform: scaleX(1);
        transform-origin: bottom left;
    }
</style>
