<script setup lang="ts">
import { ref, computed } from 'vue';

const props = defineProps<{
  images: string[];
  initialIndex: number;
}>();

const isOpen = ref(true);
const currentIndex = ref(props.initialIndex);

const currentImage = computed(() => props.images[currentIndex.value]);

const close = () => {
  isOpen.value = false;
};

const next = () => {
  currentIndex.value = (currentIndex.value + 1) % props.images.length;
};

const prev = () => {
  currentIndex.value = (currentIndex.value - 1 + props.images.length) % props.images.length;
};
</script>

<template>
  <div v-if="isOpen" class="image-slider">
    <div class="image-slider__overlay" @click="close"></div>
    <div class="image-slider__content">
      <button class="image-slider__close" @click="close">&times;</button>
      <button class="image-slider__nav image-slider__nav--prev" @click="prev">&lt;</button>
      <img :src="currentImage" alt="Zoomed project image" class="image-slider__image" />
      <button class="image-slider__nav image-slider__nav--next" @click="next">&gt;</button>
    </div>
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
  z-index: 1000;
}

.image-slider__overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
}

.image-slider__content {
  position: relative;
  max-width: 90%;
  max-height: 90%;
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
  color: white;
  font-size: 2rem;
  cursor: pointer;
}

.image-slider__close {
  top: 10px;
  right: 10px;
}

.image-slider__nav {
  top: 50%;
  transform: translateY(-50%);
}

.image-slider__nav--prev {
  left: 10px;
}

.image-slider__nav--next {
  right: 10px;
}
</style>