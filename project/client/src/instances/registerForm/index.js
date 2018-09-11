import { Vue } from "./../../vue.js";
import Element from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import store from "./../../store";

Vue.use(Element)

new Vue({
    el: "#register-form",
    store,
    data: {
        email: "",
        password: "",
        password2: ""
    },
    computed: {
        passwordMatches() {
            return this.password === this.password2
        }
    },
    methods: {
        submit() {
            
        }
    }
});
