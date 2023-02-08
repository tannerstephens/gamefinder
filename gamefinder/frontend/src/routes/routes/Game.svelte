<script>
    import api from "../../api";

    import Box from "../../bulma/elements/Box.svelte";

    import {Column, Columns} from "../../bulma/layout";

    export let params;

    let game;

    $: api.getGame(params.gameId)
    .then(json => {
        game = json.game;
    });
</script>

<Box>
    {#if game}
        <Columns>
            <Column class="is-one-fifth">
                <figure class="image"><img alt={game.name} src={game.image} height="128"></figure>
            </Column>
            <Column>
                <h1 class="title">{game.name}</h1>
                {@html game.description}
            </Column>
        </Columns>
    {/if}
</Box>
