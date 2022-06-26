<template>
  <VModal id="accountLostModal">
    <template v-slot:header>
      <button
        class="btn-close"
        type="button"
        data-bs-dismiss="modal"
        aria-label="Close"
      ></button>
      <div class="d-flex align-items-center fs-1">
        <i class="fa-solid fa-code me-1"></i>
        <span class="fw-light">Snippdev</span>
      </div>
      <p class="lead">From developer for developers.</p>
    </template>
    <template v-slot:body>
      <form>
        <div class="form-floating mb-3">
          <input
            type="email"
            class="form-control"
            id="accountLostEmail"
            placeholder="E-mail"
          />
          <label for="accountLostEmail">E-mail</label>
        </div>
        <div class="mb-3">
          <i class="fa-solid fa-circle-info"></i>
          <span class="small">
            We will send you a message with a recovery link.
          </span>
        </div>
        <button class="btn btn-primary w-100 btn-lg fw-bold">
          <i class="fa-solid fa-arrow-up-right-from-square me-1"></i>
          <span>Send</span>
        </button>
      </form>
    </template>
    <template v-slot:footer>
      <button class="btn" type="button" @click="switchToLoginModal">
        <i class="fa-solid fa-arrow-right-to-bracket me-1"></i>
        <span>Log in</span>
      </button>
      <button class="btn" type="button" @click="switchToSignupModal">
        <i class="fa-solid fa-user-plus me-1"></i>
        <span>Sign up</span>
      </button>
    </template>
  </VModal>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Modal } from "bootstrap";

import VModal from "@/components/VModal.vue";

export default defineComponent({
  components: {
    VModal,
  },
  setup() {
    const hideAccountLostModal = () => {
      const accountLostModal: Modal | null = Modal.getInstance(
        document.getElementById("accountLostModal") as Element
      );

      if (accountLostModal !== null) {
        accountLostModal.hide();
      }
    };

    const switchToLoginModal = () => {
      hideAccountLostModal();
      const loginModal: Modal = Modal.getOrCreateInstance(
        document.getElementById("loginModal") as Element
      );

      if (loginModal !== null) {
        loginModal.show();
      }
    };

    const switchToSignupModal = () => {
      hideAccountLostModal();
      const signupModal: Modal = Modal.getOrCreateInstance(
        document.getElementById("signupModal") as Element
      );

      if (signupModal !== null) {
        signupModal.show();
      }
    };

    return { switchToLoginModal, switchToSignupModal };
  },
});
</script>
