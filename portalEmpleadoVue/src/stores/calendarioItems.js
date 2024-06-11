import { defineStore } from 'pinia';
import axios from "axios";
import { useAuthStore } from "@/stores/auth.js";

const API_SERVER = import.meta.env.VITE_API_SERVER;
const API_ENDPOINT = 'api';

export const useCalendarioItemStore = defineStore("calendarioItems", {
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
                const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/calendarioItems`);
                this.items = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async save(calendarioItem) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.post(`${API_SERVER}/${API_ENDPOINT}/calendarioItems/`, calendarioItem, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();

                } catch (error) {
                    console.log(error);
                    alert('Error al guardar las fechas del calendario');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async update(calendarioItem) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.put(`${API_SERVER}/${API_ENDPOINT}/calendarioItems/${calendarioItem.id}/`, calendarioItem, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();

                } catch (error) {
                    console.log(error);
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async fetchItemsByCalendario(calendarioId) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/calendarios/${calendarioId}/items/`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.items = response.data;

                } catch (error) {
                    console.log(error);
                    alert('Error al cargar las fechas del calendario');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async detail(calendarioId) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/calendarios/${calendarioId}/items/`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Fechas del calendario cargadas con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al cargar las fechas del calendario');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async delete(calendarioItem) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.delete(`${API_SERVER}/${API_ENDPOINT}/calendarioItems/${calendarioItem.id}`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();

                } catch (error) {
                    console.log(error);
                    alert('Error al eliminar las fechas del calendario');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async deleteItem(calendarioItemId) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.delete(`${API_SERVER}/${API_ENDPOINT}/calendarioItems/${calendarioItemId}`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();

                } catch (error) {
                    console.log(error);
                    alert('Error al eliminar las fechas del calendario');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        }
    }
});
