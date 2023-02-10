<script>
    import { createEventDispatcher } from 'svelte';
    import TomSelect from '$lib/components/TomSelect.svelte';
    import api from '$lib/api';

    export let gameId;

    const dispatch = createEventDispatcher();
    const selectChange = value => {
        gameId = value;
        dispatch('change');
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

<TomSelect settings={gameSelectSettings} name="Game" placeholder="Search for a game..." />
