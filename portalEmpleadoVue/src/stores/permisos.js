import {defineStore} from 'pinia';
import axios from "axios";
import {useAuthStore} from "@/stores/auth.js";

const API_SERVER = import.meta.env.VITE_API_SERVER;
const API_ENDPOINT = 'api';

export const usePermisoStore = defineStore("permisos", {
    state: () => ({
        items: [],
    }),
    getters: {
        length(state) {
            return state.items.length;
        }
    },
    actions: {
        async fetch() {
            try {
                const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/permisos`);
                this.items = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async save(permiso) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.post(`${API_SERVER}/${API_ENDPOINT}/permisos/`, permiso, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('permiso guardado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al guardar el permiso');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async update(permiso) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.put(`${API_SERVER}/${API_ENDPOINT}/permisos/${permiso.id}/`, permiso, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Permiso editado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al editar el permiso');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async delete(permiso) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.delete(`${API_SERVER}/${API_ENDPOINT}/permisos/${permiso.id}`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Permiso eliminado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al eliminar el permiso');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        }
    }
});
