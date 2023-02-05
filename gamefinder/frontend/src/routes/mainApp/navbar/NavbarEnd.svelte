<script>
    import user from '../../../stores/user';
    import api from '../../../api';

    const logout = () => {
        api.logout()
        .then(json => {
            user.set(json.user);
        });
    }
</script>

<div class="navbar-end">
    {#if $user}
        <div class="navbar-item has-dropdown is-hoverable">
            <div class="navbar-link">
                {$user.username}
            </div>

            <div class="navbar-dropdown">
                <div class="navbar-item">
                    <button class="button is-dark" on:click={logout}>
                        Logout
                    </button>
                </div>
            </div>
        </div>
    {:else}
        <div class="navbar-item">
            <div class="buttons">
                <a class="button is-primary" href="#/sign-up">
                    <strong>Sign up</strong>
                </a>
                <a class="button is-dark" href="#/login">
                    Log in
                </a>
            </div>
        </div>
    {/if}
</div>
