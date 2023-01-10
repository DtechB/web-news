<template>
  <div className="BaseButtonGroup flex">
    <BaseButton
      :text="rightButtonText"
      color="var(--color-blue-300)"
      backgroundColor="var(--color-slate-900)"
      padding="8px 16px 8px 48px"
      @on-click="emits('onRightButtonClick')"
    />
    <BaseButton
      :text="leftButtonText"
      class="z-10"
      margin="0 -48px 0 0"
      @on-click="emits('onLefttButtonClick')"
    />
  </div>
</template>

<script setup lang="ts">
defineProps({
  leftButtonText: {
    type: String,
    required: true,
  },
  rightButtonText: {
    type: String,
    required: true,
  },
});

const emits = defineEmits(["onRightButtonClick", "onLefttButtonClick"]);
</script>
