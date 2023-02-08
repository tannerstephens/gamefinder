import Home from './routes/Home.svelte';
import Login from './routes/Login.svelte';
import AddGame from './routes/AddGame.svelte';
import AddShelf from './routes/AddShelf.svelte';
import Game from './routes/Game.svelte';
import Games from './routes/Games.svelte';

export default {
    '/': Home,
    '/home': Home,
    '/login': Login,
    '/add-game': AddGame,
    '/add-shelf': AddShelf,
    '/games': Games,
    '/games/:gameId': Game,
}
