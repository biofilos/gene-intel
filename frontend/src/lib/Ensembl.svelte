<script lang="ts">
    interface EnsData {
        ensid: string;
        data: string;
    }
    import {onMount} from "svelte";
    import {gene} from "./store.ts"
    import {species} from "./store.ts";

    let ensName = ""
    let speciesSel = ""
    let data: EnsData = {ensid: "", data: ""};
    gene.subscribe(value => {
        ensName = value
    })
    species.subscribe(value => {
        speciesSel = value
    })
    async function ensData(geneId: string) {

        if (ensName !== "") {

            const res = await fetch(`/api/ensembl/${geneId}`);
            data = await res.json();
        }
    }
    $: ensData(ensName)
</script>
{#if ensName != ""}
    <p>{ensName}</p>
    <p>{JSON.stringify(data)}</p>
    <p>Species: {speciesSel}</p>

{/if}
