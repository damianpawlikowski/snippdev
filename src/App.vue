<template>
  <TheNavbar />
  <main>
    <router-view />
  </main>
  <SignupModal />
  <LoginModal />
  <AccountLostModal />
  <TheFooter />
</template>

<script lang="ts">
import { defineComponent } from "vue";

import TheNavbar from "@/components/TheNavbar.vue";
import SignupModal from "@/components/SignupModal.vue";
import LoginModal from "@/components/LoginModal.vue";
import AccountLostModal from "@/components/AccountLostModal.vue";
import TheFooter from "@/components/TheFooter.vue";

export default defineComponent({
  components: {
    TheNavbar,
    SignupModal,
    LoginModal,
    AccountLostModal,
    TheFooter,
  },
});
</script>
