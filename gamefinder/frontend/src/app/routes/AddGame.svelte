<script>
    import { push } from 'svelte-spa-router'
    import GameSearch from './addGame/GameSearch.svelte';

    import Form from '$lib/components/Form.svelte';
    import { Input, Select } from '$lib/bulma/form';

    import api from '$lib/api';

    let submitEnabled = false;
    let gameId;
    let shelfOptions, shelfId, shelf={}, shelves;
    let row, column;

    api.getShelves()
        .then(json => {
            shelfOptions = json.shelves.map(shelf => ({name: shelf.name, value: shelf.id}));
            shelves = json.shelves;
        });

    const submit = () => {
        api.addGame(gameId, shelfId, row, column)
            .then(json => {
                if (json.success) {
                    push(`/games/${json.game.id}`)
                }
            })
        };

    const change = () => {
        submitEnabled = gameId && shelfId && row && column;

        if(shelfId != shelf.id && shelfId !== null) {
            console.log(shelfId)
            shelf = shelves.filter(shelf => shelf.id == shelfId)[0];
        } else {
            shelf = {};
        }

        if(shelf) {
            if(row > shelf.height) {row = shelf.height}
            if(column > shelf.width) {column=shelf.width}
        }
        if(row < 1) {row = 1}
        if(column < 1) {column = 1}

    }
</script>

<Form title="Add Game" submitEnabled={submitEnabled} on:submit={submit}>
    <GameSearch bind:gameId on:change={change} />
    <Select name="Shelf" options={shelfOptions} placeholder="Select shelf..." bind:value={shelfId} on:change={change} />
    <Input name="Column" type="number" bind:value={column} on:change={change} min="1" max={shelf.width} />
    <Input name="Row" type="number" bind:value={row} on:change={change} min="1" max={shelf.height} />
</Form>
