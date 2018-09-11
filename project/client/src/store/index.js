import { Vuex } from '../vue.js';

import { alert } from './alert.module';
import { authentication } from './authentication.module';


export default new Vuex.Store({
    modules: {
        alert,
        authentication,
    },
    getters: {
        
    }
});
