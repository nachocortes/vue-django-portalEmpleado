import {defineStore} from 'pinia';
import axios from "axios";
import {useAuthStore} from "@/stores/auth.js";

const API_SERVER = import.meta.env.VITE_API_SERVER;
const API_ENDPOINT = 'api';

export const useDepartamentoStore = defineStore("departamentos", {

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
                const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/departamentos`);
                this.items = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async save(departamento) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.post(`${API_SERVER}/${API_ENDPOINT}/departamentos/`, departamento, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Departamento guardado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al guardar el departamento');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async update(departamento) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.put(`${API_SERVER}/${API_ENDPOINT}/departamentos/${departamento.id}/`, departamento, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Departamento editado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al editar el departamento');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async delete(departamento) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.delete(`${API_SERVER}/${API_ENDPOINT}/departamentos/${departamento.id}`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Departamento eliminado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al eliminar el departamento');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        }
    }
});
