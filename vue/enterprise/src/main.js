import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Axios from "axios";
import VueAxios from "vue-axios";
import {
  Button,
  Select,
  Dialog,
  Form,
  FormItem,
  Menu,
  MenuItem,
  Row,
  Col,
  Dropdown,
  DropdownMenu,
  DropdownItem,
  Table,
  TableColumn,
  Input,
  Option,
  Tabs,
  TabPane,
  Radio,
  RadioGroup,
  Loading,
  Steps,
  DatePicker,
  Container,
  Header,
  Main,
  Alert,
  Step,
  MessageBox,
  Notification,
  Message
} from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

Vue.use(VueAxios, Axios);
// element 按需引入
Vue.use(Button);
Vue.use(Option);
Vue.use(Select);
Vue.use(Row);
Vue.use(Col);
Vue.use(Dropdown);
Vue.use(DropdownMenu);
Vue.use(DropdownItem);
Vue.use(Dialog);
Vue.use(Form);
Vue.use(FormItem);
Vue.use(Menu);
Vue.use(MenuItem);
Vue.use(Table);
Vue.use(TableColumn);
Vue.use(Input);
Vue.use(Tabs);
Vue.use(TabPane);
Vue.use(Radio);
Vue.use(RadioGroup);
Vue.use(Steps);
Vue.use(DatePicker);
Vue.use(Container);
Vue.use(Header);
Vue.use(Main);
Vue.use(Alert);
Vue.use(Step);

Vue.prototype.$loading = Loading.service; // 载入的时候
Vue.prototype.$confirm = MessageBox.confirm; // 提示删除
Vue.prototype.$notify = Notification; // 左上脚弹出
Vue.prototype.$message = Message;

Vue.config.productionTip = false;
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
