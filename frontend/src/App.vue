<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import {inject, onMounted, ref} from "vue";
import {useUserStore} from "@/stores/user-store";
import axios from "axios";
import type {User} from "@/lib/models";
import {Endpoints} from "@/lib/endpoints";

const loading = ref<boolean>(false)
const user = useUserStore()
const notificationStore: any = inject('notificationStore')

const checkUser = async () => {
  try {
    loading.value = true

    const response = await axios.get<User>(
        Endpoints.retrieveCurrentUser,
        {headers: {Authorization: `Bearer ${localStorage.getItem("token") || ""}`}}
    )
    if (response.status === 200) {
      user.setUserData(response.data)
    }
  } catch (error) {
    console.log(error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  checkUser()
})

document.addEventListener('DOMContentLoaded', function () {
  const navigationLinks = document.querySelectorAll('.navigation a');

  function toggleActiveLink() {
    const scrollPosition = window.scrollY;

    navigationLinks.forEach((link) => {
      const targetId = link.getAttribute('href')?.substring(2); // Remove the '#' from the href
      const targetElement = document.getElementById(targetId || '')

      console.log(targetId);

      if (
          targetElement &&
          scrollPosition >= targetElement.offsetTop - window.innerHeight / 2 &&
          scrollPosition < targetElement.offsetTop + targetElement.offsetHeight - window.innerHeight / 2
      ) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }

      const navigationContainer = document.querySelector('.navigation-container');
      if (window.scrollY > 0) {
        navigationContainer?.classList.add('scrolled');
      } else {
        navigationContainer?.classList.remove('scrolled');
      }
    });
  }

  window.addEventListener('scroll', toggleActiveLink);
  toggleActiveLink(); // Initial check on page load
});

</script>

<template>
  <Navigation/>
  <RouterView />
  <Footer />

  <Notifications />
</template>

<style>
:root {
  --orange: rgb(209, 119, 61);
  --primary: rgb(85, 85, 85);
  --secondary: rgba(85, 85, 85, 0.8);
  --tertiary: rgba(85, 85, 85, 0.2);
  --background: rgb(255, 255, 255);
  --secondary-background: rgb(0, 0, 0);
  --breakpoint: 1200px;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  transition: all 0.5s ease;
  scroll-behavior: smooth;
}
body {
  min-height: 100vh;
  color: rgb(85, 85, 85);
  background-color: white;
  font-family: "Open Sans", sans-serif;
  scroll-behavior: smooth;
  line-height: 2rem;
}
a {
  text-decoration: none;
  color: var(--orange);
}
.active {
  color: var(--primary);
}
svg, i {
  color: var(--primary) !important;
}
.button {
  display: block;
  padding: 0.7rem 1.3rem;
  box-shadow: 5px 5px 0px 0px rgba(0,0,0,0.08);
  border: 1px solid var(--primary);
  background-color: var(--background);
  text-transform: uppercase;
  width: fit-content;
  color: var(--secondary);
  letter-spacing: 2px;

  &:hover {
    background-color: var(--secondary-background);
    cursor: pointer;
    box-shadow: -5px -5px 0px 0px rgba(0,0,0,0.08);
  }
}
h2 {
  font-family: "Times New Roman ", serif;
  font-size: 2rem;
  font-weight: normal;
}
h3 {
  font-family: "Times New Roman ", serif;
  font-size: 1.5rem;
  font-weight: normal;
}
p {
  color: var(--secondary);
}
</style>
