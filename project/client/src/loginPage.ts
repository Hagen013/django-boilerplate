import Vue from "vue"
import Element from "element-ui"
import "element-ui/lib/theme-chalk/index.css";

Vue.use(Element)

new Vue({
    el: "#login-form",
    created() {
        console.log("CREATED");
    }
});
