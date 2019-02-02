import instance from "../utils/axios";

export default {
  // 根据 token 获取 User 的信息
  tokenUserInfo() {
    return instance.post("/api-token-auth/");
  }
};
