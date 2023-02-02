<script>
	import '$lib/app.scss';
  import logo from '$lib/assets/logo.png';

  let navbarActive = false;
  const toggleNavbar = () => {navbarActive = !navbarActive};
</script>

<nav class="navbar is-light" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="/">
      <img src={logo} width="28" height="28" alt="GameFinder logo">
      GameFinder
    </a>

    <button class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" class:is-active={navbarActive} on:click={toggleNavbar}>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </button>
  </div>

  <div id="navbarBasicExample" class="navbar-menu" class:is-active={navbarActive}>
    <div class="navbar-start">
      <a class="navbar-item">
        Documentation
      </a>

      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          More
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            About
          </a>
          <a class="navbar-item">
            Jobs
          </a>
          <a class="navbar-item">
            Contact
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item">
            Report an issue
          </a>
        </div>
      </div>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-primary">
            <strong>Sign up</strong>
          </a>
          <a class="button is-light">
            Log in
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>

<section class="section">
  <div class="container">
    <slot />
  </div>
</section>
