<script>
    import TomSelect from 'tom-select';
    import { onMount } from 'svelte';

    let inputElement;
    export let settings = {};
    export let name;

    onMount(() => new TomSelect(inputElement, settings));
</script>

<field class="field">
    <label class="label" for={name}>{name}</label>
    <div class="control">
        <input bind:this={inputElement} id={name} {...$$props}>
    </div>
</field>
