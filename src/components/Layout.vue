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

    <div class="bg-light">
      <ul class="nav nav-pills nav-fill nav-justified">
        <li class="nav-item">
          <a href class="nav-link">全天房</a>
        </li>
        <li class="nav-item">
          <a href class="nav-link text-muted">钟点房</a>
        </li>
      </ul>
    </div>
    <!-- <div class="row  main_head justify-content-between bg-info">
    <div class="col-lg-4  bg-success">
        logo
    </div>
    <div class="col-lg-4  bg-light">
        他们
    </div>
    <div class="col-lg-4  bg-danger">
        我们
    </div>
    </div>-->
  </div>
</template>
