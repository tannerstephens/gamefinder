<script>
    import Router, { replace } from 'svelte-spa-router';
    import user from '$lib/stores/user';

    import routes from './adminApp/routes';

    $: if($user === null || !$user.is_admin) {
        replace('/');
    }
</script>

<Router {routes} prefix="/admin" />
