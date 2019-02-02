<template id="left">
  <!-- 左边 -->
  <div>
    <el-menu
      default-active="/"
      class="el-menu-vertical-demo"
      :collapse="isCollapse"
      router
    >
      <el-menu-item index="">
        <i class="el-icon-arrow-right" v-if="isCollapse" @click="openLeft"></i>
        <i class="el-icon-arrow-left" v-else @click="closeLeft"></i>
      </el-menu-item>
      <el-menu-item index="/list-img">
        <i class="el-icon-menu"></i>
        <span slot="title">首页</span>
      </el-menu-item>
      <el-menu-item index="/upload-img">
        <i class="el-icon-edit"></i>
        <span slot="title">爬虫配置</span>
      </el-menu-item>
      <el-menu-item index="/put-password">
        <i class="el-icon-setting"></i>
        <span slot="title">设置</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isCollapse: true
    };
  },
  methods: {
    closeLeft() {
      this.isCollapse = true;
      this.$emit("listenToChildEvent", this.isCollapse);
    },
    openLeft() {
      this.isCollapse = false;
      this.$emit("listenToChildEvent", this.isCollapse);
    }
  }
};
</script>

<style scoped>
.el-menu-vertical-demo {
  position: absolute;
  left: 0;
  top: 0;
  min-height: 100vh;
  color: #999;
  background-color: #323544;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 150px;
  min-height: 100vh;
  color: #999;
  background-color: #323544;
}
.el-menu-item {
  font-size: 14px;
  color: #999;
  cursor: pointer;
}
/* 鼠标移动到字体的颜色 */
.el-menu-item:hover {
  background: #404351;
  cursor: pointer;
  color: #fff;
}
/* 设置图标的颜色 */
.el-menu-item i {
  color: rgb(184, 190, 196);
}
.el-menu-item i:hover {
  color: #fff;
}
</style>

<style scoped></style>
