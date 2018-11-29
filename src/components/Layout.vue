<template>
  <div class="container-fruild mp0">
    <div class="row">
      <div id="head_carousel" class="col carousel slide" data-ride="carousel">
        <!-- 图片 -->
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img class="d-block w-100" src="../assets/img/hotel1.jpg" alt>
          </div>
          <div class="carousel-item">
            <img class="d-block w-100" src="../assets/img/hotel2.jpg" alt>
          </div>
          <div class="carousel-item">
            <img class="d-block w-100" src="../assets/img/hotel3.jpg" alt>
          </div>
        </div>
        <ol class="carousel-indicators">
          <li class="activate" data-target="#head_carousel" data-slide-to="0"></li>
          <li data-target="#head_carousel" data-slide-to="1"></li>
          <li data-target="#head_carousel" data-slide-to="2"></li>
        </ol>
        <a class="carousel-control-prev" href="#head_carousel" data-slide="prev">
          <span class="carousel-control-prev-icon"></span>
        </a>
        <a class="carousel-control-next" href="#head_carousel" data-slide="next">
          <span class="carousel-control-next-icon"></span>
        </a>
      </div>
    </div>
    <div class="head_nav">
      <ul class="list-group">
        <li class="list-group">
          <ul class="nav nav-fill">
            <li class="nav-item">
              <a class="text-dark" href="#">全天房</a>
            </li>
            <li class="nav-item">
              <a class="muted" href="#">钟点房</a>
            </li>
            <li class="nav-item">
              <a class="muted" href="#">特价房</a>
            </li>
          </ul>
        </li>
        <li class>
          <span>武汉市</span>
          <span class="ml-80%">我的位置</span>
        </li>
        <li class>日期</li>
        <li class>名称</li>
      </ul>
    </div>
  </div>
</template>
<style>
#head_carousel img {
  height: 150px;
}
.head_nav > ul > li {
  position: relative;
  display: block;
  padding: 0.75rem 3.25rem;
  border-style: none none solid none;
  border-color: #6c757d14;
}

.muted {
  font-size: 14px;
  color: #606060;
}
</style>
