<script>
    import { push } from 'svelte-spa-router'

    import Form from '../../elements/Form.svelte';
    import { Input, Select } from '../../bulma/form';

    import TomSelect from '../../elements/TomSelect.svelte';

    import api from '../../api';

    let submitEnabled = false;
    let gameId;
    let shelfOptions, shelfId, shelf={}, shelves;
    let row, column;

    api.getShelves()
    .then(json => {
        shelfOptions = json.shelves.map(shelf => ({name: shelf.name, value: shelf.id}));
        shelves = json.shelves;
    })

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

        if(shelfId) {
            shelf = shelves.filter(shelf => shelf.id == shelfId)[0];

            if(row > shelf.height) {row = shelf.height}
            if(column > shelf.width) {column=shelf.width}
        } else {
            shelf = {};
        }

        if(row < 1) {row = 1}
        if(column < 1) {column = 1}

    }

    const selectChange = value => {
        gameId = value;
        change();
    };

    const gameSelectSettings = {
        labelField: 'name',
        valueField: 'id',
        searchField: 'name',
        maxItems: 1,
        loadThrottle: 1000,
        shouldLoad: query => query.length >= 2,
        load: (query, callback) => {
            api.bggSearch(query)
            .then(json => callback(json))
            .catch(() => callback())
        },
        render: {
            option: data => {
                const end = data.year ? ` (${data.year})` : '';
                const text = data.name + end;
                return `<div>${text}</div>`;
            },
            item: data => {
                const end = data.year ? ` (${data.year})` : '';
                const text = data.name + end;
                return `<span class="tag is-primary">${text}</span>`;
            },
        },
        onChange: selectChange,
    }
</script>

<Form title="Add Game" submitEnabled={submitEnabled} on:submit={submit}>
    <TomSelect settings={gameSelectSettings} name="Game" placeholder="Search for a game..." />
    <Select name="Shelf" options={shelfOptions} placeholder="Select shelf..." bind:value={shelfId} on:change={change} />
    <Input name="Column" type="number" bind:value={column} on:change={change} min="1" max={shelf.width} />
    <Input name="Row" type="number" bind:value={row} on:change={change} min="1" max={shelf.height} />
</Form>
