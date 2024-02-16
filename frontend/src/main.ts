import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import Container from "@/components/Container.vue";
import Navigation from "@/components/navigation/Navigation.vue";
import Footer from "@/components/footer/Footer.vue";

// ICONS
// @ts-ignore
import MenuIcon from 'vue-material-design-icons/Menu.vue';
// @ts-ignore
import Close from 'vue-material-design-icons/Close.vue';
// @ts-ignore
import LinkedIn from 'vue-material-design-icons/Linkedin.vue';


const app = createApp(App)

app.use(createPinia())
app.use(router)

app.component("Container", Container)
app.component("Navigation", Navigation)
app.component("Footer", Footer)

// Icons
app.component("MenuIcon", MenuIcon)
app.component("Close", Close)
app.component("LinkedIn", LinkedIn)

app.mount('#app')
