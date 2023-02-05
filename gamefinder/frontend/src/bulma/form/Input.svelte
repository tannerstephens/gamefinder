<script>
    import { createEventDispatcher } from 'svelte';

    export let value;
    export let name;
    export let type;

    const dispatch = createEventDispatcher();

    const handleInput = e => {
        value = type.match(/^(number|range)$/)
        ? +e.target.value
        : e.target.value;

        dispatch('change');
    }
</script>

<field class="field">
    <label class="label" for={name}>{name}</label>
    <div class="control">
        <input id={name} class="input" type={type} value={value} on:input={handleInput}>
    </div>
</field>
