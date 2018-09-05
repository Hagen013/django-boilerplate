import Vue from "vue"
import Element from "element-ui"

Vue.use(Element)

new Vue({
    el: "#login-form",
    created() {
        console.log(Element);
        console.log("CREATED");
    }
});
