import { writable } from 'svelte/store';
import api from '../api';

const config = writable({});

api.getConfig()
    .then(json => config.set(json));

export default config;
