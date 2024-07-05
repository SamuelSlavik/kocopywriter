<script setup lang="ts">
import {inject, ref} from "vue";

const notificationStore: any = inject('notificationStore')
const name = ref<string>("");
const email = ref<string>("");
const message = ref<string>("");
const captcha = ref<string>("42"); // INPUT FOR CAPTCHA TEMPORARILY HIDDEN

const submitForm = async () => {
  if (captcha.value !== "42" || !name.value || !email.value || !message.value) {
    notificationStore.addNotification({type: "error", message: "Please fill in all fields."});
    return;
  }
  try {
    const response = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        access_key: "912b2c5d-9ef9-4142-a482-acb6be43a720",
        from_name: `${name.value} (kocopywriter.cz)`,
        subject: "New message from kocopywriter.cz",
        name: name.value,
        email: email.value,
        message: message.value,
      }),
    });
    const result = await response.json();
    if (result.success) {
      notificationStore.addNotification({type: "success", message: "Message sent successfully."});
      name.value = "";
      email.value = "";
      message.value = "";
      captcha.value = "42"; // INPUT FOR CAPTCHA TEMPORARILY HIDDEN
    }
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to send message: " + error.response.data.detail});
  }
};

</script>

<template>
  <div class="contact-background" id="section-contact">
    <!--<img src="@/assets/images/wallpapers/contact-background.jpeg" class="contact-background"/>-->
    <Container
        class="section-contact"
    >
      <!--style="background-image: url('src/assets/images/logos/logo.png')"-->
      <div class="section-contact__content">
        <div class="section-contact__text">
          <h2>
            Chcete originální prodejní texty,<br/>
            než řeknu š-š-švec?
          </h2>
          <p>Napište mi.</p>
        </div>
        <div class="section-contact__form">
          <form @submit.prevent="submitForm">
            <input
              type="text"
              name="name"
              placeholder="Vaše jméno?"
              v-model="name"
            />
            <input
              type="email"
              name="email"
              placeholder="Váš e-mail?"
              v-model="email"
            />
            <textarea
              name="message"
              placeholder="Vaše přání?"
              v-model="message"
            ></textarea>
            <!--
            <input
              type="text"
              name="captcha"
              id="captcha"
              v-model="captcha"
              placeholder="27+15 = ?"
            />
            -->
            <button class="button" type="submit">Odeslat zprávu</button>
          </form>
        </div>
      </div>
      <!--
      <div class="section-contact__background">
        <img src="../../assets/images/logos/logo.png" alt="Logo" />
      </div>
      -->
      <!--
      <div class="contact-wallpaper">
        <img src="../../assets/images/wallpapers/w-4.jpg" alt="Logo" />
      </div>
      -->
    </Container>
  </div>
</template>

<style>
.contact-background {
  position: relative;
  width: 100%;
  height: 100%;
}
.contact-background::before {
  content: "";
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/images/wallpapers/contact-background.jpeg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  opacity: 0.1;
}
.section-contact {
  overflow-x: hidden;
}
.section-contact__background {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-30%, -50%);
  z-index: -1;
  opacity: 0.1;

}
.section-contact__content {
  display: flex;
  min-height: 100vh;
  height: auto;
  gap: 2rem;
  width: 100%;
  margin-left: 0;
  text-align: left;
  justify-content: space-between;
  margin-bottom: 0;
  flex-wrap: wrap;

  .section-contact__text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 40%;
    @media (max-width: 1024px) {
      width: 100%;
    }
  }
  .section-contact__form {
    width: 50%;
    margin: auto;
    @media (max-width: 1024px) {
      width: 100%;
      margin: 0;
    }
  }
}
.contact-wallpaper {
  img {
    width: 100%;
    left: 25%;
    height: auto;
    position: absolute;
    z-index: -1;
    top: 50%;
    transform: translateY(-50%);
  }
}
</style>