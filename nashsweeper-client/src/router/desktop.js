import WidthWarning from "../views/DesktopPages/WidthWarning.vue";
import ViewResult from "../views/DesktopPages/ViewResult.vue";
import ViewLogs from "../views/DesktopPages/ViewLogs.vue";

export default [
  {
    path: "/desktop/widthwarning",
    name: "WidthWarning",
    component: WidthWarning,
  },
  {
    path: "/desktop/viewresult",
    name: "ViewResult",
    component: ViewResult,
  },
  {
    path: "/desktop/viewlogs",
    name: "ViewLogs",
    component: ViewLogs,
  },
];
