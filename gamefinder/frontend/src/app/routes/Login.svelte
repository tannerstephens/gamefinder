<script>
    import { replace } from 'svelte-spa-router'
    import {Input} from '$lib/bulma/form';
    import Form from '$lib/components/Form.svelte';

    import api from '$lib/api';
    import user from '$lib/stores/user';

    let username='', password='', submitEnabled=false;

    const submit = () => {
        api.login(username, password)
        .then(json => {
            if(json.success) {
                user.set(json.user);
                replace('/')
            }
        });
    };

    const change = () => {
        submitEnabled = (username.length > 0) && (password.length > 0);
    }
</script>

<Form title="Login" submitEnabled={submitEnabled} on:submit={submit}>
    <Input name="Username" type="text" bind:value={username} on:change={change} />
    <Input name="Password" type="password" bind:value={password} on:change={change} />
</Form>
