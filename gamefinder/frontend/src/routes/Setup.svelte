<script>
    import { replace } from 'svelte-spa-router'

    import Form from '../elements/Form.svelte';
    import { Section, Container } from '../bulma/layout';
    import { Input } from '../bulma/form';

    import api from '../api';

    let username='', password='', verifyPassword='', submitEnabled=false;

    const onChange = () => {
        submitEnabled = (username.length > 0 && password.length > 0 && (password == verifyPassword));
    }

    const submit = () => {
        if (submitEnabled) {
            api.setConfig(username, password)
            .then(json => {
                console.log(json);
                if(json.setup_completed) {
                    replace('/');
                }
            });
        }
    }
</script>

<Section>
    <Container>
        <Form title="First Time Setup" submitEnabled={submitEnabled} on:submit={submit}>
            <Input name="Admin Username" bind:value={username} type="text" on:change={onChange} />
            <Input name="Admin Password" bind:value={password} type="password" on:change={onChange} />
            <Input name="Verify Password" bind:value={verifyPassword} type="password" on:change={onChange} />
        </Form>
    </Container>
</Section>
