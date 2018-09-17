<template>
    <div id="app" class="app">
        <router-view/>
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
</style>
