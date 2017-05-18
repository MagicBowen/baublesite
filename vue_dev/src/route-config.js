import List from './List.vue'
import EChart from './ECharts.vue'

export default {routes: [
  { path: '/', component: List },
  { path: '/home', component: List },
  { path: '/chart', component: EChart }
]}