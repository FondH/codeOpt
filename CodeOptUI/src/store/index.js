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
    modelSettings: JSON.parse(window.localStorage.getItem('modelSettings')) || {
      model: 'model1',
      proxy: '',
      temperature: 0.7,
      maxTokens: 100,
      topP: 0.9,
      frequencyPenalty: 0,
      presencePenalty: 0
    },
    algorithmSettings: JSON.parse(window.localStorage.getItem('algorithmSettings')) || {
      python: {
        syntaxMethod: 'classic',
        vulnerabilityMethod: 'none',
        styleCheckMethod: 'classic'
      },
      go: {
        syntaxMethod: 'classic',
        vulnerabilityMethod: 'none',
        styleCheckMethod: 'classic'
      },
      java: {
        syntaxMethod: 'classic',
        vulnerabilityMethod: 'none',
        styleCheckMethod: 'classic'
      },
      cpp: {
        syntaxMethod: 'classic',
        vulnerabilityMethod: 'none',
        styleCheckMethod: 'classic'
      },
      js: {
        syntaxMethod: 'classic',
        vulnerabilityMethod: 'none',
        styleCheckMethod: 'classic'
      },
      ruby: {
        syntaxMethod: 'classic',
        vulnerabilityMethod: 'none',
        styleCheckMethod: 'classic'
      },
      php: {
        syntaxMethod: 'classic',
        vulnerabilityMethod: 'none',
        styleCheckMethod: 'classic'
      }
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
    setModelSettings(state, newSettings) {
      state.modelSettings = newSettings;
    },
    setAlgorithmSettings(state, newSettings) {
      state.algorithmSettings = newSettings;
    }
  },
  actions,
  getters: {},


});
