import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

app.use(router);
app.config.globalProperties.$filters = {
    pluralize(value, word) {
        if (value !== 1) {
            return word + "s";
        }
        return word;
    }
  }

app.mount("#app");
