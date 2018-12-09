<template>
  <div>
    <h1>{{name}}</h1>

    <input v-model.number="msg" type="number" placeholder="请输入年龄" value>
    <p>{{msg}}</p>
  </div>
</template>
<script>
export default {
  name: 'home',
  data () {
    return {
      msg: '',
      name: '哈哈',
      xc: '<h2>我们都是好孩子</h2>'
    }
  }
}
</script>
