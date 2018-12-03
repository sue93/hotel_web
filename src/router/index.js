import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Layout from '@/components/LaYout'
import home from '@/components/Home'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: Layout
    }, {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    }, {
      path: '/home',
      name: 'HOme',
      component: home
    }
  ]
})
