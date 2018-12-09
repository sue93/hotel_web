<template>
  <div style>
    <router-link to="/hello">Go to Foo</router-link>
    <router-link to="/home">Go to Bar</router-link>
    <router-link to="/test">Go to test</router-link>

    <pd>
      <router-view></router-view>
    </pd>
    <el-container>
      <el-aside class="ly_primary">
        <div class="hotel_info">
          <h4>金九龙大酒店</h4>
          <p>操作员:admin</p>
          <div>
            <p>
              <span>班次:早班</span>
              <span>消息</span>
            </p>
            <p>
              <span>2018/12/04</span>
              <span>08:32</span>
            </p>
          </div>
        </div>
        <mymenu></mymenu>
      </el-aside>
      <el-container>
        <el-header style="height:200px;">Header</el-header>
        <el-main style="height:500px;">
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
