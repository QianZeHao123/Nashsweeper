import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Mobile from "../views/MobilePage.vue";
import Desktop from "../views/DesktopPage.vue";
import Pad from "../views/PadPage.vue";

import desktop from "./desktop";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
    },
    {
      path: "/mobile",
      name: "Mobile",
      component: Mobile,
    },
    {
      path: "/desktop",
      name: "Desktop",
      component: Desktop,
    },
    {
      path: "/pad",
      name: "Pad",
      component: Pad,
    },
    ...desktop,
  ],
});

export default router;
