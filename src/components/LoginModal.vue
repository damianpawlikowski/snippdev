<template>
  <VModal id="loginModal">
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
            id="loginEmail"
            placeholder="E-mail"
          />
          <label for="loginEmail">E-mail</label>
        </div>
        <div class="form-floating mb-3">
          <input
            type="password"
            class="form-control"
            id="loginPassword"
            placeholder="Password"
          />
          <label for="loginPassword">Password</label>
        </div>
        <button class="btn btn-primary w-100 btn-lg fw-bold">
          <i class="fa-solid fa-arrow-right-to-bracket me-1"></i>
          <span>Log in</span>
        </button>
      </form>
    </template>
    <template v-slot:footer>
      <button class="btn" type="button" @click="switchToSignupModal">
        <i class="fa-solid fa-user-plus me-1"></i>
        <span>Sign up</span>
      </button>
      <button class="btn" type="button" @click="switchToAccountLostModal">
        <i class="fa-solid fa-circle-question me-1"></i>
        <span>Account lost</span>
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
    const hideLoginModal = () => {
      const loginModal: Modal | null = Modal.getInstance(
        document.getElementById("loginModal") as Element
      );

      if (loginModal !== null) {
        loginModal.hide();
      }
    };

    const switchToSignupModal = () => {
      hideLoginModal();
      const signupModal: Modal = Modal.getOrCreateInstance(
        document.getElementById("signupModal") as Element
      );

      if (signupModal !== null) {
        signupModal.show();
      }
    };

    const switchToAccountLostModal = () => {
      hideLoginModal();
      const accountLostModal: Modal = Modal.getOrCreateInstance(
        document.getElementById("accountLostModal") as Element
      );

      if (accountLostModal !== null) {
        accountLostModal.show();
      }
    };

    return { switchToSignupModal, switchToAccountLostModal };
  },
});
</script>
