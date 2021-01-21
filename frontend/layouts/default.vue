<template>
  <v-app id="inspire" class="site_root">
    <toolbar :state="layout" />
    <v-content>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-content>
    <le-footer />
    <v-snackbar
      :timeout="snack.timeout"
      :color="snack.color"
      bottom
      v-model="snack.visible"
    >
      {{snack.text}}
      <v-btn dark flat @click.native="snack.visible = false">Close</v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
import toolbar from '~/components/toolbar.vue'
import footer from '~/components/footer.vue'
export default {
  components: {
    toolbar,
    leFooter: footer
  },
  data: () => ({
    layout: {
      drawer: true
    }
  }),
  computed: {
    snack () {
      return JSON.parse(JSON.stringify(this.$store.state.snack.snack))
    }
  },
  methods: {
    closeSnack () {
      this.$store.commit('snack/hide')
    }
  }
}
</script>

<style scoped>
  .site_root {
    background-color: yellow;
  }
</style>
