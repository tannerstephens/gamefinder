<script>
    import { Container } from '$lib/bulma/layout';
    import NavbarEnd from './navbar/NavbarEnd.svelte';
    import NavbarStart from './navbar/NavbarStart.svelte';

    let isActive = false;
</script>

<nav class="navbar is-light">
    <Container>
        <div class="navbar-brand">
            <a class="navbar-item" href="#/">
                <b>GameFinder</b>
            </a>

            <button class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar" class:is-active={isActive} on:click={() => (isActive = !isActive)}>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </button>
        </div>

        <div id="navbar" class="navbar-menu" class:is-active={isActive}>
            <NavbarStart />
            <NavbarEnd />
        </div>
    </Container>
</nav>
