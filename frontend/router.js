import Vue from 'vue'
import Router from 'vue-router'
import Index from '~/pages/index.vue'
import Todos from '~/pages/todos.vue'
import setores from '~/pages/setores.vue'
import acougue from '~/pages/acougue.vue'
import bolos from '~/pages/bolos.vue'
import padaria from '~/pages/padaria.vue'
import achocolatados from '~/pages/achocolatados.vue'
import bebidas_alcoolicas from '~/pages/bebidas_alcoolicas.vue'
import higiene from '~/pages/higiene.vue'
import salgadinhos from '~/pages/salgadinhos.vue'
import especiarias from '~/pages/especiarias.vue'
import massas from '~/pages/massas.vue'
import congelados from '~/pages/congelados.vue'
import chocolates from '~/pages/chocolates.vue'
import utilidades from '~/pages/utilidades.vue'
import hortifruti from '~/pages/hortifruti.vue'
import enlatados from '~/pages/enlatados.vue'
import bebidas from '~/pages/bebidas.vue'

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  routes: [
    {path: '/', component: Index, name: 'index'},
    { path: '/todos', component: Todos, name: 'todos' },
    { path: '/setores', component: setores, name: 'setores' },
    { path: '/setores/acougue', component: acougue, name: 'acougue' },
    { path: '/setores/bolos', component: bolos, name: 'bolos' },
    { path: '/setores/padaria', component: padaria, name: 'padaria' },
    { path: '/setores/achocolatados', component: achocolatados, name: 'achocolatados' },
    { path: '/setores/bebidas_alcoolicas', component: bebidas_alcoolicas, name: 'bebidas_alcoolicas' },
    { path: '/setores/higiene', component: higiene, name: 'higiene' },
    { path: '/setores/salgadinhos', component: salgadinhos, name: 'salgadinhos' },
    { path: '/setores/especiarias', component: especiarias, name: 'especiarias' },
    { path: '/setores/massas', component: massas, name: 'massas' },
    { path: '/setores/congelados', component: congelados, name: 'congelados' },
    { path: '/setores/chocolates', component: chocolates, name: 'chocolates' },
    { path: '/setores/utilidades', component: utilidades, name: 'utilidades' },
    { path: '/setores/hortifruti', component: hortifruti, name: 'hortifruti' },
    { path: '/setores/enlatados', component: enlatados, name: 'enlatados' },
    { path: '/setores/bebidas', component: bebidas, name: 'bebidas' }
  ]
}

export function createRouter (ctx) {
  return new Router(routerOptions)
}
