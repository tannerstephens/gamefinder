<script>
    import { createEventDispatcher } from 'svelte';

    import { Column, Columns, Level } from '../bulma/layout';
    import {Box} from '../bulma/elements';

    const dispatch = createEventDispatcher();

    const submit = e => {
        e.preventDefault();
        dispatch('submit');
    }

    export let title;
    export let submitEnabled = true;
</script>

<Columns class="is-centered">
    <Column class="is-half">
        <Box>
            <h1 class="title">{title}</h1>

            <form on:submit={submit}>
                <slot></slot>
                <br>
                <Level>
                    <span slot="right">
                        <button class="button is-primary" type="submit" disabled={!submitEnabled}>Submit</button>
                    </span>
                </Level>
            </form>
        </Box>
    </Column>
</Columns>
