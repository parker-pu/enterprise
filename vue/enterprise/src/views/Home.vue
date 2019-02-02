<template>
  <div>
    <el-container>
      <el-aside :width="leftSize" class="aside">
        <Left v-on:listenToChildEvent="updateLeft"></Left>
      </el-aside>
      <el-container>
        <!-- 面包屑 -->
        <el-header>
          <Breadcrumb></Breadcrumb>
        </el-header>
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Left from "../components/Left";
import Breadcrumb from "../components/Breadcrumb";

export default {
  name: "Home",
  components: {
    Left,
    Breadcrumb
  },
  data() {
    return {
      imgUrl: require("../assets/logo.png"),
      leftSize: "65px"
    };
  },
  methods: {
    updateLeft(isCollapse) {
      if (isCollapse === true) {
        this.leftSize = "65px";
      } else {
        this.leftSize = "151px";
      }
    }
  }
};
</script>

<style scoped>
.el-header {
  background-color: #ffffff;
  color: #333;
  line-height: 60px;
}
</style>
