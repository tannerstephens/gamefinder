<script>
    import { replace } from 'svelte-spa-router'
    import {Input} from '../../bulma/form';
    import Form from '../../elements/Form.svelte';

    import api from '../../api';
    import user from '../../stores/user';

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
