<template>
    <div class="app-container"
    >
        <h1>Категории</h1>
        <div class="table">
            <div class="table__controls">
            </div>
            <div class="table__content">
                    <tr class="table__header">
                        <th class="table__head"
                            v-for="prop in tableProps"
                            :key="prop.value"
                        >
                            <div class="table__head-container">
                                {{prop.label}}
                            </div>
                        </th>
                    </tr>
                    <tr class="table__row"
                        v-for="item in tableItems"
                        :key="item.id"
                        @click="selectItem(item)"
                    >
                        <td class="table__cell"
                            v-for="prop in tableProps"
                            :key="prop.value"
                        >
                            <div class="table__cell-container">
                                {{item[prop.value]}}
                            </div>
                        </td>
                    </tr>
            </div>
        </div>
    </div>
</template>

<script>
import shopApi from '@/api/shop'

export default {
    name: 'Categories',
    data: () => ({
        loading: true,
        tableItems: [],
        tableProps: [
            {
                value: 'id',
                label: 'ID'
            },
            {
                value: 'name',
                label: 'Наименование'
            },
            {
                value: 'url',
                label: 'URL'
            },
            {
                value: 'level',
                label: 'Глубина'
            }
        ]
    }),
    computed: {
    },
    created() {
        this.initialize();
    },
    mounted() {
    },
    methods: {
        initialize() {
            this.getList();
        },
        getList() {
            shopApi.categories.list().then(
                response => {
                    this.handleSuccessfulListResponse(response);
                },
                error => {
                    this.handleErrorListResponse(error);
                }
            )
        },
        selectItem(item) {
            let path = `/shop/categories/${item.id}`;
            this.$router.push({path: path});
        },
        // Response handlers start
        handleSuccessfulListResponse(response) {
            this.loading = false;
            this.tableItems = response.data.results;
        },
        handleErrorListResponse(response) {
            this.loading = false;
        }
        // Response handlers end
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
    tbody {
        width: 100%;
    }
    .table__content {
        display: table;
        width: 100%;
    }
    .table__row {
        width: 100%;
    }
    .table__head {
        height: 48px;
    }
    .table__head-container {
        display: flex;
        align-items: center;
        padding: 0px 16px;
        height: 100%;
        width: 100%;
    }
    .table__cell {
        height: 48px;
        border-top-color: rgba(0,0,0,.12);
        border-top: 1px solid rgba(0,0,0,.12);
    }
    .table__cell-container {
        display: flex;
        align-items: center;
        padding: 0px 16px;
        height: 100%;
        width: 100%;
    }
    .table__row {
        transition: .3s cubic-bezier(.4,0,.2,1);
        transition-property: background-color,font-weight;
        will-change: background-color,font-weight;
        cursor: pointer;
        &:hover {
            background-color: rgba(0,0,0,.08);
        }

    }
    .text_left {
        text-align: left;
    }
    .text_center {
        text-align: center;
    }
    .text_right {
        text-align: right;
    }
</style>
