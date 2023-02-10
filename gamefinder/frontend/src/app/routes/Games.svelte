<script>
    import api from "$lib/api";
    import Columns from "$lib/bulma/layout/Columns.svelte";
    import GameCard from "./games/GameCard.svelte";

    let page = 1;

    let games = [];
    let total_pages;

    $: api.getGames(page)
    .then(json => {
        games = json.games;
        total_pages = json.total_pages;
    });
</script>


<Columns class="is-multiline">
    {#each games as game}
        <GameCard game={game} />
    {/each}
</Columns>

<nav class="pagination is-centered" aria-label="pagination">
    <button class="button pagination-previous is-link" disabled={page==1} on:click={() => page -= 1}>Previous</button>
    <button class="button pagination-next is-link" disabled={page>=total_pages} on:click= {() => page += 1}>Next page</button>
</nav>


<style>
    .button:disabled:hover {
        color: hsl(0deg, 0%, 48%);
    }
</style>
