<template>
  <main>
    <div class="container-fluid py-4">
      <div
        class="page-header min-height-300"
        style="
          background-image: url(&quot;https://images.unsplash.com/photo-1531512073830-ba890ca4eba2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80&quot;);
          margin-right: -24px;
          margin-left: -34%;
        "
      >
        <span class="mask bg-gradient-success opacity-4"></span> 
      </div>
      <div class="card shadow-lg mt-n9">
        <div class="card-body p-3">
          <div class="row gx-1">

            <div class="col-auto my-auto">
              <div class="h-100">
                <h5 class="mb-1">Custom your own CodeOpt</h5>
   
              </div>
            </div>
            <div
              class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0"
            >
              <div class="nav-wrapper position-relative end-0">
                <ul
                  class="p-1 bg-transparent nav nav-pills nav-fill"
                  role="tablist"
                >
                  <li class="nav-item">
                    <a
                      class="px-0 py-1 mb-0 nav-link active"
                      data-bs-toggle="tab"
                      href="javascript:;"
                      role="tab"
                      aria-selected="true"
                      @click="showModelSettings = true"
                    >
                      <svg
                        class="text-dark"
                        width="16px"
                        height="16px"
                        viewBox="0 0 42 42"
                        version="1.1"
                        xmlns="http://www.w3.org/2000/svg"
                        xmlns:xlink="http://www.w3.org/1999/xlink"
                      >
                        <g
                          stroke="none"
                          stroke-width="1"
                          fill="none"
                          fill-rule="evenodd"
                        >
                          <g
                            transform="translate(-2319.000000, -291.000000)"
                            fill="#FFFFFF"
                            fill-rule="nonzero"
                          >
                            <g transform="translate(1716.000000, 291.000000)">
                              <g transform="translate(603.000000, 0.000000)">
                                <path
                                  class="color-background"
                                  d="M22.7597136,19.3090182 L38.8987031,11.2395234 C39.3926816,10.9925342 39.592906,10.3918611 39.3459167,9.89788265 C39.249157,9.70436312 39.0922432,9.5474453 38.8987261,9.45068056 L20.2741875,0.1378125 L20.2741875,0.1378125 C19.905375,-0.04725 19.469625,-0.04725 19.0995,0.1378125 L3.1011696,8.13815822 C2.60720568,8.38517662 2.40701679,8.98586148 2.6540352,9.4798254 C2.75080129,9.67332903 2.90771305,9.83023153 3.10122239,9.9269862 L21.8652864,19.3090182 C22.1468139,19.4497819 22.4781861,19.4497819 22.7597136,19.3090182 Z"
                                />
                                <path
                                  class="color-background"
                                  d="M23.625,22.429159 L23.625,39.8805372 C23.625,40.4328219 24.0727153,40.8805372 24.625,40.8805372 C24.7802551,40.8805372 24.9333778,40.8443874 25.0722402,40.7749511 L41.2741875,32.673375 L41.2741875,32.673375 C41.719125,32.4515625 42,31.9974375 42,31.5 L42,14.241659 C42,13.6893742 41.5522847,13.241659 41,13.241659 C40.8447549,13.241659 40.6916418,13.2778041 40.5527864,13.3472318 L24.1777864,21.5347318 C23.8390024,21.7041238 23.625,22.0503869 23.625,22.429159 Z"
                                  opacity="0.7"
                                />
                                <path
                                  class="color-background"
                                  d="M20.4472136,21.5347318 L1.4472136,12.0347318 C0.953235098,11.7877425 0.352562058,11.9879669 0.105572809,12.4819454 C0.0361450918,12.6208008 6.47121774e-16,12.7739139 0,12.929159 L0,30.1875 L0,30.1875 C0,30.6849375 0.280875,31.1390625 0.7258125,31.3621875 L19.5528096,40.7750766 C20.0467945,41.0220531 20.6474623,40.8218132 20.8944388,40.3278283 C20.963859,40.1889789 21,40.0358742 21,39.8806379 L21,22.429159 C21,22.0503869 20.7859976,21.7041238 20.4472136,21.5347318 Z"
                                  opacity="0.7"
                                />
                              </g>
                            </g>
                          </g>
                        </g>
                      </svg>
                      <span class="ms-1">Model Settings</span>
                    </a>
                  </li>
                  <li class="nav-item">
                    <a
                      class="px-0 py-1 mb-0 nav-link"
                      data-bs-toggle="tab"
                      href="javascript:;"
                      role="tab"
                      aria-selected="false"
                      @click="showModelSettings = false"
                    >
                      <svg
                        class="text-dark"
                        width="16px"
                        height="16px"
                        viewBox="0 0 40 44"
                        version="1.1"
                        xmlns="http://www.w3.org/2000/svg"
                        xmlns:xlink="http://www.w3.org/1999/xlink"
                      >
                        <title>document</title>
                        <g
                          stroke="none"
                          stroke-width="1"
                          fill="none"
                          fill-rule="evenodd"
                        >
                          <g
                            transform="translate(-1870.000000, -591.000000)"
                            fill="#FFFFFF"
                            fill-rule="nonzero"
                          >
                            <g transform="translate(1716.000000, 291.000000)">
                              <g transform="translate(154.000000, 300.000000)">
                                <path
                                  class="color-background"
                                  d="M40,40 L36.3636364,40 L36.3636364,3.63636364 L5.45454545,3.63636364 L5.45454545,0 L38.1818182,0 C39.1854545,0 40,0.814545455 40,1.81818182 L40,40 Z"
                                  opacity="0.603585379"
                                />
                                <path
                                  class="color-background"
                                  d="M30.9090909,7.27272727 L1.81818182,7.27272727 C0.814545455,7.27272727 0,8.08727273 0,9.09090909 L0,41.8181818 C0,42.8218182 0.814545455,43.6363636 1.81818182,43.6363636 L30.9090909,43.6363636 C31.9127273,43.6363636 32.7272727,42.8218182 32.7272727,41.8181818 L32.7272727,9.09090909 C32.7272727,8.08727273 31.9127273,7.27272727 30.9090909,7.27272727 Z M18.1818182,34.5454545 L7.27272727,34.5454545 L7.27272727,30.9090909 L18.1818182,30.9090909 L18.1818182,34.5454545 Z M25.4545455,27.2727273 L7.27272727,27.2727273 L7.27272727,23.6363636 L25.4545455,23.6363636 L25.4545455,27.2727273 Z M25.4545455,20 L7.27272727,20 L7.27272727,16.3636364 L25.4545455,16.3636364 L25.4545455,20 Z"
                                />
                              </g>
                            </g>
                          </g>
                        </g>
                      </svg>
                      <span class="ms-1">Strategy Type</span>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="showModelSettings" class="py-4 container-fluid">
        <div class="row">
          <div class="col-md-8">
            <div class="card">
              <div class="card-header pb-0">
                <div class="d-flex align-items-center">
                  <p class="mb-0">Edit Model Settings</p>
                  <argon-button color="success" size="sm" class="ms-auto"
                    >Save</argon-button
                  >
                </div>
              </div>
              <div class="card-body">
                <p class="text-uppercase text-sm">Model Information</p>
                <div class="row">
                  <div class="col-md-6">
                    <label for="model-select" class="form-control-label">Model</label>
                    <select id="model-select" v-model="modelSettings.model" class="form-control">
                      <option value="model3">Phi3:3.8B</option>
                      <option value="model1">Lamma3-8b</option>
                      <option value="model2">Lamma2-7B-Instruct</option>
         
                    </select>
                  </div>
                  <div class="col-md-6">
                    <label for="proxy-input" class="form-control-label">Proxy</label>
                    <argon-input id="proxy-input" type="text" v-model="modelSettings.proxy" />
                  </div>
                  <div class="col-md-6">
                    <label for="temperature-input" class="form-control-label">Temperature</label>
                    <argon-input id="temperature-input" type="number" v-model="modelSettings.temperature" min="0" max="1" step="0.1" />
                  </div>
                  <div class="col-md-6">
                    <label for="max-tokens-input" class="form-control-label">Max Tokens</label>
                    <argon-input id="max-tokens-input" type="number" v-model="modelSettings.maxTokens" min="1" />
                  </div>
                </div>
                <hr class="horizontal dark" />
                <p class="text-uppercase text-sm">Additional Options</p>
                <div class="row">
                  <div class="col-md-6">
                    <label for="top-p-input" class="form-control-label">Top P</label>
                    <argon-input id="top-p-input" type="number" v-model="modelSettings.topP" min="0" max="1" step="0.1" />
                  </div>
                  <div class="col-md-6">
                    <label for="frequency-penalty-input" class="form-control-label">Frequency Penalty</label>
                    <argon-input id="frequency-penalty-input" type="number" v-model="modelSettings.frequencyPenalty" min="0" max="2" step="0.1" />
                  </div>
                  <div class="col-md-6">
                    <label for="presence-penalty-input" class="form-control-label">Presence Penalty</label>
                    <argon-input id="presence-penalty-input" type="number" v-model="modelSettings.presencePenalty" min="0" max="2" step="0.1" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="py-4 container-fluid">
        <div class="row">
          <div class="col-md-8">
            <div class="card">
              <div class="card-header pb-0">
                <div class="d-flex align-items-center">
                  <p class="mb-0">Algorithm Kernel Settings</p>
                  <argon-button color="success" size="sm" class="ms-auto"
                    >Save</argon-button
                  >
                </div>
              </div>
              <div class="card-body">
                <p class="text-uppercase text-sm">Syntax Analysis</p>
                <div class="row">
                  <div class="col-md-6">
                    <label for="syntax-method" class="form-control-label">Method</label>
                    <select id="syntax-method" v-model="algorithmSettings.syntaxMethod" class="form-control">
                      <option value="method1">classic(cppcheck) 1</option>
                      <option value="method2">perimum(codeclimate)</option>
                      <option value="method3">inteligent(llm)</option>
                    </select>
                  </div>
                </div>
                <hr class="horizontal dark" />
                <p class="text-uppercase text-sm">Vulnerability Analysis</p>
                <div class="row">
                  <div class="col-md-6">
                    <label for="vulnerability-method" class="form-control-label">Method</label>
                    <select id="vulnerability-method" v-model="algorithmSettings.vulnerabilityMethod" class="form-control">
                      <option value="method1">None</option>
                      <option value="method2">perimum(D-shield)</option>
                      <option value="method3">inteligent(llm)</option>
                    </select>
                  </div>
                </div>
                <hr class="horizontal dark" />
                <p class="text-uppercase text-sm">Style Check</p>
                <div class="row">
                  <div class="col-md-6">
                    <label for="style-check-method" class="form-control-label">Method</label>
                    <select id="style-check-method" v-model="algorithmSettings.styleCheckMethod" class="form-control">
                       <option value="method1">classic(pylint) 1</option>
                      <option value="method2">perimum(codeclimate)</option>
                      <option value="method3">inteligent(llm)</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onBeforeMount, onMounted, onBeforeUnmount } from "vue";
