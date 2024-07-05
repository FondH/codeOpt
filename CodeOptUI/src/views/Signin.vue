<script setup>
import { onBeforeUnmount, onBeforeMount } from "vue";
import { useStore } from "vuex";
import Navbar from "@/examples/PageLayout/Navbar.vue";
import ArgonInput from "@/components/ArgonInput.vue";
import ArgonSwitch from "@/components/ArgonSwitch.vue";
import ArgonButton from "@/components/ArgonButton.vue";

// import {login} from "@/apis"
const body = document.getElementsByTagName("body")[0];

const store = useStore();
onBeforeMount(() => {
  store.state.hideConfigButton = true;
  store.state.showNavbar = false;
  store.state.showSidenav = false;
  store.state.showFooter = false;
  body.classList.remove("bg-gray-100");
});
onBeforeUnmount(() => {
  store.state.hideConfigButton = false;
  store.state.showNavbar = true;
  store.state.showSidenav = true;
  store.state.showFooter = true;
  body.classList.add("bg-gray-100");
});
</script>
<script>
import ArgonAlert from "@/components/ArgonAlert.vue";
export default{
  data () {
    return {
      username: '',
      password: '',
      re_password: '',
      showError: false,
      success: false,
      errorMessage: '',
    }
  },
  methods:{
    doLogin (event) {
      event.preventDefault();
      console.log("login!!",this.username, this.password)

      this.$store.dispatch('toLogin', {
        loginUser: this.username,
        loginPassword: this.password
      }).then(() => {
        //this.$store.dispatch('getUser')
        this.success = true;
        console.log("Jump to main-page")
        setTimeout(() => {
            this.success = false;
            this.$router.push("/main-page")

        }, 1000);   
      }).catch((error) => {
          console.log("errorr",error);
          this.errorMessage = error.data.msg || 'An error occurred';
          this.showError = true;
          setTimeout(() => {
            this.showError = false;
          }, 3000); // Hide after 3 seconds
        }).catch((error) => {
          console.log(error);
        });
        
    },

  }
}
</script>
<template>
  <div class="container top-0 position-sticky z-index-sticky">
    <div class="row">
      <div class="col-12">
        <navbar
          isBlur="blur  border-radius-lg my-3 py-2 start-0 end-0 mx-4 shadow"
          v-bind:darkMode="true"
          isBtn="bg-gradient-success"
        />
      </div>
    </div>
  </div>
  <main class="mt-0 main-content">
    <section>
      <div class="page-header min-vh-100">
        <div class="container">
          <div class="row">
            <div
              class="mx-auto col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0"
            >
              <div class="card card-plain">
                <div class="pb-0 card-header text-start">
                  <h4 class="font-weight-bolder">Sign In</h4>
                  <p class="mb-0">Enter your email and password to sign in</p>
                </div>
                <div class="card-body">
                  <form role="form">
                    <div class="mb-3">
                      <argon-input
                        id="username"
                        type="username"
                        placeholder="Username"
                        name="username"
                        size="lg"
                        v-model="username"
                      />
                    </div>
                    <div class="mb-3">
                      <argon-input
                        id="password"
                        type="password"
                        placeholder="Password"
                        name="password"
                        size="lg"
                        v-model="password"
                      />
                    </div>
                    <argon-switch id="rememberMe" name="remember-me"
                      >Remember me</argon-switch
                    >

                    <div class="text-center">
                      <argon-button
                        class="mt-4"
                        variant="gradient"
                        color="success"
                        fullWidth
                        size="lg"
                        @click="doLogin"
                        >Sign in</argon-button
                      >
                    </div>
                    <argon-alert
                      v-if="showError"
                      color="danger"
                      icon="ni ni-bell-55"
                     dismissible
                    >
                      {{ errorMessage }}
                    </argon-alert>

                    <argon-alert
                      v-if="success"
                      color="success"
                      icon="ni ni-bell-55"
                     dismissible
                    >
                      Jump to your Account
                    </argon-alert>
                    
                  </form>
                </div>
                <div class="px-1 pt-0 text-center card-footer px-lg-2">
                  <p class="mx-auto mb-4 text-sm">
                    Don't have an account?

                    <router-link to="/signup" class="text-success text-gradient font-weight-bold">
                    Sign up  
                    </router-link>
                  </p>
                </div>
              </div>
            </div>
            <div
              class="top-0 my-auto text-center col-6 d-lg-flex d-none h-100 pe-0 position-absolute end-0 justify-content-center flex-column"
            >
              <div
                class="position-relative bg-gradient-primary h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center overflow-hidden"
                style="
                  background-image: url(&quot;https://raw.githubusercontent.com/creativetimofficial/public-assets/master/argon-dashboard-pro/assets/img/signin-ill.jpg&quot;);
                  background-size: cover;
                "
              >
                <span class="mask bg-gradient-success opacity-6"></span>
                <h4
                  class="mt-5 text-white font-weight-bolder position-relative"
                >
                  Nku 2021 Cyber Security
                </h4>
                <p class="text-white position-relative">
                  Team  of  developers:  
                  JiaHao Li, YuZhe Zhong
                  MingXu Ai, XianQian Ma 
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
