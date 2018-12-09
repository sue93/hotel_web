
 <template>
  <div>
    <div v-for="o in objs" :objs="o.child" :key="o.id">
      <el-submenu v-if="Object.keys(o.child).length!=0" :index="o.id">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>{{o.name}}</span>
        </template>

        <elmenua :objs="o.child"></elmenua>
      </el-submenu>

      <el-menu-item v-else :index="o.id" :route="{name:'hello'}">
        <i class="el-icon-menu"></i>
        <span slot="title">{{o.name}}1</span>
      </el-menu-item>
    </div>
  </div>
</template>
<script>
export default {
  name: 'elmenua',
  props: ['objs']
}
</script>
