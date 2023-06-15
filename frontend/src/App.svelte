<script lang="ts">
	import { onMount} from "svelte";
	import {gene} from "./lib/store.ts"
	import {species} from "./lib/store.ts";
	import Ensembl from "./lib/Ensembl.svelte";

	let geneId = ""
	let user_name = "Guest";
	let inputGene = ""
	// make interface for this
	let speciesObj = [
		{code: "hsap", name: "Human", selected: true},
		{code: "mmus", name: "Mouse", selected: false},
		{code: "rnor", name: "Rat", selected: false},
		{code: "drer", name: "Zebrafish", selected: false},
	]
	let inputSpecies = speciesObj[0].name

	gene.subscribe(value => {
		geneId = value
	})
	species.subscribe(value => {
		inputSpecies = value
	})
	onMount(async () => {
		const user_req = await fetch("/api/current_user");
		const user_json = await user_req.json();
		user_name = user_json.username;
	});
	function setData(){
		// geneId = inputGene
		gene.set(inputGene)
		species.set(inputSpecies)
		for (let i=0; i<speciesObj.length; i++){
			if (speciesObj[i].code == inputSpecies){
				console.log(speciesObj[i])
			}
		}
	}
</script>

<main>
	<h1 class="italic hover:not-italic">Hello {user_name}</h1>
	<form on:submit|preventDefault={setData}>
		<label for="geneIn">Gene ID</label>
		<input type="text" id="geneIn" bind:value={inputGene}>
		<select bind:value={inputSpecies}>
			{#each speciesObj as sp}
					<option value={sp.name} selected={sp.selected}>{sp.name}</option>


			{/each}
		</select>
		<button>Get intel</button>
	</form>
		<Ensembl></Ensembl>

</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}


	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>