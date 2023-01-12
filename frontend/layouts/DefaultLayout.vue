<template>
  <div
    :style="{
      backgroundImage: `url(/_nuxt/assets/images/bg.webp)`,
      backgroundPosition: 'fixed',
    }"
    class="w-full p-4 overflow-x-hidden"
  >
    <div class="container rounded-[40px] m-auto p-4 sm:p-[60px]">
      <LayoutTheHeader> Hello </LayoutTheHeader>
      <div class="overflow-y-scroll main animate__animated animate__fadeIn">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: ["auth"],
});
</script>

<style scoped lang="scss">
.main {
  height: calc(100vh - 36px);
  @screen sm {
    & {
      height: calc(100vh - 240px);
    }
  }
}
</style>
