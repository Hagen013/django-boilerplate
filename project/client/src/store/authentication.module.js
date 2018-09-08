import { userService } from '../services';


export const authentication = {
    namespaced: true,
    state: {

    },
    actions: {
        login({dispatch, commit}, { username, password }) {
            commit('loginRequest', { username });

            userService.login(username, password).then(
                user => {
                    commit('loginSuccess', user);
                },
                error => {
                    commit('loginFailure', error);
                    dispatch('alert/error', error);
                }
            )
        },
        logout({commit}) {
            userService.logout();
            commit('logout');
        }
    },
    mutations: {
        loginRequest(state, user) {
            state.status = { loggingIn: true };
            state.user = user;
        },
        loginSuccess(state, user) {
            state.status = { loggedIn: true };
            state.user = user;
        },
        loginFailure(state) {
            state.status = {};
            state.user = null;
        },
        logout(state) {
            state.status = {};
            state.user = null;
        }
    }
}