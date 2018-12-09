import Vue from 'vue'
import Router from 'vue-router'
import hello from '@/components/HelloWorld'
import home1 from '@/components/Home'
import test from '@/components/test'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [

    {
      path: '/hello',
      name: 'hello',
      component: hello
    },
    {
      path: '/home',
      name: 'home',
      component: home1
    },

    {
      path: '/test',
      name: 'test',
      component: test
    }
  ]
})
