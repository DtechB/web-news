<template>
  <div
    class="BaseButton md:cursor-pointer transition-all xl:px-16 xl:py-4 lg:px-12 lg:py-3 px-8 py-2 rounded-full"
    :style="{ backgroundColor }"
    @click="$emit('onClick')"
  >
    <div class="flex items-center justify-center">
      <AppIcon
        v-if="rightIconName"
        :name="rightIconName"
        :color="color"
        :backgroundColor="backgroundIconColor"
        size="30px"
      />
      <h4
        v-if="text"
        class="text-button"
        :class="{ 'mx-4': leftIconName || rightIconName }"
        :style="{ color }"
      >
        {{ text }}
      </h4>
      <AppIcon
        v-if="leftIconName"
        :name="leftIconName"
        :color="color"
        :backgroundColor="backgroundIconColor"
        size="30px"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  text: String,
  leftIconName: String,
  rightIconName: String,
  color: {
    type: String,
    default: "var(--color-slate-900)",
  },
  backgroundColor: {
    type: String,
    default: "var(--color-blue-400)",
  },
  backgroundIconColor: {
    type: String,
    default: "var(--color-slate-900)",
  },
});

const emits = defineEmits(["onClick"]);
</script>
