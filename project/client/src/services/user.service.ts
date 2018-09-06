import axios from "axios";

import { User } from "./user";

const api = "/api/v0"


class UserService {
    constructor() {
    }
    login(username: string, password: string) {
        let data = {
            "username": username,
            "password": password
        }
        return axios.post(`${api}/users/auth/`)
    }
    logout() {
        
    }
    addUser(user: User) {
        return axios.post(`${api}/users/`, { user });
    }
    updateUser(user: User) {
        return axios.put(`${api}/users/${user.id}/`, { user });
    }
    deleteUser(user: User) {
        return axios.delete(`${api}/users/${user.id}/`);
    }
    getUsers() {
        return axios.get<User[]>(`${api}/users/`);
    }
}

export const userService = new UserService();
