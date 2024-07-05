import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import Tables from "../views/Tables.vue";
import checktable from "../views/checktable.vue";
import VirtualReality from "../views/VirtualReality.vue";
import TaskStatus from "../views/TaskStatus.vue";
import Profile from "../views/Profile.vue";
import Signup from "../views/Signup.vue";
import Signin from "../views/Signin.vue";
import Signout from '../views/Signout.vue';
import report from '../views/report.vue';
import network from '../views/network.vue';

import { useStore } from 'vuex'; 

const routes = [
  {
    path: "/",
    name: "/",
    redirect: "/main-page",
    meta: { requiresAuth: true },
  },
  {
    path: "/main-page",
    name: "MainPage",
    component: Dashboard,
    meta: { requiresAuth: true },
  },
  {
    path: "/tables",
    name: "Tables",
    component: Tables,
    meta: { requiresAuth: true },
  },
  {
    path: "/check",
    name: "check",
    component: checktable,
    meta: { requiresAuth: true },
  },
  {
    path: "/network",
    name: "network",
    component: network,
    meta: { requiresAuth: true },
  },
  {
    path: "/virtual-reality",
    name: "Virtual Reality",
    component: VirtualReality,
    meta: { requiresAuth: true },
  },
  {
    path: '/task-status/:taskId', 
    component: TaskStatus,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/report/:taskId', 
    component: report,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "Signin",
    component: Signin,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/logout",
    name: "Signout",
    component: Signout,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});

router.beforeEach((to, from, next) => {
  const store = useStore();
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.state.isAuthenticated) {
      next({ path: '/login' });
    } else {
      next();
    }
  } else {
    next(); // 确保继续导航
  }
});
export default router;
