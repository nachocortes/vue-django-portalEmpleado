import {defineStore} from 'pinia';
import axios from "axios";
import {useAuthStore} from "@/stores/auth.js";

const API_SERVER = import.meta.env.VITE_API_SERVER;
const API_ENDPOINT = 'api';

export const useAusenciaStore = defineStore("ausencias", {
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
                const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/ausencias`);
                this.items = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async save(ausencia) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.post(`${API_SERVER}/${API_ENDPOINT}/ausencias/`, ausencia, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('ausencia guardada con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al guardar la ausencia');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async update(ausencia) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.put(`${API_SERVER}/${API_ENDPOINT}/ausencias/${ausencia.id}/`, ausencia, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Ausencia editada con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al editar la ausencia');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async delete(ausencia) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.delete(`${API_SERVER}/${API_ENDPOINT}/ausencias/${ausencia.id}`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Ausencia eliminada con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al eliminar la ausencia');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        }
    }
});
