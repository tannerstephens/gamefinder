<script>
    import user from '$lib/stores/user';
</script>

<div class="navbar-start">
    <a class="navbar-item" href="#/games">
        Browse Games
    </a>

    {#if $user !== null && $user.is_admin}
        <div class="navbar-item has-dropdown is-hoverable">
            <div class="navbar-link">
                Admin Zone
            </div>
            <div class="navbar-dropdown">
                <a class="navbar-item" href="#/admin/add-game">
                    Add Game
                </a>
                <a class="navbar-item" href="#/admin/add-shelf">
                    Add Shelf
                </a>
            </div>
        </div>
    {/if}
</div>
