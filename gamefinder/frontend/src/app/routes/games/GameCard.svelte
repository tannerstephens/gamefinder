<script>
    export let game;

    import Column from "$lib/bulma/layout/Column.svelte";
</script>

<Column class="is-one-quarter">
    <a href='#/games/{game.id}'>
        <div class="card">
            <div class="card-image">
                <figure class="image is-regular">
                    <img src={game.image} alt="{game.name} Thumbnail">
                </figure>
            </div>
            <div class="card-content">
                <p class="title is-4">{game.name}</p>
                <p class="subtitle is-6">{game.location.shelf}: Row: {game.location.row}, Col: {game.location.col}</p>

                <div class="content">
                    {@html game.short_description}
                </div>
            </div>
        </div>
    </a>
</Column>

<style>
    .is-regular img {
        height: 256px;
        width: auto;
        margin: auto;
        padding: 20px;
    }

    .is-regular {
        background-color: white;
    }

    .card {
        height: 100%;
    }
</style>
