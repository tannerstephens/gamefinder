<script>
    let clazz="";
    export { clazz as class };
</script>

<div class={`container ${clazz || ''}`}>
    <slot></slot>
</div>
