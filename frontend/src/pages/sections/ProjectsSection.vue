<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue';
import {EffectCoverflow, Navigation} from "swiper/modules";
import 'swiper/css';
import 'swiper/css/effect-coverflow';
import 'swiper/css/pagination';
import { ref } from 'vue'
import VuePdfEmbed from 'vue-pdf-embed'

import softli from '@/assets/images/projectLogos/softli.svg'
import krstatic from '@/assets/images/projectLogos/KRStatic.jpg'
import ablado from '@/assets/images/projectLogos/ablado.png'
import accelapps from '@/assets/images/projectLogos/accelapps.png'
import zahradyGreen from '@/assets/images/projectLogos/zahrady-green.svg'
import realmstav from '@/assets/images/projectLogos/realmstav.png'
import domyKrizkovyUjezdec from '@/assets/images/projectLogos/domy-krizkovy-ujezdec.png'
import meopta from '@/assets/images/projectLogos/meopta.png'

import softliPdf from '@/assets/pdfs/projectPdfs/softli.pdf'
import krstaticPdf from '@/assets/pdfs/projectPdfs/KRStatic.pdf'
import abladoPdf from '@/assets/pdfs/projectPdfs/ablado.pdf'
import accelappsPdf from '@/assets/pdfs/projectPdfs/accelapps.pdf'
import zahradyGreenPdf from '@/assets/pdfs/projectPdfs/zahrady-green.pdf'
import realmstavPdf from '@/assets/pdfs/projectPdfs/REALMstav.pdf'
import domyKrizkovyUjezdecPdf from '@/assets/pdfs/projectPdfs/domy-krizkovy-ujezdec.pdf'
import meoptaPdf from '@/assets/pdfs/projectPdfs/Meopta.pdf'

const modules = [ Navigation, EffectCoverflow ];

const data = [
  {
    id: 0,
    name: 'SoftLi',
    segment: 'Tech SaaS | B2B',
    logo: softli,
    pdf: softliPdf
  },
  {
    id: 1,
    name: 'Ablado',
    segment: 'Edu | B2C',
    logo: ablado,
    pdf: abladoPdf
  },
  {
    id: 2,
    name: 'Accelapps',
    segment: 'Business IT | B2B',
    logo: accelapps,
    pdf: accelappsPdf
  },
  {
    id: 3,
    name: 'Zahrady Green',
    segment: 'Landscape Architecture | B2C',
    logo: zahradyGreen,
    pdf: zahradyGreenPdf
  },
  {
    id: 4,
    name: 'REALMstav',
    segment: 'Real Estate | B2C/B2B',
    logo: realmstav,
    pdf: realmstavPdf
  },
  {
    id: 5,
    name: 'Domy Křížkový Újezdec',
    segment: 'Real Estate | B2C',
    logo: domyKrizkovyUjezdec,
    pdf: domyKrizkovyUjezdecPdf
  },
  {
    id: 6,
    name: 'Meopta',
    segment: 'High-Tech | B2B',
    logo: meopta,
    pdf: meoptaPdf
  },
  {
    id: 7,
    name: 'KRStatic',
    segment: 'Civil Engineering | B2B',
    logo: krstatic,
    pdf: krstaticPdf
  },
]

const selectedPdf = ref<string | null>(null)

const openModal = (pdf: string) => {
  selectedPdf.value = pdf
}

const closeModal = () => {
  selectedPdf.value = null
}

</script>

<template>
  <div class="section-projects" id="section-projects">
    <h2 class="section-projects__heading">Takhle vypadá účelná jinakost u klientů</h2>
    <Container>
      <swiper
        :modules="modules"
        :loop="true"
        :grabCursor="false"
        :centeredSlides="true"
        :navigation="true"
        :effect="'coverflow'"
        :coverflowEffect="{
          rotate: 0,
          stretch: 0,
          depth: 100,
          modifier: 4,
          slideShadows: true,
        }"
        :breakpoints="{
          640: {
            slidesPerView: 1,
          },
          1024: {
            slidesPerView: 3,
          },
        }"
      >
        <swiper-slide v-for="project in data" class="section-projects__slide" :key="project.id">
          <div @click="openModal(project.pdf)"  class="section-projects__slide-content">
            <div class="section-projects__image-container">
              <img :src="project.logo" :alt="project.name" />
            </div>
            <div class="section-projects__slide-text">
              <h2>{{project.name}}</h2>
              <p>{{project.segment}}</p>
            </div>
            <span class="section-projects__slide-arrow" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="m256-240-56-56 384-384H240v-80h480v480h-80v-344L256-240Z"/></svg>
            </span>
          </div>
        </swiper-slide>
      </swiper>
      <transition name="modal-fade">
        <div v-if="selectedPdf" class="modal-overlay" @click.self="closeModal">
          <div class="modal-content">
            <button class="modal-close" @click="closeModal">✕</button>
            <VuePdfEmbed
                v-if="selectedPdf"
                :source="selectedPdf"
                class="pdf-viewer"
            />
          </div>
        </div>
      </transition>
    </Container>
  </div>
