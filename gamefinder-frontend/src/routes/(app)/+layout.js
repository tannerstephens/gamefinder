import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
    const resp = await fetch('/api/setup');
    const json = await resp.json();

    if(!json.setup_completed) {
        throw redirect(307, '/setup')
    }
}
