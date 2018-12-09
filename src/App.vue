<template>
  <div class="mycontent">
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
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          background-color="#2f2f2f"
          text-color="#777777"
          active-text-color="#FEFEFE"
          router
          @select="menu_tab"
        >
          <mymenu :objs="obj" :ta="ta"></mymenu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-main class="mymain">
          <div class>
            <el-tabs v-model="activeName" type="card" closable @tab-remove="close_tab">
              <el-tab-pane
                v-for="(item) in tabs"
                :key="item.name"
                :label="item.title"
                :name="item.name"
              ></el-tab-pane>
            </el-tabs>
          </div>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
.mymain {
  background-color: #cc85d9;
}

.ly_primary {
  width: 18%;
}

.hotel_info {
  margin: 5px auto;
  text-align: center;
}

.mynav {
  height: 30px;
  background-color: aquamarine;
}
</style>
<script>
import mymenu from './components/custom/MyMenu'
export default {
  name: 'sue',
  data: function () {
    return {
      msg: 'women ',
      ta: 'text-align: center;',
      activeName: '2',
      tab_total: 0,
      tabs: [{
        title: '房态图',
        name: '1',
        close: true
      },
      { title: '会员管理',
        name: '2',
        close: true
      }],
      obj: [
        { name: '房态查询', id: '1', child: {} },
        { name: '营销中心', id: '2', child: {} },
        { name: '客史查询', id: '3', child: {} },
        { name: '团队查询', id: '4', child: {} },
        { name: '非住客账', id: '5', child: {} },
        { name: '预定管理', id: '6', child: {} },
        { name: '业务查询', id: '7', child: {} }
      ]
    }
  },
  components: {
    mymenu
  },
  methods: {

    menu_tab: function (index, path) { // 菜单栏选中事件
      this.add_tab()
    },
    add_tab: function () {
      let newTabName = ++this.tabIndex + ''
      this.tabs.push({
        title: 'New Tab',
        name: newTabName,
        content: 'New Tab content'
      })
      this.activeName = newTabName
    },
    close_tab: function (targetName) {
      let tabs = this.tabs
      let activeName = this.activeName

      // 关闭的是当前元素,就激活它的兄弟tab
      if (activeName === targetName) {
        tabs.forEach((tab, index) => {
          if (tab.name === targetName) {
            let nextTab = tabs[index + 1] || tabs[index - 1]
            if (nextTab) {
              activeName = nextTab.name
            }
          }
        })
      }
      this.activeName = activeName
      // 过滤掉
      this.tabs = tabs.filter(tab => tab.name !== targetName)
    }
  }
}

</script>
