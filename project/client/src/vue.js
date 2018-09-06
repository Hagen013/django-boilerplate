import Vue from 'vue';
import Vuex from 'vuex';
import Axios from 'axios'

import csrfToken from './helpers/csrfToken'


Axios.defaults.headers.common = {
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN' : csrfToken()
};

Vue.use(Vuex);
Vue.prototype.$http = Axios;


export {
    Vue,
    Vuex,
    Axios
}