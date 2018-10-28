import request from '@/utils/request'

const shop = {
    categories: {
        list() {
            return request.get('/categories')
        },
        create() {
            return null
        },
        get(id) {
            return request.get(`/categories/${id}/`);
        },
        update(id) {
            return null
        },
        delete(id) {
            return null
        }
    },
}

export default shop;