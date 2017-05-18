import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
// import './assets/theme/theme-black/index.css'
import VueRouter from 'vue-router'
import routeConfig from './route-config'
import App from './App.vue'
import List from './List.vue'
import EChart from './ECharts.vue'


Vue.use(ElementUI)
Vue.use(VueRouter)

const router = new VueRouter(routeConfig)

new Vue({
  router,
  el: '#app',
  render: h => h(App)
})