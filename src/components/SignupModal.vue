<template>
  <VModal id="signupModal">
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
      <p class="lead">Signing up is super quick. Please, do not hesitate.</p>
    </template>
    <template v-slot:body>
      <form @submit.prevent="handleSubmit">
        <div class="form-floating mb-3">
          <input
            type="email"
            class="form-control"
            id="email"
            placeholder="E-mail"
            v-model="credentials.email"
          />
          <label for="email">E-mail</label>
        </div>
        <div class="form-floating mb-3">
          <input
            type="password"
            class="form-control"
            id="password"
            placeholder="Password"
            v-model="credentials.password"
          />
          <label for="password">Password</label>
        </div>
        <div class="form-floating mb-3">
          <input
            type="password"
            class="form-control"
            id="repeatPassword"
            placeholder="Repeat password"
          />
          <label for="repeatPassword">Repeat password</label>
        </div>
        <div class="mb-3">
          <span>
            <i class="fa-solid fa-circle-info"></i>
            <span class="small">
              By signing up, you agree to our
              <a href="#" class="link-dark text-decoration-underline">
                Terms and Rules</a
              >
              and
              <a href="#" class="link-dark text-decoration-underline"
                >Privacy Policy</a
              >.
            </span>
          </span>
        </div>
        <button class="btn btn-primary w-100 btn-lg fw-bold">
          <i class="fa-solid fa-user-plus me-1"></i>
          <span>Sign up</span>
        </button>
      </form>
    </template>
    <template v-slot:footer>
      <button class="btn" type="button" @click="switchToLoginModal">
        <i class="fa-solid fa-arrow-right-to-bracket me-1"></i>
        <span>Log in</span>
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
import { reactive } from "vue";

import VModal from "@/components/VModal.vue";
import useSignupUser from "@/composables/signupUser";

export default defineComponent({
  components: {
    VModal,
  },
  setup() {
    const hideSignupModal = () => {
      const signupModal: Modal | null = Modal.getInstance(
        document.getElementById("signupModal") as Element
      );

      if (signupModal !== null) {
        signupModal.hide();
      }
    };

    const switchToLoginModal = () => {
      hideSignupModal();
      const loginModal: Modal = Modal.getOrCreateInstance(
        document.getElementById("loginModal") as Element
      );

      if (loginModal !== null) {
        loginModal.show();
      }
    };

    const switchToAccountLostModal = () => {
      hideSignupModal();
      const accountLostModal: Modal = Modal.getOrCreateInstance(
        document.getElementById("accountLostModal") as Element
      );

      if (accountLostModal !== null) {
        accountLostModal.show();
      }
    };

    const credentials = reactive({
      email: "",
      password: "",
    });

    const handleSubmit = () => {
      useSignupUser()
        .signupUser(credentials)
        .then(() => {
          hideSignupModal();
        });
    };

    return {
      switchToLoginModal,
      switchToAccountLostModal,
      credentials,
      handleSubmit,
    };
  },
});
</script>
