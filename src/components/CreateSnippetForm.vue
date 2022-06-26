<template>
  <form>
    <div class="form-floating mb-3">
      <input
        type="text"
        class="form-control"
        id="snippetTitle"
        placeholder="Title"
      />
      <label for="snippetTitle">Title</label>
    </div>
    <div class="form-floating mb-3">
      <textarea
        class="form-control"
        style="height: 100%"
        id="snippetBody"
        rows="15"
        placeholder="Body"
      ></textarea>
      <label for="snippetBody">Body</label>
    </div>
    <button class="btn btn-primary w-100 btn-lg fw-bold">
      <span>Create snippet</span>
    </button>
  </form>
</template>
