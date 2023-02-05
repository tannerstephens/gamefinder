<script>
    let clazz;
    export {clazz as class};
</script>

<div class={`columns ${clazz || ''}`}>
    <slot></slot>
</div>
