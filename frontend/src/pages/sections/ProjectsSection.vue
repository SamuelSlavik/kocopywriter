<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue';
import {EffectCoverflow, Navigation} from "swiper/modules";
import 'swiper/css';
import 'swiper/css/effect-coverflow';
import 'swiper/css/pagination';

import softli from '@/assets/images/projectLogos/softli.png'
import krstatic from '@/assets/images/projectLogos/KRStatic.jpg'
import ablado from '@/assets/images/projectLogos/ablado.png'
import accelapps from '@/assets/images/projectLogos/accelapps.jpg'
import zahradyGreen from '@/assets/images/projectLogos/zahrady-green.png'
import realmstav from '@/assets/images/projectLogos/realmstav.png'
import domyKrizkovyUjezdec from '@/assets/images/projectLogos/domy-krizkovy-ujezdec.png'
import meopta from '@/assets/images/projectLogos/Meopta.jpg'

const modules = [ Navigation, EffectCoverflow ];

const data = [
  {
    id: 0,
    name: 'SoftLi',
    segment: 'Tech SaaS | B2B',
    logo: softli,
    pdf: ''
  },
  {
    id: 1,
    name: 'KRStatic',
    segment: 'Civil Engineering | B2B',
    logo: krstatic,
    pdf: ''
  },
  {
    id: 2,
    name: 'Ablado',
    segment: 'Edu | B2C',
    logo: ablado,
    pdf: ''
  },
  {
    id: 3,
    name: 'Accelapps',
    segment: 'Business IT | B2B',
    logo: accelapps,
    pdf: ''
  },
  {
    id: 4,
    name: 'Záhrady Green',
    segment: 'Landscape Architecture | B2C',
    logo: zahradyGreen,
    pdf: ''
  },
  {
    id: 5,
    name: 'REALMstav',
    segment: 'Real Estate | B2C/B2B',
    logo: realmstav,
    pdf: ''
  },
  {
    id: 6,
    name: 'Domy Křížkový Újezdec',
    segment: 'Real Estate | B2C',
    logo: domyKrizkovyUjezdec,
    pdf: ''
  },
  {
    id: 7,
    name: 'Meopta',
    segment: 'High-Tech | B2B',
    logo: meopta,
    pdf: ''
  },
]

</script>

<template>
  <div class="section-projects" id="section-offer">
    <Container>
      <swiper
        :modules="modules"
        :loop="true"
        :grabCursor="true"
        :centeredSlides="true"
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
          768: {
            slidesPerView: 2,
          },
          1024: {
            slidesPerView: 3,
          },
        }"
      >
        <swiper-slide v-for="project in data" class="section-projects__slide" :key="project.id">
          <div  class="section-projects__slide-content">
            <div class="section-projects__image-container">
              <img :src="project.logo" :alt="project.name" />
            </div>
            <div class="section-projects__slide-text">
              <h2>{{project.name}}</h2>
              <p>{{project.segment}}</p>
            </div>
          </div>
        </swiper-slide>
      </swiper>
    </Container>
  </div>
</template>

<style>
.section-projects {
  padding: 5rem;

  .section-projects__slide-content {
    width: 80%;
    margin: auto;
    height: auto;
    text-align: center;
    padding: 2rem 2rem;
    background-color: var(--background-light);
    border-radius: 10px;
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
    }
  }

  .section-projects__slide-text {
    margin-top: 2rem;
  }
}
</style>