<template>
    <div class="app-container"
    >
        <h1>Категории</h1>
        <div class="table">
            <div class="table__controls">
                <div class="table__buttons">
                    <el-button type="primary"
                        @click="handleCreateClick"
                    >
                        Создать
                    </el-button>
                </div>
                <div class="table__filters">
                    <div class="filter-field"
                        v-for="item in tableFilters"
                        :key=item.field
                    >
                        <el-input v-if="item.type==='string'"
                            :placeholder="item.label"
                            v-model="item.value"
                        >
                        </el-input>
                    </div>
                </div>
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
import debounce from 'debounce'

import shopApi from '@/api/shop'


export default {
    name: 'Categories',
    data: () => ({
        loading: true,
        tableItems: [],
        routes: {
            create: '/shop/categories/create',
            retrieve: '/shop/categories/',
        },
        tableProps: [
            {
                value: 'id',
                label: 'ID',
                sortable: true
            },
            {
                value: 'name',
                label: 'Наименование',
                sortable: false
            },
            {
                value: 'url',
                label: 'URL',
                sortable: false
            },
            {
                value: 'level',
                label: 'Глубина',
                sortable: true
            }
        ],
        tableFilters: [
            {
                lookupField: 'search',
                label: 'наименование',
                type: 'string',
                value: ''
            },
            {
                lookupField: 'is_published',
                label: 'опубликован',
                type: 'boolean',
                value: false
            },
            {
                lookupField: 'parent',
                label: 'ID родительской категории',
                type: 'number',
            }
        ],
        showFilters: false
    }),
    computed: {
        queryParams() {
            let params = {};
            for (let i=0; i<this.tableFilters.length; i++) {
                let field = this.tableFilters[i].lookupField;
                let value = this.tableFilters[i].value;
                let filterType = this.tableFilters[i].type;
                if (filterType === 'string') {
                    if (value !== '') {
                        params[field] = value;
                    }
                }
            }
            return params
        }
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
            shopApi.categories.list(this.queryParams).then(
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
        },
        handleCreateClick() {
            this.$router.push({path: this.routes.create})
        }
        // Response handlers end
    },
    watch: {
        queryParams: {
            handler: debounce(function() {
                this.getList();
            }, 300),
            deep: true
        }
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
    .filter-field {
        max-width: 300px;
    }
</style>
