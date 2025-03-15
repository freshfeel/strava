import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: '/strava/', // This should match your repository name
  build: {
    rollupOptions: {
      input: {
        main: 'index.html',
        auth: 'public/auth.html',
        callback: 'public/callback.html'
      }
    }
  },
  css: {
    postcss: './postcss.config.cjs'
  }
})
