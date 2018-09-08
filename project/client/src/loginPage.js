import { Vue } from "./vue.js"
import Element from "element-ui"
import "element-ui/lib/theme-chalk/index.css";

import store from "./store/index.js"

Vue.use(Element)

new Vue({
    el: "#login-form",
    store,
    created() {
        console.log("Createds");
    },
    methods: {
        submit() {
            
        }
    }
});
