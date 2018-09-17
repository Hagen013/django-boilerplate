import Vue from 'vue';
import Router from 'vue-router';

import Layout from '@/views/layout/Layout'
import Home from '@/views/Home.vue';
import Login from '@/views/Login.vue';

Vue.use(Router);

const publicPages = ['/login'];

export const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/',
            component: Layout,
            redirect: '/dashboard',
            name: 'Home',
            hidden: true,
            children: [{
                path: 'dashboard',
                component: () => import('@/views/Home.vue')
            }]
        },
        {
            path: '/users',
            component: Layout,
            name: 'Users',
            hidden: true,
            children: [{
                path: 'users',
                component: () => import('@/views/Users.vue')
            }]
        },
        { path: '*', redirect: '/' }
    ],
});

// router.beforeEach((to, from, next) => {
//     // redirect to login page if not logged in and trying to access a restricted page
//     const authRequired = !publicPages.includes(to.path);
//     const loggedIn = localStorage.getItem('user');
//     if (authRequired && !loggedIn) {
//         return next('/login');
//     }
//     next();
// })
