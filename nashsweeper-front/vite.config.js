import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    // port: 1234,
    proxy: {
      "/backend": {
        target: "http://127.0.0.1:6778",
        changeOrigin: true,
        pathRewrite: {
          "^/backend": "/backend",
        },
      },
    },
  },
});
