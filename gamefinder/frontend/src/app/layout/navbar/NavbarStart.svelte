<script>
    import user from '$lib/stores/user';
</script>

<div class="navbar-start">
    <a class="navbar-item" href="#/games">
        Games
    </a>

    {#if $user && $user.is_admin}
        <a class="navbar-item" href="#/add-game">
            Add Game
        </a>
        <a class="navbar-item" href="#/add-shelf">
            Add Shelf
        </a>
    {/if}
</div>
