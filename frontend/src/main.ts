import { createApp } from 'vue'
import { createPinia } from 'pinia'

// @ts-ignore
import Notifications from "notification-quark"
import "notification-quark/dist/style.css"

import App from './App.vue'
import router from './router'
import Container from "@/components/Container.vue";
import Navigation from "@/components/navigation/Navigation.vue";
import Footer from "@/components/footer/Footer.vue";
import Loader from "@/components/loader/Loader.vue";

// ICONS
// @ts-ignore
import MenuIcon from 'vue-material-design-icons/Menu.vue';
// @ts-ignore
import Close from 'vue-material-design-icons/Close.vue';
// @ts-ignore
import LinkedIn from 'vue-material-design-icons/Linkedin.vue';
import axios from "axios";


const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Notifications)

app.component("Loader", Loader)

app.component("Container", Container)
app.component("Navigation", Navigation)
app.component("Footer", Footer)

// Icons
app.component("MenuIcon", MenuIcon)
app.component("Close", Close)
app.component("LinkedIn", LinkedIn)

app.mount('#app')

axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    // If the response status is 401 (Unauthorized), navigate to the login page
    if (error.response.status === 401) {
      await router.push('/login');
    }
    return Promise.reject(error);
  }
);