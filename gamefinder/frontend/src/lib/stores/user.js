import { writable } from 'svelte/store';
import api from '../api';

const user = writable({});

api.getCurrentUser()
    .then(json => user.set(json));

export default user;
