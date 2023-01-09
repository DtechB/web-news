<template>
  <div
    class="BaseIcon aspect-square"
    :style="{
      backgroundColor,
      borderRadius,
      width: size,
      height: size,
      padding,
    }"
    @click="$emit('onClick')"
  >
    <div
      class="icon"
      :class="{ 'icon-hover': cursorPointer }"
      :style="[
        { '-webkit-mask': `url(/_nuxt/icons/${name}.svg)` },
        { mask: `url(/icons/${name}.svg)` },
        { width: '100%' },
        { height: '100%' },
        { backgroundColor: color },
      ]"
    ></div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  name: String,
  size: { type: String, default: "115px" },
  color: { type: String, default: "var(--color-blue-300)" },
  backgroundColor: { type: String, default: "none" },
  borderRadius: { type: String, default: "50%" },
  cursorPointer: { type: Boolean, default: false },
  padding: { type: String, default: "30px" },
});

const emits = defineEmits(["onClick"]);
</script>
