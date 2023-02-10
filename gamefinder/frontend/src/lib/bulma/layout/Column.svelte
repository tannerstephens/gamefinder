<script>
    let clazz;
    export {clazz as class};
</script>

<div class={`column ${clazz || ''}`}>
    <slot></slot>
</div>
