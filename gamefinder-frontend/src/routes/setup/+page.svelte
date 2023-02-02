<script>
    import '$lib/app.scss';

    let step = 0;
    const numSteps = 5;

    const submit = () => {
        console.log('submit')
    };
</script>

<section class="section">
    <div class="container">
        <div class="columns">
            <div class="column is-half is-offset-one-quarter">
                <div class="box">
                    <h1 class="title">First Time Setup</h1>
                    <div class="tab" class:active={step === 0}>
                        <div class="field">
                            <label class="label" for="username">Admin Username</label>
                            <div class="control">
                                <input class="input" type="text" id="username">
                            </div>
                        </div>
                        <div class="field">
                            <label class="label" for="password">Admin Password</label>
                            <div class="control">
                                <input class="input" type="password" id="password">
                            </div>
                        </div>
                        <div class="field">
                            <label class="label" for="verify">Verify Password</label>
                            <div class="control">
                                <input class="input" type="password" id="verify">
                            </div>
                        </div>
                    </div>
                    <div class="tab" class:active={step === 1}>
                        <div class="field">
                            <label class="label" for="username">Board Game Atlas Client ID</label>
                            <div class="control">
                                <input class="input" type="text" id="username">
                            </div>
                        </div>
                    </div>
                    <div style="text-align:center;margin-top:40px;">
                        {#each [...Array(numSteps)] as _, i}
                            <span class="step" class:active={step === i}></span>
                        {/each}
                    </div>
                    <nav class="level">
                        <div class="level-left">
                            {#if step > 0}
                                <div class="level-item">
                                    <button class="button" on:click={() => {step -= 1}}>Previous</button>
                                </div>
                            {/if}
                        </div>
                        <div class="level-right">
                            {#if step < numSteps - 1}
                                <div class="level-item">
                                    <button class="button is-link" on:click={() => {step += 1}}>Next</button>
                                </div>
                            {:else}
                                <div class="level-item">
                                    <button class="button is-success" disabled on:click={submit}>Submit</button>
                                </div>
                            {/if}
                        </div>
                    </nav>
                </div>
            </div>
        </div>
    </div>
</section>

<style>
    /* Style the form */
    #regForm {
        background-color: #ffffff;
        margin: 100px auto;
        padding: 40px;
        width: 70%;
        min-width: 300px;
    }

    /* Style the input fields */
    input {
        padding: 10px;
        width: 100%;
        font-size: 17px;
        font-family: Raleway;
        border: 1px solid #aaaaaa;
    }

    /* Mark input boxes that gets an error on validation: */
    input.invalid {
        background-color: #ffdddd;
    }

    /* Hide all steps by default: */
    .tab {
        display: none;
    }

    .tab.active {
        display: block;
    }

    /* Make circles that indicate the steps of the form: */
    .step {
        height: 15px;
        width: 15px;
        margin: 0 2px;
        background-color: #bbbbbb;
        border: none;
        border-radius: 50%;
        display: inline-block;
        opacity: 0.5;
    }

    /* Mark the active step: */
    .step.active {
        opacity: 1;
    }
</style>
