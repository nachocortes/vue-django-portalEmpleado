import {defineStore} from 'pinia';
import axios from "axios";
import {useAuthStore} from "@/stores/auth.js";

const API_SERVER = import.meta.env.VITE_API_SERVER;
const API_ENDPOINT = 'api';

export const useCalendarioStore = defineStore("calendarios", {

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
                const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/calendarios`);
                this.items = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async save(calendario) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.post(`${API_SERVER}/${API_ENDPOINT}/calendarios/`, calendario, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('calendario guardado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al guardar el calendario', error);
                }
            } else {
                throw new Error('El usuario debe estar autenticado', error);
            }
        },
        async update(calendario) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.put(`${API_SERVER}/${API_ENDPOINT}/calendarios/${calendario.id}/`, calendario, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('calendario editado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al editar el calendario', error);
                }
            } else {
                throw new Error('El usuario debe estar autenticado', error);
            }
        },
        async detail() {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/user/calendarios`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    alert('calendario obtenido con éxito');
                } catch (error) {
                    console.error('Error al obtener el calendario', error);
                }
            } else {
                throw new Error('El usuario debe estar autenticado', error);
            }
        },
        async fetchUserCalendarios() {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/user/calendarios`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.items = response.data;
                    alert('Calendarios obtenidos con éxito');
                } catch (error) {
                    console.error('Error al obtener los calendarios del usuario', error);
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async delete(calendario) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.delete(`${API_SERVER}/${API_ENDPOINT}/calendarios/${calendario.id}`, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('calendario eliminado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al eliminar el calendario', error);
                }
            } else {
                throw new Error('El usuario debe estar autenticado', error);
            }
        }
    }
});
