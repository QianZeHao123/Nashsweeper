import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    // port: 1234,
    proxy: {
      // UploadPage CORS
      "/UploadPage": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true,
        pathRewrite: {
          "^/UploadPage": "/UploadPage",
        },
      },
      // GetUserData CORS
      "/GetUserData": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true,
        pathRewrite: {
          "^/GetUserData": "/GetUserData",
        },
      },
    },
  },
});
