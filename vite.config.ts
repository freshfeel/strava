import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: '/strava/', // This should match your repository name
  css: {
    postcss: './postcss.config.cjs'
  }
})
