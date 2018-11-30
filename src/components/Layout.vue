<template>
  <div class="container-fruild mp0">
    <div class="row">
      <div id="head_carousel" class="col carousel slide" data-ride="carousel" style="margin:0px;padding:0px;">
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
      <ul class="">
        <li class="" style="border-bottom: 1px solid #c0c0c0;">
          <ul class="inter_type">
            <li class="">
              <span class="muted activate" href="#">全天房</span>
            </li>
            <li class="">
              <span  class="muted" href="#">钟点房</span>
            </li>
            <li class="">
              <span class="muted" href="#">特价房</span>
            </li>
          </ul>
        </li>
        <li class="list_group_item">
          <span>武汉市</span>
          <span class="ml-80%" style="float:right">我的位置</span>
        </li>
        <li class="list_group_item">
         <p style="width:80px;" class="dis_inline mp0">入住日期11/30</p>
            <p style="width:80px;" class="dis_inline mp0">共两晚</p>
         <p style="width:80px;" class="dis_inline mp0">离店日期11/31</p>
        </li>
        <li class="list_group_item">
          <p style="width:80px;">离店日期12</p>

        </li>
      </ul>
    </div>
  </div>
</template>
<style>
#head_carousel img {
  height: 150px;
}
.list_group_item{
  padding: 30px 40px;
  border-bottom: 1px solid #c0c0c0;
}

.inter_type>li{
  display: inline;
  text-align: center;
}
.muted{
    line-height: 24px;
    padding: 12px 0px;
    text-decoration: none;
    display:inline-block;
    width: 30%;
    font-size: 14px;
    color:#606266;
}

.activate{
      color: #303133;
      font-size: 16px;
      font-family: fantasy;
      border-bottom: 1px solid #409EFF;
}

</style>
