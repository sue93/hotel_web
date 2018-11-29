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

    <div class="bg-xr">
      <ul class="nav nav-pills nav-fill nav-justified">
        <li class="nav-item">
          <a href class="nav-link">全天房</a>
        </li>
        <li class="nav-item">
          <a href class="nav-link text-muted">钟点房</a>
        </li>
      </ul>
    </div>

    <div class="bg-wt">
      <ul class="list-group">
        <li class="list-group-item">
          <i class="iconfont icon-Hotel"></i>
          <span class="ml-4">泉州市</span>
          <i class="iconfont icon-jiantou_liebiaoxiangyou"></i>

          <span class="float-right text-muted">
            <i class="iconfont icon-weizhixiangqing"></i>
            我的位置
          </span>
        </li>
        <li class="list-group-item">
          <i class="iconfont icon-riqi1"></i>
          <span class="ml-2">
            <strong>2018-11-28</strong>
            <small class="text-muted font-size:15px">周四</small>
          </span>
          <label class="ml-4">共1晚</label>
          <span class="ml-4">
            <strong>2018-11-29</strong>
            <small class="text-muted font-size:15px">周五</small>
          </span>
        </li>
        <li class="list-group-item">
          <i class="iconfont icon-lubiao"></i>
          <small class="ml-2">位置/商圈/酒店名称</small>
        </li>
      </ul>
    </div>
    <div style="width:20px;">哈哈哈哈哈哈哈ssfsffasfdfsfasfsafsafasfdasaasfwefwefwfwfwfwefeafs</div>
  </div>
</template>
