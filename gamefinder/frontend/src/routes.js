import { wrap } from 'svelte-spa-router/wrap';
import Setup from './routes/Setup.svelte';
import MainApp from './routes/MainApp.svelte';

import api from './api';

const mainApp = wrap({
    component: MainApp,
    conditions: [
        async () => {
            const json = await api.getConfig()

            return json.setup_completed;
        },
    ]});

export default {
    '/': mainApp,
    '/setup': Setup,
    '/*': mainApp
}
