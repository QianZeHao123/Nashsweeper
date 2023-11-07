import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
// deal with CORS
import BackendServerInfo from "./BackendServerInfo.json";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    watch: { usePolling: true },
    proxy: {
      // 
      "/api": {
        target: BackendServerInfo.backendIP,
        changeOrigin: true,
        pathRewrite: {
          "^/api": "",
        },
      },
      "/nodebridge": {
        target: BackendServerInfo.nodebridgeIP,
        changeOrigin: true,
        pathRewrite: {
          "^/nodebridge": "",
        },
      },
    },
  },
});
