<template>
    <el-scrollbar wrap-class="scrollbar-wrapper">
        <el-menu
            mode="vertical"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#00ef81"
        >
            <el-menu-item index="1">
                <i class="el-icon-goods"></i>
                <span>Заказы</span>
            </el-menu-item>
            <el-menu-item index="2">
                <i class="el-icon-setting"></i>
                <span>Настройки</span>
            </el-menu-item>
        </el-menu>
    </el-scrollbar>
</template>

<script>
export default {
    name: "sidebar",
    components: {}
};
</script>

<style lang="scss">
</style>
