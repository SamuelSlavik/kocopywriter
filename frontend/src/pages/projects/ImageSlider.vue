<script setup lang="ts">
import { ref, computed } from 'vue';

const props = defineProps<{
  images: string[];
  initialIndex: number;
}>();

defineEmits(['close']);

const currentIndex = ref(props.initialIndex);

const currentImage = computed(() => props.images[currentIndex.value]);

const next = () => {
  currentIndex.value = (currentIndex.value + 1) % props.images.length;
};

const prev = () => {
  currentIndex.value = (currentIndex.value - 1 + props.images.length) % props.images.length;
};
</script>

<template>
  <div class="image-slider">
    <div class="image-slider__overlay" @click="$emit('close')"></div>
    <button class="image-slider__close" @click="$emit('close')">
      <Close :size="32"/>
    </button>
    <button class="image-slider__nav image-slider__nav--prev" @click="prev">
      <ArrowLeft :size="32"/>
    </button>
    <div class="image-slider__content">
      <img :src="currentImage" alt="Zoomed project image" class="image-slider__image" />
    </div>
    <button class="image-slider__nav image-slider__nav--next" @click="next">
      <ArrowRight :size="32"/>
    </button>
  </div>
</template>

<style scoped>
.image-slider {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 20000;
}

.image-slider__overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  z-index: 20001;
}

.image-slider__content {
  position: relative;
  max-width: calc(100% - 20% - 4rem);
  max-height: 90%;
  z-index: 20002;
}

.image-slider__image {
  max-width: 100%;
  max-height: 90vh;
  object-fit: contain;
}

.image-slider__close,
.image-slider__nav {
  position: absolute;
  background: none;
  border: none;
  color: var(--background);
  font-size: 2rem;
  cursor: pointer;
  z-index: 20003;
  &:hover {
    color: var(--orange);
  }
}

.image-slider__close {
  top: 2rem;
  right: 2rem;
}

.image-slider__nav {
  top: 50%;
  transform: translateY(-50%);
}

.image-slider__nav--prev {
  left: 2rem;
}

.image-slider__nav--next {
  right: 2rem;
}
</style>