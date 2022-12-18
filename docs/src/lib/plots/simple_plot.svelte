<script>
    import Plot from "svelte-plotly.js";

    let wrapper;
    let changed = false;

    const data = [
        {
            x: [1, 2, 3, 4, 5],
            y: [1, 2, 4, 8, 16],
        },
    ];

    function change() {
        if (!changed) {
            const anchors = wrapper.querySelectorAll("a.modebar-btn");
            anchors.forEach((anchor) => {
                anchor.setAttribute("data-sveltekit-reload", "");
            });
            changed = true;
        }
    }
</script>

<div bind:this={wrapper} on:mouseenter={change}>
    <Plot
        {data}
        layout={{
            margin: { t: 0 },
            yaxis: {
                type: "log",
                autorange: true,
            },
        }}
        fillParent="width"
        debounce={250}
    />
</div>
