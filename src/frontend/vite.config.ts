import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    port: 3000,
    hmr: false,
  },
  build: {
    outDir: 'dist',
    sourcemap: false, // ソースマップを無効化
    minify: true     // コードの最小化
  }
})
