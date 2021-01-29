import { get, post } from '~/helpers/api/ajaxutils'
import axios from '~/helpers/axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

export default {
  login (username, password) {
    return post('/api/login', { username, password })
  },
  logout () {
    return post('/api/logout')
  },
  whoami () {
    return get('/api/whoami')
  },
  add_todo (newtask) {
    return post('/api/add_todo', { new_task: newtask })
  },
  list_todos () {
    return get('/api/list_todos')
  },
  image () {
    return get('/api/image')
  }
}