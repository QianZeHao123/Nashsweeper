import { createRouter, createWebHistory } from "vue-router";
// import Home from "../views/Home.vue";
import Pad from "../views/Pad.vue";
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "Home",
      component: Pad,
    },
    {
      path: "/Pad",
      name: "Pad",
      component: Pad,
    },
  ],
});

export default router;
