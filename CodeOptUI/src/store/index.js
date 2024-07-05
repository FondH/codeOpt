import { createStore } from "vuex";
import actions from './actions.js'
export default createStore({
  state: {
    hideConfigButton: false,
    isPinned: false,
    showConfig: false,
    sidebarType: "bg-white",
    isRTL: false,
    mcolor: "",
    darkMode: false,
    isNavFixed: true,
    isAbsolute: true,
    showNavs: true,
    showSidenav: true,
    showNavbar: true,
    showFooter: true,
    showMain: true,
    layout: "default",

    //** user context
    token: localStorage.getItem('token') || null,
    userInfo: JSON.parse(localStorage.getItem('userInfo')) || null,
    profile:{

    },
    isAuthenticated: localStorage.getItem('isAuthenticated') || false,
  },
  mutations: {
    LOGIN(state, value){state.token = value},

    SET_USER(state, info){
      state.userInfo = info
    },
    SET_AUTH(state, bo){state.isAuthenticated = bo},
    SET_PROFILE(state, info){state.profile = info},
    toggleConfigurator(state) {
      state.showConfig = !state.showConfig;
    },
    sidebarMinimize(state) {
      let sidenav_show = document.querySelector("#app");
      if (state.isPinned) {
        sidenav_show.classList.add("g-sidenav-hidden");
        sidenav_show.classList.remove("g-sidenav-pinned");
        state.isPinned = false;
      } else {
        sidenav_show.classList.add("g-sidenav-pinned");
        sidenav_show.classList.remove("g-sidenav-hidden");
        state.isPinned = true;
      }
    },
    sidebarType(state, payload) {
      state.sidebarType = payload;
    },
    navbarFixed(state) {
      if (state.isNavFixed === false) {
        state.isNavFixed = true;
      } else {
        state.isNavFixed = false;
      }
    },
  },
  actions,
  getters: {},


});
