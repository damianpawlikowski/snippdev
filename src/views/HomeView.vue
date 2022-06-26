<template>
  <div class="container">
    <div class="row">
      <div class="col-12 col-lg-7">
        <section class="py-5 px-4">
          <h1 class="display-5">
            <i class="fa-solid fa-code me-1"></i>
            <span class="fw-light">Snippdev</span>
          </h1>
          <p class="lead">Create your code snippet now, quickly and free.</p>
          <CreateSnippetForm />
        </section>
      </div>
      <div class="col-12 col-lg-5"></div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import CreateSnippetForm from "@/components/CreateSnippetForm.vue";

export default defineComponent({
  components: {
    CreateSnippetForm,
  },
});
</script>
