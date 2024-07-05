<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";

import SidenavItem from "./SidenavItem.vue";
import SidenavCard from "./SidenavCard.vue";

const store = useStore();
const isRTL = computed(() => store.state.isRTL);
const isAu =  computed(() => store.state.isAuthenticated);

const getRoute = () => {
  const route = useRoute();
  const routeArr = route.path.split("/");
  return routeArr[1];
};


</script>


<template>
  <div
    class="collapse navbar-collapse w-auto h-auto h-100"
    id="sidenav-collapse-main"
  >
    <ul class="navbar-nav">
      <li class="nav-item">
        <sidenav-item
          to="/main-page"
          :class="getRoute() === 'main-page' ? 'active' : ''"
          :navText="isRTL ? '仪表盘' : 'Dashboard'"
        >
          <template v-slot:icon>
            <i class="ni ni-tv-2 text-primary text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li class="nav-item">
        <sidenav-item
          to="/check"
          :class="getRoute() === 'check' ? 'active' : ''"
          :navText="isRTL ? '生成报告' : 'Check'"
        >
          <template v-slot:icon>
            <i class="ni ni-credit-card text-success text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>


      <li class="nav-item">
        <sidenav-item
          to="/tables"
          :class="getRoute() === 'tables' ? 'active' : ''"
          :navText="isRTL ? '历史记录' : 'History'"
        >
          <template v-slot:icon>
            <i
              class="ni ni-calendar-grid-58 text-warning text-sm opacity-10"
            ></i>
          </template>
        </sidenav-item>
      </li>



      <li class="nav-item">
        <sidenav-item
          to="/network"
          :class="getRoute() === 'network' ? 'active' : ''"
          :navText="isRTL ? '网络' : 'modelwork'"
        >

          <template v-slot:icon>
           <i class="ni ni-world-2 text-danger text-sm opacity-10"></i>
          </template>
        
        </sidenav-item>
      </li>


      <li class="nav-item">
        <sidenav-item
          to="/virtual-reality"
          :class="getRoute() === 'virtual-reality' ? 'active' : ''"
          :navText="isRTL ? '虚拟现实' : 'Virtual Reality'"
        >
          <template v-slot:icon>
            <i class="ni ni-app text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
      <li class="mt-3 nav-item">
        <h6
          v-if="isRTL"
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="isRTL ? 'me-4' : 'ms-2'"
        >
          账户信息
        </h6>

        <h6
          v-else
          class="text-xs ps-4 text-uppercase font-weight-bolder opacity-6"
          :class="isRTL ? 'me-4' : 'ms-2'"
        >
          ACCOUNT PAGES
        </h6>
      </li>

      <li class="nav-item">
        <sidenav-item
          to="/profile"
          :class="getRoute() === 'profile' ? 'active' : ''"
          :navText="isRTL ? '主页' : 'Profile'"
        >
          <template v-slot:icon>
            <i class="ni ni-single-02 text-dark text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li v-if="isAu"  class="nav-item">
        <sidenav-item
          to="/logout"
          :class="getRoute() === 'logout' ? 'active' : ''"
          :navText="isRTL ? '登出': 'Sign out'"
        >
          <template v-slot:icon>
            <i class="ni ni-single-copy-04 text-danger text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li v-if="!isAu" class="nav-item">
        <sidenav-item
          to="/login"
          :class="getRoute() === 'signin' ? 'active' : ''"
          :navText="isRTL ? '注册': 'Sign In'"
        >
          <template v-slot:icon>
            <i class="ni ni-single-copy-04 text-danger text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>

      <li v-if="!isAu" class="nav-item">
        <sidenav-item
          to="/signup"
          :class="getRoute() === 'signup' ? 'active' : ''"
          :navText="isRTL ? '退出' : 'Sign Up'"
        >
          <template v-slot:icon>
            <i class="ni ni-collection text-info text-sm opacity-10"></i>
          </template>
        </sidenav-item>
      </li>
    </ul>
  </div>

  <div class="pt-3 mx-3 mt-3 sidenav-footer">
    <sidenav-card
      :card="{
        title: 'Need Help?',
        description: 'Please check our docs',
        links: [
          {
            label: 'Documentation',
            route:
              'https://www.creative-tim.com/learning-lab/vue/overview/argon-dashboard/',
            color: 'dark',
          },
          {
            label: 'Buy now',
            route:
              'https://www.creative-tim.com/product/vue-argon-dashboard-pro?ref=vadp',
            color: 'success',
          },
        ],
      }"
    />
  </div>
</template>
