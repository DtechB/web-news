<template>
  <div>Hello</div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "auth-layout",
  middleware: ["auth"],
});
</script>
