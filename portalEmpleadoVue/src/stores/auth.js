import {defineStore} from 'pinia';
import axios from "axios"

const API_SERVER = import.meta.env.VITE_API_SERVER;
const API_ENDPOINT = 'auth/jwt';


export const useAuthStore = defineStore({
    id: 'auth',

    state: () => ({
        user: JSON.parse(localStorage.getItem('user')),
    }),
    getters: {

        isAuthenticated(state) {
            if (state.user !== null) {
            }
            return state.user !== null;
        },

        token(state) {
            return `JWT ${state.user.access}`;
        },
    },

    actions: {
        async login(username, password) {
            try {
                const response = await axios.post(`${API_SERVER}/${API_ENDPOINT}/create`, {username, password});
                this.user = response.data;
                localStorage.setItem('user', JSON.stringify(response.data));

            } catch (error) {
                console.log(error);
            }
        },
        logout() {
            this.user = null;
            localStorage.removeItem('user');
        }
    }
});
