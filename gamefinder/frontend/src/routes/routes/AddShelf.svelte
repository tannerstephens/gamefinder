<script>
    import { push } from 'svelte-spa-router'


    import Form from '../../elements/Form.svelte';
    import { Input } from '../../bulma/form';
    import Select from '../../bulma/form/Select.svelte';

    import api from '../../api';

    let submitEnabled = false, name='', width, height, type;

    const submit = () => {
        if(submitEnabled) {
            api.addShelf(name, type, width, height)
            .then(json => {
                if(json.success) {
                    push('/');
                }
            });
        }
    };

    const change = () => {
        submitEnabled = (name.length > 0 && type !== undefined && width > 0 && height > 0);
    };

    const options = [
        {
            name: 'Standard',
            value: 'standard'
        },
        {
            name: 'Cube',
            value: 'cube'
        }
    ];
</script>

<Form title="Add Shelf" submitEnabled={submitEnabled} on:submit={submit}>
    <Input name="Name" type="text" bind:value={name} on:change={change} />
    <Select bind:value={type} name="Type of Shelf" options={options} on:change={change} />
    <Input name="Width" type="number" bind:value={width} on:change={change} min="1" />
    <Input name="Height" type="number" bind:value={height} on:change={change} min="1" />
</Form>
