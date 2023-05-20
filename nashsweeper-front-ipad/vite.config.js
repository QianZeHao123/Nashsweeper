import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
// deal with CORS
import BackendServerInfo from './BackendServerInfo.json'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      // UploadPage CORS
      "/UploadPage": {
        // target: "http://127.0.0.1:5000",
        target: "BackendServerInfo.backendIP",
        changeOrigin: true,
        pathRewrite: {
          "^/UploadPage": "/UploadPage",
        },
      },
      // GetUserData CORS
      "/GetUserData": {
        // target: "http://127.0.0.1:5000",
        target: BackendServerInfo.backendIP,
        changeOrigin: true,
        pathRewrite: {
          "^/GetUserData": "/GetUserData",
        },
      },
    },
  },
});
