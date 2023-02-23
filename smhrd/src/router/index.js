import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/main/MainView.vue'

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/detected',
    name: 'DetectedView',
    component: () => import(/* webpackChunkName: "home", webpackPrefetch:true */ '../views/main/DetectedView.vue')
  },
  {
    path: '/patient',
    name: 'PatientView',
    component: () => import(/* webpackChunkName: "home", webpackPrefetch:true */ '../views/patient/PatientView.vue')
  },
  {
    path: '/vital',
    name: 'VitalView',
    component: () => import(/* webpackChunkName: "home", webpackPrefetch:true */ '../views/patient/VitalView.vue')
  },
  {
    path: '/addpatient',
    name: 'AddPatient',
    component: () => import(/* webpackChunkName: "home" */ '../views/popups/AddPatient.vue')
  },
  {
    path: '/addvital',
    name: 'AddVital',
    component: () => import(/* webpackChunkName: "home" */ '../views/popups/AddVital.vue')
  },
  {
    path: '/getAllPatient',
    name: 'getAllPatient',
    component: () => import(/* webpackChunkName: "home" */ '../views/patient/PatientView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
