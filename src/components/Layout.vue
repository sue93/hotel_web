<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <div id="lbt" class="carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li data-target="#lbt" data-slide-to="0" class="active"></li>
            <li data-target="#lbt" data-slide-to="1"></li>
            <li data-target="#lbt" data-slide-to="2"></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img class="d-block w-100" src="../assets/img/hotel1.jpg" alt="First slide">
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src="../assets/img/hotel2.jpg" alt="Second slide">
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src="../assets/img/hotel3.jpg" alt="Third slide">
            </div>
          </div>
          <a class="carousel-control-prev" href="#lbt" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#lbt" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div>
      <div class="row inner_pt">
        <div class="inner">
          <ul class="mp-0">
            <li>
              <a class="ziti actvate" href>全天房</a>
              <i class="xian"></i>
            </li>
            <li>
              <a class="ziti" href>钟点房</a>
            </li>
            <li>
              <a class="ziti" href>特价房</a>
            </li>
          </ul>
        </div>
      </div>
      <div class="row w-100 mp-0">
        <ul class="search">
          <li>
            <p style="display:inline-block;margin:auto;width:100%">
              <span>武汉市</span>
              <span style="float:right">我的位置</span>
            </p>
          </li>
          <li>
            <div class="lq">
              <p class="lq_ly">入住时间</p>
              <p class>12/02</p>
            </div>
            <div class="lq" style="margin-left:22%">
              <p class="lq_ly" style="display:table-cell;vertical-align:middle;">共一晚</p>
            </div>
            <div class="lq" style="float:right">
              <p class="lq_ly">离店时间</p>
              <p class>12/03</p>
            </div>
          </li>
          <li>
            <input id="hotel_name" style type="text" name placeholder="品牌/地点/酒店名">
          </li>
          <li>
            <div>
              <button type="button" class="iconfont icon-sousuo btn btn-block btn_primary">查询酒店</button>
            </div>
          </li>
        </ul>
      </div>
      <div class="row" style="background-color: #dee2e6;height:6px;"></div>
    </div>
    <div class="my_hotel">
      <span>
        <i class="iconfont icon-jiudian-A"></i> 我的酒店
      </span>

      <span style="display:inline;float:right">
        <i class="iconfont icon-jiudian-A"></i> 我的收藏
      </span>
    </div>
  </div>
</template>
<style scoped>
.carousel-inner img {
  height: 200px;
}
.inner_pt {
  border-bottom: 1px solid #dee2e6;
  text-align: left;
}

.inner {
  margin: auto;
  width: 70%;
}

.inner > ul > li {
  width: 30%;
  display: inline-block;
  padding: 20px 0px;
}
.xian {
  width: 20px;
  display: inline-block;
  position: relative;
  bottom: -16px;
  left: -38px;

  border-bottom: 2px solid #37bbf3;
}

.ziti {
  font-size: 0.75rem;
  color: #72859d;
  text-decoration: none;
}

.actvate {
  font-size: 1rem;
  color: #1e2b3b;
}

.search {
  width: 100%;
  padding-right: 40px;
}

.search > li {
  padding: 20px 0px;
  border-bottom: 1px solid #dee2e6;
}

.lq {
  display: inline-block;
  width: 50px;
}
.lq p {
  margin: 0px;
  padding: 0px;
  display: inline-block;
}
.lq_ly {
  font-size: 12px;
  color: #72859d;
}
#hotel_name {
  border: none;
  outline: none;
}
.my_hotel {
  position: fixed;
  bottom: 0px;
  width: 100%;
  font-size: 1rem;
  padding: 10px 40px;
}
</style>