import { useStore } from "vuex";

import setNavPills from "@/assets/js/nav-pills.js";
import setTooltip from "@/assets/js/tooltip.js";
// import ProfileCard from "./components/ProfileCard.vue";
import ArgonInput from "@/components/ArgonInput.vue";
import ArgonButton from "@/components/ArgonButton.vue";

const body = document.getElementsByTagName("body")[0];

const store = useStore();
const showModelSettings = ref(true);

const modelSettings = ref({
  model: 'model1',
  proxy: '',
  temperature: 0.7,
  maxTokens: 100,
  topP: 0.9,
  frequencyPenalty: 0,
  presencePenalty: 0
});

const algorithmSettings = ref({
  syntaxMethod: 'method1',
  vulnerabilityMethod: 'method1',
  styleCheckMethod: 'method1'
});

onMounted(() => {
  store.state.isAbsolute = true;
  setNavPills();
  setTooltip();
});
onBeforeMount(() => {
  store.state.imageLayout = "profile-overview";
  store.state.showNavbar = false;
  store.state.showFooter = true;
  store.state.hideConfigButton = true;
  body.classList.add("profile-overview");
});
onBeforeUnmount(() => {
  store.state.isAbsolute = false;
  store.state.imageLayout = "default";
  store.state.showNavbar = true;
  store.state.showFooter = true;
  store.state.hideConfigButton = false;
  body.classList.remove("profile-overview");
});
</script>

<style scoped>
/* 样式可以根据需要进行调整 */
.text-sm {
  font-size: 0.875rem;
}

.align-middle {
  vertical-align: middle;
}

.text-center {
  text-align: center;
}

.text-xs {
  font-size: 0.75rem;
}

.font-weight-bold {
  font-weight: bold;
}

.mb-0 {
  margin-bottom: 0;
}

.min-height-300 {
  min-height: 300px;
}

.mask {
  display: block;
  height: 100%;
}

.bg-gradient-success {
  background: linear-gradient(87deg, #11cdef 0, #1171ef 100%) !important;
}
</style>