</template>

<style>
.section-projects {
  padding: 10rem 5rem 15rem 5rem;

  @media (max-width: 640px) {
    padding: 5rem 0 5rem 0;
  }

  .section-projects__heading {
    text-align: center;
    margin-bottom: 3rem;

    @media (max-width: 1024px) {
      font-size: 1.7rem;
      margin-bottom: 0;
      padding: 0 1rem;
    }
  }

  .section-projects__slide-content {
    width: 80%;
    margin: auto;
    height: auto;
    text-align: center;
    padding: 2rem 2rem;
    background-color: var(--background);
    border-radius: 10px;
    cursor: pointer;

    @media (max-width: 1024px) {
      width: 60%;
    }
  }

  .section-projects__image-container {
    width: 100%;
    height: 200px;

    display: flex;
    justify-content: center;
    align-items: center;

    img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      filter: brightness(80%);
    }
  }

  .section-projects__slide-text {
    margin-top: 2rem;
  }

  .section-projects__slide-arrow {
    display: inline-block;
    margin-top: 1rem;
    color: var(--tertiary);
    transition: color 0.25s ease, transform 0.25s ease;

    svg {
      fill: var(--tertiary);
    }

    @media (max-width: 640px) {
      svg {
        fill: var(--orange);
      }
    }
  }

  .swiper,
  .swiper-wrapper {
    pointer-events: none;
  }

  .swiper-wrapper {
    width: calc(100% - 60px);
  }

  .swiper-slide,
  .swiper-button-prev,
  .swiper-button-next,
  .section-projects__slide-content {
    pointer-events: auto;
  }

  .swiper-button-prev,
  .swiper-button-next {
    z-index: 10;
    background-color: var(--background);
    height: 100%;
    top: 0 !important;
    width: fit-content;
  }

  .swiper-button-prev {
    left: 0 !important;
    padding-right: 1rem;
  }

  .swiper-button-next {
    right: 0 !important;
    padding-left: 1rem;
  }

  .swiper-slide:not(.swiper-slide-active) .section-projects__slide-content {
    opacity: 0.72;
    filter: brightness(0.85);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.18);
  }

  .swiper-slide.swiper-slide-active .section-projects__slide-content {
    &:hover .section-projects__slide-arrow {
      color: var(--orange);
      transform: translate(2px, -2px);

      svg {
        fill: var(--orange);
      }
    }

    &:hover img {
      filter: none;
    }
  }

  .swiper-slide-active .section-projects__slide-content {
    opacity: 1;
    filter: brightness(1);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
  }

  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 99999;
  }

  .modal-content {
    width: 80%;
    height: 80%;
    background: white;
    border-radius: 10px;
    overflow: auto;
    position: relative;
  }

  .modal-close {
    position: absolute;
    top: 10px;
    right: 15px;
    font-size: 2rem;
    background: none;
    border: none;
    cursor: pointer;
    z-index: 10;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity 0.35s ease;
  }

  .modal-fade-enter-from,
  .modal-fade-leave-to {
    opacity: 0;
  }

  /* Content scale animation */
  .modal-fade-enter-active .modal-content,
  .modal-fade-leave-active .modal-content {
    transition: transform 0.35s ease, opacity 0.35s ease;
  }

  .modal-fade-enter-from .modal-content {
    transform: scale(0.85);
    opacity: 0;
  }

  .modal-fade-leave-to .modal-content {
    transform: scale(0.85);
    opacity: 0;
  }
}
</style>