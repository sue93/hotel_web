<template>
<div class="container">
<div class="card border-primary">
  <img class="card-img-bottom" style="height:100px;" src="../assets/logo.png" alt="">
  <div class="card-body">
    <h4 class="card-title">Title</h4>
    <p class="card-text">Text</p>
  </div>
</div>

</div>

</template>
<script>

export default {
  name: 'hello',
  data () {
    return {
      counter: 0
    }
  }
}
</script>
<style>
.container > div {
  height: 500px;
}
</style>
