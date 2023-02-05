<script>
	import Router from 'svelte-spa-router';
	import routes from './routes';

	import Navbar from './mainApp/Navbar.svelte';
	import {Section, Container} from '../bulma/layout';
</script>

<main>
	<Navbar />
	<Section>
		<Container>
			<Router {routes} />
		</Container>
	</Section>
</main>
