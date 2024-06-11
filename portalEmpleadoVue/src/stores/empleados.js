import {defineStore} from 'pinia';
import axios from "axios";
import {useAuthStore} from "@/stores/auth.js";

const API_SERVER = import.meta.env.VITE_API_SERVER;
const API_ENDPOINT = 'api';

export const useEmpleadoStore = defineStore("empleados", {
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
                const response = await axios.get(`${API_SERVER}/${API_ENDPOINT}/empleados`);
                this.items = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async save(empleado) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.post(`${API_SERVER}/${API_ENDPOINT}/empleados/`, empleado, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Empleado guardado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al guardar el empleado');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async update(empleado) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.put(`${API_SERVER}/${API_ENDPOINT}/empleados/${empleado.id}/`, empleado, {
                        headers: {
                            'Authorization': auth.token,
                        }
                    });
                    this.fetch();
                    alert('Empleado editado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al editar el empleado');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        },
        async delete(empleado) {
            const auth = useAuthStore();

            if (auth.isAuthenticated) {
                try {
                    const response = await axios.delete(`${API_SERVER}/${API_ENDPOINT}/empleados/${empleado.id}`, {
                        headers: {
                            'Authorization': auth.token,
                            'user': this.auth
                        }
                    });
                    this.fetch();
                    alert('Empleado eliminado con éxito');
                } catch (error) {
                    console.log(error);
                    alert('Error al eliminar el empleado');
                }
            } else {
                throw new Error('El usuario debe estar autenticado');
            }
        }
    }
});
