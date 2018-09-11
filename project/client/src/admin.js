"use strict";

import Vue from 'vue';

import Element from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

import store from './store';
import { router } from './admin/router'
import App from './admin/App.vue';

Vue.use(Element);

new Vue({
    el: '#app',
    store,
    router,
    render: h => h(App)
});
