<template>
    <div id="app" class="app">
        <el-container class="main-container">
            <el-aside width="200px">
                <el-menu
                    class="el-menu-vertical"
                    @open="handleOpen"
                    @close="handleClose"
                    background-color="#545c64"
                    text-color="#fff"
                    active-text-color="#ffd04b"
                >
                    <div class="menu-placeholder">
                    </div>
                    <el-submenu index="1">
                        <template slot="title">
                            <i class="el-icon-goods"></i>
                            <span>Заказы</span>
                        </template>
                    </el-submenu>
                    <el-submenu index="2">
                        <template slot="title">
                            <i class="el-icon-goods"></i>
                            <span>Товары</span>
                        </template>
                    </el-submenu>
                    <el-submenu index="3">
                        <template slot="title">
                            <i class="el-icon-goods"></i>
                            <span>Страницы</span>
                        </template>
                    </el-submenu>
                    <el-menu-item index="3">
                        <i class="el-icon-menu"></i>
                        <span>Пользователи</span>
                    </el-menu-item>
                    <el-menu-item index="4">
                        <i class="el-icon-menu"></i>
                        <span>Платежи</span>
                    </el-menu-item>
                </el-menu>
            </el-aside>
            <el-container>
                <el-header>
                </el-header>
                <el-main>
                    <router-view/>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
export default {
    name: 'app',
    methods: {
        handleOpen() {
        },
        handleClose() {
        }
    }
}
</script>


<style lang="scss">
    * {
        box-sizing: border-box;
    }
    html {
        min-height: 100vh;
    }
    body {
        margin: 0px;
        height: 100vh;
    }
    .app {
        height: 100%;
    }
    .main-container {
        height: 100%;
    }
    .el-header {
        background-color: #545c64;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    .el-aside {
        height: 100%;
        background-color: #545c64;
    }
    .el-menu {
        border-right: none;
    }
    .el-menu-vertical {
        height: 100%;
    }
    .el-main {
        background-color: #E9EEF3;
        color: #333;
        text-align: center;
        line-height: 160px;
    }
</style>