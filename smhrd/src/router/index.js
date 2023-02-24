import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/main/MainView.vue'
import DetectedView from '../views/main/DetectedView.vue'
import PatientView from '../views/patient/PatientView.vue'
import VitalView from '../views/patient/VitalView.vue'

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/detected',
    name: 'DetectedView',
    component: DetectedView
  },
  {
    // path: '/patient/:pid'
    path: '/patient',
    name: 'PatientView',
    component: PatientView
  },
  {
    path: '/vital',
    name: 'VitalView',
    component: VitalView
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
