const { defineConfig } = require('@vue/cli-service')
const path = require('path');

module.exports = defineConfig({
  transpileDependencies: true,    //Transpile your dependencies
  lintOnSave : false,
  publicPath: "",          //Path of static directory
  outputDir: path.resolve(__dirname, '../static'),   // Output path for the static files
  runtimeCompiler: true,
  devServer: {
    // Write files to disk in dev mode, so FastAPI can serve the assets
    port: 8005,
    devMiddleware: {
      writeToDisk: true,
    },
    historyApiFallback: true
  },
})