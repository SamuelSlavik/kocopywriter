<script setup lang="ts">
import {ref} from "vue";
import {scrollToTarget} from "@/lib/utils";
import {useUserStore} from "@/stores/user-store";

const displayMenu = ref<boolean>(false)
const user = useUserStore()

const toggleMenu: any = () => {
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

      const targetId = link.getAttribute('href')?.substring(2);
      const targetElement = document.getElementById(targetId || '');

      if (targetElement) {
        const offset = 120;
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
      scrollToTarget(targetId, 200);
    }
  };

  handleHashChange();
});

</script>

<template>
  <div class="navigation-container">
    <nav class="navigation">
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
      </div>

      <div class="navigation__content">
        <router-link to="/#section-offer">Služby</router-link>
        <router-link to="/#section-about">O mně</router-link>
        <router-link to="/#section-references">Reference</router-link>
        <router-link to="/#section-blog">Blog</router-link>
        <router-link to="/#section-contact">Kokontakt</router-link>
        <router-link v-if="user.id" to="/admin">Profil</router-link>
      </div>

      <a class="navigation__icon" :onclick="toggleMenu" v-if="!displayMenu"><MenuIcon :size="32"/></a>
      <a class="navigation__icon" :onclick="toggleMenu" v-if="displayMenu"><Close :size="32"/></a>
    </nav>

    <div v-if="displayMenu" class="menu">
      <router-link to="/#section-offer" :onclick="toggleMenu">Služby</router-link>
      <router-link to="/#section-about" :onclick="toggleMenu">O mně</router-link>
      <router-link to="/#section-references" :onclick="toggleMenu">Reference</router-link>
      <router-link to="/#section-blog" :onclick="toggleMenu">Blog</router-link>
      <router-link to="/#section-contact" :onclick="toggleMenu">Kokontakt</router-link>
      <router-link v-if="user.id" to="/admin" :onclick="toggleMenu">Profil</router-link>
    </div>
  </div>

</template>

<style>
.navigation-container {
  position: fixed;
  width: 100%;
  z-index: 10000;
  transition: all 0.3s ease;

  &.scrolled {
    box-shadow: 0px 1px 2px 0px rgba(0,0,0,0.11);
    background-color: var(--background);
  }

  nav {
    width: 100%;
    max-width: var(--breakpoint);
    margin: auto;
    position: relative;
    display: flex;
    height: auto;
    padding: 2rem 1rem;
    justify-content: space-between;

    .navigation__content {
      width: auto;
      text-transform: uppercase;
      display: flex;
      gap: 2rem;
      font-size: 0.9rem;

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
          width: 0;
          border-bottom: 2px solid var(--primary);
        }

        &:hover:after {
          width: 80%;
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
          width: 80%;
          border-bottom: 2px solid var(--primary);
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
        line-height: normal;

        > span:nth-child(1) {
          color: var(--secondary);
        }
        > span:nth-child(2) {
          color: var(--primary);
        }
      }
    }
  }

  .menu {
    width: auto;
    position: absolute;
    right: 1rem;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    text-align: right;
    gap: 1rem;
    background-color: var(--background);
    border: 1px solid rgba(60, 60, 67, 0.12);
    box-shadow: rgba(0, 0, 0, 0.1) 0px 12px 32px 0px, rgba(0, 0, 0, 0.08) 0px 2px 6px 0px;

    a {
      width: auto;
      color: var(--primary);
    }
  }
}


</style>
