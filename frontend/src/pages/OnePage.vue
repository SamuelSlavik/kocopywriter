<script setup lang="ts">
import Homepage from "@/pages/sections/Homepage.vue";
import Offer from "@/pages/sections/Offer.vue";
import About from "@/pages/sections/About.vue";
import BlogSection from "@/pages/sections/BlogSection.vue";
import References from "@/pages/sections/References.vue";
import Contact from "@/pages/sections/Contact.vue";
import BrandsSection from "@/pages/sections/BrandsSection.vue";

</script>

<template>
  <KeepAlive>
    <Homepage />
  </KeepAlive>
  <KeepAlive>
    <BrandsSection />
  </KeepAlive>
  <KeepAlive>
    <Offer />
  </KeepAlive>
  <KeepAlive>
    <About />
  </KeepAlive>
  <KeepAlive>
    <References />
  </KeepAlive>
  <KeepAlive>
    <BlogSection />
  </KeepAlive>
  <Contact />
</template>

<style>

</style>