<script>
    export let value;
    export let name;

    export let options;
    export let placeholder=null;
</script>

<field class="field">
    <label class="label" for={name}>{name}</label>
    <div class="select">
        <select id={name} bind:value={value} on:change>
            {#if placeholder}
                <option value={null}>{placeholder}</option>
            {/if}
            {#if options}
                {#each options as option}
                    <option value={option.value}>{option.name}</option>
                {/each}
            {/if}
        </select>
    </div>
</field>
