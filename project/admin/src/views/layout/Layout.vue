<template>
    <div>
        <sidebar class="sidebar-container">
        </sidebar>
        <div class="main-container">
            <navbar>
            </navbar>
            <app-main>
            </app-main>
        </div>
    </div>
</template>

<script>
import { Navbar, Sidebar, AppMain } from './components';

export default {
    name: 'layout',
    components: {
        Navbar,
        Sidebar,
        AppMain
    },
};
</script>

<style lang="scss">
</style>

