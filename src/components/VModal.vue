<template>
  <div class="modal" :id="id" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header flex-column">
          <slot name="header"></slot>
        </div>
        <div class="modal-body">
          <slot name="body"></slot>
        </div>
        <div class="modal-footer">
          <slot name="footer"></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    id: {
      type: String,
      required: true,
    },
  },
});
</script>
