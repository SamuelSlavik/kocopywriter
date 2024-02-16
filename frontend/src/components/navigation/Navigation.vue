<script setup lang="ts">
import {ref} from "vue";
import {scrollToTarget} from "@/lib/utils";

const displayMenu = ref<boolean>(false)

const toggleMenu = () => {
  displayMenu.value = !displayMenu.value
}

document.addEventListener('DOMContentLoaded', function () {
  const navigationContainer = document.querySelector('.navigation-container');

  window.addEventListener('scroll', function () {
    if (window.scrollY > 0) {
      navigationContainer?.classList.add('scrolled');
    } else {
      navigationContainer?.classList.remove('scrolled');
    }
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const navigationLinks = document.querySelectorAll('.navigation a');

  navigationLinks.forEach(link => {
    link.addEventListener('click', function (event) {
      event.preventDefault();

      const targetId = link.getAttribute('href')?.substring(2); // Remove the '#' from the href
      const targetElement = document.getElementById(targetId || '');

      if (targetElement) {
        const offset = 120; // Set your desired offset
        const targetPosition = targetElement.offsetTop - offset;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  const handleHashChange = function () {
    const targetId = window.location.hash.substring(1);
    if (targetId) {
      scrollToTarget(targetId, 200); // Set your desired offset
    }
  };

  // Handle hash change on page load
  handleHashChange();
});
</script>

<template>
  <div class="navigation-container">
    <div class="navigation-wrapper">
      <div class="logo">
        <router-link to="/#section-homepage" class="logo">
          <div>
            <img alt="Logo" src="@/assets/images/logos/logo.png"/>
            <div>
              <span>Koktající copywriter</span>
              <span>Vojtěch Hulinský</span>
            </div>
          </div>
        </router-link>
        <!--<img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />-->
      </div>

      <div class="navigation">
        <router-link to="/#section-offer">Co nabízím</router-link>
        <router-link to="/#section-about">O mně</router-link>
        <router-link to="/#section-references">Reference</router-link>
        <router-link to="/#section-blog">Blog</router-link>
        <router-link to="/#section-contact">Kokontakt</router-link>
      </div>

      <a class="navigation__icon" :onclick="toggleMenu" v-if="!displayMenu"><MenuIcon :size="32"/></a>
      <a class="navigation__icon" :onclick="toggleMenu" v-if="displayMenu"><Close :size="32"/></a>
    </div>

    <div v-if="displayMenu" class="menu">
      <router-link to="/" :onclick="toggleMenu">Homepage</router-link>
    </div>
  </div>

</template>

<style>
.navigation-container {
  position: fixed;
  width: 100%;
  z-index: 10000;
  transition: all 0.3s ease;
}
.navigation-container.scrolled {
  box-shadow: 0px 1px 2px 0px rgba(0,0,0,0.11);
  background-color: var(--background);
}
.navigation-wrapper {
  width: 100%;
  max-width: var(--breakpoint);
  margin: auto;
  position: relative;
  display: flex;
  height: auto;
  padding: 2rem 1rem;
  justify-content: space-between;
}
.navigation {
  width: auto;
  text-transform: uppercase;
  display: flex;
  gap: 2rem;

  * {
    display: block;
    margin: auto;
    color: var(--secondary);
    letter-spacing: 2px;
  }
  a {
    position: relative;
    &:after {
      content: "";
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      bottom: -0.5rem;
      width: 0; /* Adjust the width of the border */
      border-bottom: 2px solid var(--primary); /* Set the border color and style */
    }

    &:hover:after {
      width: 80%; /* Expand the border to full width on hover */
    }
  }
  a:hover {
    color: var(--primary);
  }
  .active {
    color: var(--primary);
    &:after {
      content: "";
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      bottom: -0.5rem;
      width: 80%; /* Adjust the width of the border */
      border-bottom: 2px solid var(--primary); /* Set the border color and style */
    }
  }

  @media (max-width: 1024px) {
    display: none;
  }
}
.navigation__icon {
  display: none;
  cursor: pointer;

  @media (max-width: 1024px) {
    display: block;
  }
}

.logo {
  > div {
    height: 3rem;
    display: flex;
    gap: 0.5rem;

    > img {
      height: 100%;
      width: auto;
    }
    > div {
      display: flex;
      flex-direction: column;
      justify-content: space-between;

      > span:nth-child(1) {
        font-size: 0.9rem;
        color: var(--secondary);
      }
    }
  }
}
</style>
