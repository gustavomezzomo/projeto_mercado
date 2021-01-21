<template>
  <v-app-bar color="red" class="yellow--text" dark fixed app clipped-right>
    <v-layout justify-center align-center>
      <v-toolbar-title>Mercado Santa Inês</v-toolbar-title>
    </v-layout>
  </v-app-bar>
</template>

<script>
import Snacks from '~/helpers/Snacks.js'
import api from '~api'
export default {
  props: ['state'],
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  methods: {
    open_login_dialog (evt) {
      this.$refs.login_dialog.open()
      evt.stopPropagation()
    },
    async logout () {
      await api.logout()
      this.$store.commit('auth/setCurrentUser', null)
      Snacks.show(this.$store, {text: 'Até logo!'})
    }
  }
}
</script>
