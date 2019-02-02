import Vuex from "vuex";
import Vue from "vue";

Vue.use(Vuex);
export default new Vuex.Store({
  modules: {},
  state: {
    // 用户的Token信息
    User: {
      // 获取用户名
      get Name() {
        return localStorage.getItem("userName");
      },
      // 获取 token
      get Token() {
        return localStorage.getItem("userToken");
      },
      // 获取过期时间
      get Expires() {
        return localStorage.getItem("tokenExpires");
      }
    },
    /*域名*/
    domainName: "http://127.0.0.1:8000"
  },
  getters: {
    _isMobile() {
      let flag = navigator.userAgent.match(
        /(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i
      );
      return flag;
    }
  },
  mutations: {
    setUser(state, { userName, userToken, tokenExpires }) {
      // 在这里把用户名和token保存起来
      localStorage.setItem("userName", userName);
      localStorage.setItem("userToken", userToken);
      localStorage.setItem("tokenExpires", tokenExpires);
    },
    // 清除用户保存在本地的信息
    clearUser() {
      localStorage.clear();
    }
  },
  actions: {}
});
