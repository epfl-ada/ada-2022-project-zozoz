<script>
    import Example from "../content/example.md";
    import Video from "../content/Video.svelte";

    import Plot from "svelte-plotly.js";

    const data = [
        {
            x: [1, 2, 3, 4, 5],
            y: [1, 2, 4, 8, 16],
        },
    ];
</script>

<Video />

<div class="max-width-4 mx-auto" id="start">
    <h1>LOL</h1>
    <Example />
    <Plot
        {data}
        layout={{
            margin: { t: 0 },
        }}
        fillParent="width"
        debounce={250}
    />
</div>

<style>
    #start {
        min-height: 100vh;
    }
</style>
