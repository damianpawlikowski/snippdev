<template>
  <nav class="navbar navbar-expand-lg navbar-light border-bottom">
    <div class="container">
      <a href="#" class="navbar-brand fs-3">
        <i class="fa-solid fa-code"></i>
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a href="#" class="nav-link">Create snippet</a>
          </li>
          <li class="nav-item dropdown">
            <a
              href="#"
              class="nav-link dropdown-toggle"
              id="helpDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Help
            </a>
            <ul class="dropdown-menu" aria-labelledby="helpDropdown">
              <li><a href="#" class="dropdown-item">Contact</a></li>
              <li><a href="#" class="dropdown-item">Terms and Rules</a></li>
              <li><a href="#" class="dropdown-item">Privacy Policy</a></li>
            </ul>
          </li>
        </ul>
        <div class="d-flex">
          <button
            class="btn btn-primary me-3 fw-bold"
            type="button"
            data-bs-toggle="modal"
            data-bs-target="#signupModal"
          >
            <i class="fa-solid fa-user-plus me-1"></i>
            <span>Sign up</span>
          </button>
          <button
            class="btn btn-light me-3"
            type="button"
            data-bs-toggle="modal"
            data-bs-target="#loginModal"
          >
            <i class="fa-solid fa-arrow-right-to-bracket me-1"></i>
            <span>Log in</span>
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>
