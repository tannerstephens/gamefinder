<script>
    import { location } from 'svelte-spa-router';

    import { Section, Container } from '$lib/bulma/layout';

    import Navbar from './layout/Navbar.svelte';
</script>


{#if $location != '/setup'}
    <Navbar />
{/if}

<Section>
    <Container>
        <slot></slot>
    </Container>
</Section>
