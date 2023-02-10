import Game from './routes/Game.svelte';
import Games from './routes/Games.svelte';
import Home from './routes/Home.svelte';
import Login from './routes/Login.svelte';
import Setup from './routes/Setup.svelte';
import AdminApp from './routes/admin/AdminApp.svelte';


export default {
    '/': Home,
    '/home': Home,
    '/login': Login,
    '/games': Games,
    '/games/:gameId': Game,
    '/setup': Setup,
    '/admin/*': AdminApp
}
