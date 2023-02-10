<script>
    import { replace } from 'svelte-spa-router'

    import Form from '$lib/components/Form.svelte';
    import Input from '$lib/bulma/form/Input.svelte';

    import api from '$lib/api';
    import config from '$lib/stores/config';

    let username='', password='', verifyPassword='', submitEnabled=false;

    const onChange = () => {
        submitEnabled = (username.length > 0 && password.length > 0 && (password == verifyPassword));
    }

    const submit = () => {
        if (submitEnabled) {
            api.setConfig(username, password)
                .then(json => config.set(json));
        }
    }

    $: if($config.setup_completed === true) {
        replace('/');
    }
</script>

<Form title="First Time Setup" submitEnabled={submitEnabled} on:submit={submit}>
    <Input name="Admin Username" bind:value={username} type="text" on:change={onChange} />
    <Input name="Admin Password" bind:value={password} type="password" on:change={onChange} />
    <Input name="Verify Password" bind:value={verifyPassword} type="password" on:change={onChange} />
</Form>
