<template>
    <div id="app" class="app">
        <el-container class="main-container">
            <el-aside width="200px">
                <el-menu
                    class="el-menu-vertical"
                    @open="handleOpen"
                    @close="handleClose"
                    background-color="#304156"
                    text-color="#fff"
                    active-text-color="#3399FF"
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
    @import url("https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900&amp;subset=cyrillic");
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
        font-family: 'Roboto';
    }
    .main-container {
        height: 100%;
    }
    .el-header {
        background-color: #304156;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    .el-aside {
        height: 100%;
        background-color: #545c64;
    }
    .el-menu {
        border-right: none !important;
    }
    .el-menu-vertical {
        height: 100%;
    }
</style>
