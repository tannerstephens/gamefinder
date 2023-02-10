<script>
	import "./app/app.scss";

	import config from './lib/stores/config';

	import Router, { replace } from 'svelte-spa-router';
	import routes from './app/routes';

	import Layout from "./app/Layout.svelte";

	$: if($config.setup_completed === false) {
		replace('/setup');
	}
</script>

<Layout>
	<Router {routes} />
</Layout>
