// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

// ui plugins
// 使用了scss，要在vue引入前引用ui组件，防止配置文件无效
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import Vue from 'vue'
import App from './App'
import router from './router'

Vue.use(Buefy)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
