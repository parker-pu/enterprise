<template id="header">
  <div>
    <el-row class="container">
      <!--头部-->
      <el-col :span="24" class="topbar-wrap">
        <!--图标-->
        <div class="topbar-logo topbar-btn">
          <!--<img :src="imgUrl" style="padding-left:4px;">-->
        </div>
        <!--选项-->
        <div class="topbar-logos">
          <span style="color: #fff;">FoolMongo</span>
        </div>
        <!-- 中间的部分 -->
        <div class="topbar-title">
          <el-row>
            <!-- 注意：这里就是topNavState作用之处，根据当前路由所在根路由的type值判断显示不同顶部导航菜单 -->
            <el-col :span="24">
              <el-menu
                class="el-menu-demo"
                mode="horizontal"
                @select="handleSelect"
                :router="true"
              >
                <el-menu-item index="/task">查看任务</el-menu-item>
                <!--<el-menu-item index="/select">查询</el-menu-item>-->
                <el-menu-item index="/mongo-to-mysql">添加任务</el-menu-item>
                <el-menu-item index="/db-source">数据源</el-menu-item>
              </el-menu>
            </el-col>
          </el-row>
        </div>
        <!--最右侧-->
        <div class="topbar-account topbar-btn">
          <el-dropdown trigger="click">
            <span class="el-dropdown-link userinfo-inner">
              <i class="iconfont icon-user"></i>
              {{ userInfo.username }}
              <i class="el-icon-caret-bottom"></i>
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item divided @click.native="goUserInfo">
                <div>
                  <span style="color: #555;font-size: 14px;">个人信息</span>
                </div>
              </el-dropdown-item>
              <!--<el-dropdown-item>-->
              <!--<div><span style="color: #555;font-size: 14px;">修改密码</span></div>-->
              <!--</el-dropdown-item>-->
              <el-dropdown-item divided @click.native="logout">
                退出登录
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-col>
    </el-row>
    <div>
      <el-dialog
        title="个人信息"
        :visible.sync="openUserInfo"
        :close-on-click-modal="false"
      >
        <el-form :model="seeUserInfo" label-width="100px">
          <el-form-item label="用户名：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.username }}</span>
          </el-form-item>
          <el-form-item label="用户状态：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.is_active }}</span>
          </el-form-item>
          <el-form-item
            :formatter="dateFormat"
            label="最近登录："
            :label-width="seeWidth"
          >
            <span style="float: left">{{ seeUserInfo.last_login }}</span>
          </el-form-item>
          <el-form-item label="超级用户：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.is_superuser }}</span>
          </el-form-item>
          <el-form-item label="姓：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.first_name }}</span>
          </el-form-item>
          <el-form-item label="名：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.last_name }}</span>
          </el-form-item>
          <el-form-item label="邮箱：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.email }}</span>
          </el-form-item>
          <el-form-item
            :formatter="dateFormat"
            label="创建时间："
            :label-width="seeWidth"
          >
            <span style="float: left">{{ seeUserInfo.date_joined }}</span>
          </el-form-item>
        </el-form>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import store from "../store";
import moment from "moment";
import { mapState } from "vuex";

export default {
  store,
  computed: {
    ...mapState({
      userInfo: "userInfo"
    })
  },
  data() {
    return {
      activeName: "first",
      imgUrl: require("../assets/logo.png"),
      defaultActiveIndex: "/",
      loading: false,
      openUserInfo: false,
      seeUserInfo: {},
      seeWidth: "120px"
    };
  },
  // // 在页面加载的时候，调这个函数
  // created: function() {
  //   this.getUserInfo();
  // },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    // 时间格式化
    dateFormat(row, column) {
      let date = row[column.property];
      if (date === undefined) {
        return "";
      }
      return moment(date).format("YYYY-MM-DD HH:mm:ss");
    },
    goUserInfo() {
      this.seeUserInfo = this.userInfo;
      this.openUserInfo = true;
    },
    logout() {
      // 清除token
      this.$store.commit("clearUser");
      if (!this.$store.state.User.Token) {
        this.$router.push("/login");
        this.$message({
          type: "success",
          message: "退出成功"
        });
      } else {
        this.$message({
          type: "info",
          message: "退出失败"
        });
      }
    }
  }
};
</script>

<style></style>

<style scoped></style>
