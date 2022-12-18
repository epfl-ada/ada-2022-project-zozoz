<script>
    import Plot from "svelte-plotly.js";
    import * as d3 from "d3";
    import { onMount } from "svelte";
    import { base } from "$app/paths";

    let wrapper;
    let changed = false;
    let data;
    console.log(base);
    onMount(async () => {
        let ratings = [];

        await d3.csv(base + "/data/hist.csv", function (rows) {
            ratings.push(rows.ratings);
        });
        data = [
            {
                x: ratings,
                type: "histogram",
                nbinsx: 10,
            },
        ];
    });

    function change() {
        if (!changed) {
            const anchors = wrapper.querySelectorAll("a.modebar-btn");
            anchors.forEach((anchor) => {
                anchor.setAttribute("data-sveltekit-reload", "");
            });
            changed = true;
        }
    }
    var fillParent = true;
</script>

<div
    bind:this={wrapper}
    on:mouseenter={change}
    style="width: 100%; height: 100%; min-height: 400px;"
>
    <Plot
        {data}
        {fillParent}
        layout={{
            margin: { t: 30 },

            title: "Distribution of ratings in our IMDb dataset",
            xaxis: {
                title: "Rating",
            },
            yaxis: {
                title: "Number of movies (log scale)",
                type: "log",
            },
        }}
        debounce={250}
    />
</div>
