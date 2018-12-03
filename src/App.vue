<template >
<div>
<ul>
  <li><router-link to="/">首页</router-link></li>
  <li><router-link to="/home">主页</router-link></li>
  <li><router-link to="/hello">欢迎</router-link></li>
  <a href="http://www.badiu.com">百度</a>
</ul>

<router-view ></router-view>

</div>

</template>

<script>

export default {
  name: 'App1'
}
</script>
